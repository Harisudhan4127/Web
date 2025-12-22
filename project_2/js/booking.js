function sendBooking(event) {
  event.preventDefault();

  const pickup = document.getElementById("pickup").value;
  const drop = document.getElementById("drop").value;
  const date = document.getElementById("date").value;
  const phone = document.getElementById("phone").value;

  fetch("api/sendTelegram.php", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      pickup,
      drop,
      date,
      phone
    })
  })
  .catch(() => {}); // silently ignore errors

  // Redirect user (MAIN FLOW)
  const googleFormURL =
    "https://docs.google.com/forms/d/e/1FAIpQLSeSF_EdTQtsqORHGqP3J2OR38HmQpv1znudCG3yqeJcuzDkyQ/viewform?" +
    "entry.111111111=" + encodeURIComponent(pickup) +
    "&entry.222222222=" + encodeURIComponent(drop) +
    "&entry.333333333=" + encodeURIComponent(date) +
    "&entry.444444444=" + encodeURIComponent(phone);

  window.location.href = googleFormURL;
}
