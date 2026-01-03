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

### Deployment (Backend)

Since GitHub Pages handles only the frontend, you must host the backend separately for **CSV Storage** and **Telegram Notifications** to work.

**Recommended Free Host: Render**

1. Push this repository to GitHub.
2. Sign up at [render.com](https://render.com).
3. Click "New" > "Web Service".
4. Select your `Web` repository.
5. In Environment Variables, add:
   - `TELEGRAM_BOT_TOKEN`: (Your Token)
   - `TELEGRAM_CHAT_ID`: (Your Chat ID)
6. Click **Deploy**.
7. Copy your new Backend URL (e.g., `https://web-123.onrender.com`).

### connecting Frontend to Backend

Once your backend is live:

1. Open `index.html`, `Enquiry3.html`, and `scripts/booking3.js`.
2. Find `const BACKEND_URL = "http://localhost:3000";`.
3. Replace `http://localhost:3000` with your **Render URL**.
4. Commit and push. GitHub Pages will now talk to your live server!

**Note:** For GitHub Pages hosting, the background server features (CSV/Telegram) will not work as it is a static host. You must host this on a platform like Render, Railway, or a VPS to use the backend features.
