import time
import logging

from config import WEBSITES, CHECK_INTERVAL
from monitor import check_website
from notifier import send_notification

logging.basicConfig(
    filename="website_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

website_status = {}

for name in WEBSITES:
    website_status[name] = {
        "failures": 0,
        "status": "UP"
    }

print("Website Monitor Started")
logging.info("Website Monitor Started")

while True:

    print("\nChecking websites...\n")

    for name, url in WEBSITES.items():

        current_status = check_website(name, url)
        data = website_status[name]

        if current_status == "DOWN":

            data["failures"] += 1

            print(f"{name}: DOWN | Failures: {data['failures']}")

            logging.warning(
                f"{name} is DOWN. Consecutive failures: {data['failures']}"
            )

            if data["failures"] >= 2 and data["status"] != "DOWN":

                data["status"] = "DOWN"

                logging.error(f"{name} failed two consecutive checks")

                send_notification("website_down", name, url)

        else:

            print(f"{name}: UP")
            logging.info(f"{name} is UP")

            if data["status"] == "DOWN":

                print(f"RECOVERY: {name} is back UP!")

                logging.info(f"{name} has recovered")

                send_notification("website_recovered", name, url)

            data["failures"] = 0
            data["status"] = "UP"

    print("\nNext check in 5 minutes...")

    time.sleep(CHECK_INTERVAL)