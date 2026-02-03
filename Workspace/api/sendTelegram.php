<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json");

$botToken = "7797155729:AAE2XbAvFicbL8ACNX0hYdgpYB1tiIBukBU";
$chatId   = "7522813568"; // your chat ID

$data = json_decode(file_get_contents("php://input"), true);

if (!$data) {
    http_response_code(400);
    echo json_encode(["error" => "No input"]);
    exit;
}

$message = "Pondicherry Taxi Booking\n";
$message .= "Pickup: {$data['pickup']}\n";
$message .= "Drop: {$data['drop']}\n";
$message .= "Date: {$data['date']}\n";
$message .= "Mobile: {$data['phone']}";

$url = "https://api.telegram.org/bot$botToken/sendMessage";
// https://api.telegram.org/bot7797155729:AAE2XbAvFicbL8ACNX0hYdgpYB1tiIBukBU/sendMessage?chat_id=7522813568&text
$ch = curl_init($url);
curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => ["Content-Type: application/json"],
    CURLOPT_POSTFIELDS => json_encode([
        "chat_id" => $chatId,
        "text" => $message
    ])
]);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
