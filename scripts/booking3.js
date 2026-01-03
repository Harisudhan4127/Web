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

    // Open WhatsApp with encoded message
    window.open(
      `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(messageText)}`,
      "_blank"
    );
  });
