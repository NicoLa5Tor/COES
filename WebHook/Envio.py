import requests
import json

ACCESS_TOKEN = "TU_ACCESS_TOKEN"  
PHONE_NUMBER_ID = "TU_PHONE_NUMBER_ID" 
RECIPIENT_WAID = "521XXXXXXXXXX"

url = f"https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}/messages"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

data = {
    "messaging_product": "whatsapp",
    "to": RECIPIENT_WAID,
    "type": "text",
    "text": {
        "body": "Hola! Este es un mensaje de prueba desde mi webhook en Flask 🚀"
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print("Respuesta de WhatsApp:", response.text)
