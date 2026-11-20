import logging
import requests
from datetime import datetime, timezone
from config import WEBHOOK_URL

def send_notification(event, name, url):

    payload = {
        "event": event,
        "website": name,
        "url": url,
        "status": "DOWN" if event == "website_down" else "UP",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "message": (
            "Website failed two consecutive checks"
            if event == "website_down"
            else "Website is back online"
        )
    }

    try:
        response = requests.post(
            WEBHOOK_URL,
            json=payload,
            timeout=10
        )

        response.raise_for_status()
        logging.info(f"Webhook sent successfully: {event} - {name}")

        

    except requests.RequestException as error:
        logging.error(f"Webhook failed: {error}")

        