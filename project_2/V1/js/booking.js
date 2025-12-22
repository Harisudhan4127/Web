function sendBooking(event) {
  event.preventDefault(); // stop form submit

  // Get input values
  const pickup = document.getElementById("pickup").value;
  const drop = document.getElementById("drop").value;
  const date = document.getElementById("date").value;
  const phone = document.getElementById("phone").value;

  // ===== WHATSAPP SETTINGS =====
  const whatsappNumber = "919344040002"; // change to your number

  const message =
    "Pondicherry Taxi Booking\n" +
    "Pickup: " + pickup + "\n" +
    "Drop: " + drop + "\n" +
    "Date: " + date + "\n" +
    "Mobile: " + phone;

  const whatsappURL =
    "https://wa.me/" +
    whatsappNumber +
    "?text=" +
    encodeURIComponent(message);

  window.open(whatsappURL, "_blank");

  // ===== GOOGLE FORM AUTO-FILL =====
  const googleFormURL =
    "https://docs.google.com/forms/d/e/1FAIpQLSeSF_EdTQtsqORHGqP3J2OR38HmQpv1znudCG3yqeJcuzDkyQ/viewform?" +
    "entry.111111111=" + encodeURIComponent(pickup) +
    "&entry.222222222=" + encodeURIComponent(drop) +
    "&entry.333333333=" + encodeURIComponent(date) +
    "&entry.444444444=" + encodeURIComponent(phone);

  window.open(googleFormURL, "_blank");
}
