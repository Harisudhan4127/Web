document
  .getElementById("bookingForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    // Get Form Values
    const region = document.getElementById("region").value;
    const name = document.getElementById("custName").value;
    const phone = document.getElementById("phone").value;
    const pickup = document.getElementById("pickup").value;
    const drop = document.getElementById("drop").value;
    const date = document.getElementById("date").value;
    const time = document.getElementById("time").value;
    const taxi = document.getElementById("taxiType").value;

    // ⚠️ IMPORTANT: Replace with your Render/Railway URL for GitHub Pages
    const BACKEND_URL = "http://localhost:3000"; 

    // Get Current Timestamp
    const now = new Date();
    const currentBookingTime =
      now.toLocaleDateString() +
      " | " +
      now.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });

    const whatsappNumber = "919585641389";

    // Construct WhatsApp Message using standard newlines
    const messageText =
      `*NEW TAXI BOOKING*\n` +
      `--------------------------\n` +
      `🕒 *Booked On:* ${currentBookingTime}\n\n` +
      `🌎 *Region:* ${region}\n` +
      `👤 *Customer:* ${name}\n` +
      `📞 *Phone:* ${phone}\n` +
      `🚗 *Taxi:* ${taxi}\n\n` +
      `📍 *Pickup:* ${pickup}\n` +
      `🏁 *Drop:* ${drop}\n` +
      `📅 *Date:* ${date}\n` +
      `⏰ *Time:* ${time}\n` +
      `--------------------------\n` +
      `Email: puducherrytaxi@gmail.com\n` +
      `_Pondicherry Taxi Services_`;

    // Send to Server (Background)
    fetch(`${BACKEND_URL}/api/book`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            region, name, phone, pickup, drop, date, time, taxi
        })
    }).catch(err => console.error("Server logging failed", err));

    // Open WhatsApp with encoded message
    window.open(
      `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(messageText)}`,
      "_blank"
    );

    // Open Google Form
    const googleFormLink = "https://docs.google.com/forms/d/e/1FAIpQLSeSF_EdTQtsqORHGqP3J2OR38HmQpv1znudCG3yqeJcuzDkyQ/viewform?";
    window.open(googleFormLink, "_blank");
  });
