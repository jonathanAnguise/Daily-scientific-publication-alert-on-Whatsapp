import requests
import os
from dotenv import load_dotenv
project_folder = os.path.expanduser('.')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

# Handle communication with API of Whatsapp
TOKEN_CALLMEBOT = os.getenv("TOKEN_CALLMEBOT")
ENDPOINT_CALLMEBOT = os.getenv("ENDPOINT_CALLMEBOT")
PHONE_NUMBER = int(os.getenv("PHONE_NUMBER"))

class WhatsAppManager:

    @staticmethod
    def send_whatsapp_message(articles):
        text_to_send = articles
        parameters = {
            "phone": PHONE_NUMBER,
            "text": text_to_send,
            "apikey": TOKEN_CALLMEBOT
        }
        message = requests.post(url=ENDPOINT_CALLMEBOT, params=parameters)
        message.raise_for_status()
        print(message.text)



