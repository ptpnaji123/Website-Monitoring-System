
import time
import logging

from config import WEBSITES, CHECK_INTERVAL
from monitor import check_website
from notifier import send_notification


# Configure logging
logging.basicConfig(
    filename="website_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Initialize website status
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

        # WEBSITE DOWN
        if current_status == "DOWN":

            data["failures"] += 1

            print(f"{name}: DOWN | Failures: {data['failures']}")

            logging.warning(
                f"{name} is DOWN. Consecutive failures: {data['failures']}"
            )

            # Send DOWN alert after 2 consecutive failures
            if data["failures"] >= 2 and data["status"] != "DOWN":

                data["status"] = "DOWN"

                print(f"ALERT: {name} is DOWN!")

                logging.error(
                    f"{name} failed two consecutive checks"
                )

                send_notification("website_down", name, url)

        # WEBSITE UP
        else:

            print(f"{name}: UP")
            logging.info(f"{name} is UP")

            # Detect recovery from DOWN to UP
            if data["status"] == "DOWN":

                print(f"\n🟢 BACK UP: {name} has recovered!")

                logging.info(
                    f"{name} has recovered and is back UP"
                )

                # Send only one recovery notification
                send_notification("website_recovered", name, url)

            # Reset failure counter and status
            data["failures"] = 0
            data["status"] = "UP"

    print(f"\nNext check in {CHECK_INTERVAL // 60} minutes...")

    time.sleep(CHECK_INTERVAL)
