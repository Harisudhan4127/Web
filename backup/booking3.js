document.getElementById('bookingForm').addEventListener('submit', function(event) {
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
    const currentBookingTime = now.toLocaleDateString() + " | " + now.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});

    const whatsappNumber = "919585641389"; 
    
    // Construct WhatsApp Message
    const message = `*NEW TAXI BOOKING*%0A` +
                    `--------------------------%0A` +
                    `🕒 *Booked On:* ${currentBookingTime}%0A%0A` +
                    `🌎 *Region:* ${region}%0A` +
                    `👤 *Customer:* ${name}%0A` +
                    `📞 *Phone:* ${phone}%0A` +
                    `🚗 *Taxi:* ${taxi}%0A%0A` +
                    `📍 *Pickup:* ${pickup}%0A` +
                    `🏁 *Drop:* ${drop}%0A` +
                    `📅 *Date:* ${date}%0A` +
                    `⏰ *Time:* ${time}%0A` +
                    `--------------------------%0A` +
                    `Email: puducherrytaxi@gmail.com%0A` +
                    `_Pondicherry Taxi Services_`;

    // Open WhatsApp
    window.open(`https://wa.me/${whatsappNumber}?text=${message}`, "_blank");
});