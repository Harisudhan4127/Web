const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const fs = require('fs');
const path = require('path');
const { createObjectCsvWriter } = require('csv-writer');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname))); // Serve static files from root

// CSV Writer Setup
const csvWriter = createObjectCsvWriter({
    path: 'bookings.csv',
    header: [
        {id: 'timestamp', title: 'TIMESTAMP'},
        {id: 'region', title: 'REGION'},
        {id: 'name', title: 'NAME'},
        {id: 'phone', title: 'PHONE'},
        {id: 'taxi', title: 'TAXI'},
        {id: 'pickup', title: 'PICKUP'},
        {id: 'drop', title: 'DROP'},
        {id: 'date', title: 'DATE'},
        {id: 'time', title: 'TIME'}
    ],
    append: true
});

// Telegram Settings
const TELEGRAM_BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN;
const TELEGRAM_CHAT_ID = process.env.TELEGRAM_CHAT_ID;

// API Route to Handle Booking
app.post('/api/book', async (req, res) => {
    const bookingData = req.body;
    
    // 1. Add Timestamp
    const timestamp = new Date().toLocaleString();
    bookingData.timestamp = timestamp;

    try {
        // 2. Save to CSV
        await csvWriter.writeRecords([bookingData]);
        console.log('Booking saved to CSV');

        // 3. Send Telegram Message
        if(TELEGRAM_BOT_TOKEN && TELEGRAM_CHAT_ID) {
            const message = `🚖 *NEW WEBSITE BOOKING* 🚖\n\n` +
                            `👤 *Name:* ${bookingData.name}\n` +
                            `📞 *Phone:* ${bookingData.phone}\n` +
                            `🚗 *Taxi:* ${bookingData.taxi}\n` +
                            `🌎 *Region:* ${bookingData.region}\n` +
                            `📍 *From:* ${bookingData.pickup}\n` +
                            `🏁 *To:* ${bookingData.drop}\n` +
                            `📅 *Date:* ${bookingData.date}\n` +
                            `⏰ *Time:* ${bookingData.time}\n` +
                            `⌚ *Submitted:* ${timestamp}`;

            // Use dynamic import or standard fetch if available, else require node-fetch
            const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));
            
            const telegramUrl = `https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`;
            await fetch(telegramUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    chat_id: TELEGRAM_CHAT_ID,
                    text: message,
                    parse_mode: 'Markdown'
                })
            });
            console.log('Telegram notification sent');
        }

        res.status(200).json({ success: true, message: 'Booking processed successfully' });

    } catch (error) {
        console.error('Error processing booking:', error);
        res.status(500).json({ success: false, message: 'Internal Server Error' });
    }
});

// Start Server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
