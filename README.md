# Pondicherry Taxi Booking Website

Multi-page taxi booking website for Pondicherry and Tamil Nadu tourism.

## Features

- **Responsive Design**: Mobile-friendly interface.
- **Booking System**: Direct WhatsApp integration for bookings.
- **Service Pages**: Local sightseeing, airport transfers, and outstation tours.
- **Security**: Content Security Policy (CSP) and input sanitization implemented.

## Tech Stack

- HTML5, CSS3, JavaScript (Vanilla)
- FontAwesome Icons
- Google Maps Embed

## Setup

1. Clone the repository.
2. Open `index.html` in your browser.

## Security Improvements

- Added Content Security Policy (CSP) headers.
- Implemented URL encoding for WhatsApp messages to prevent injection.
- added `rel="noopener noreferrer"` (implicit in new window opens) principles.

## Backend Server & Background Processing

This project now includes a Node.js backend (`server.js`) to:

1. **Store Bookings**: Automatically saves booking details to `bookings.csv`.
2. **Send Notifications**: Sends real-time Telegram alerts using a secure Bot.

### Setup (Local/Server)

1. Install Node.js.
2. Run `npm install` to install dependencies.
3. Create a `.env` file (see `.env.example`) with your Telegram credentials:
   ```
   TELEGRAM_BOT_TOKEN=your_token_here
   TELEGRAM_CHAT_ID=your_chat_id
   PORT=3000
   ```
4. Start the server:
   ```
   npm start
   ```
5. Open `http://localhost:3000`. Bookings will now be saved to `bookings.csv` and sent to Telegram in the background.

**Note:** For GitHub Pages hosting, the background server features (CSV/Telegram) will not work as it is a static host. You must host this on a platform like Render, Railway, or a VPS to use the backend features.
