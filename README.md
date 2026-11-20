# Website Monitor – How to Run

## Requirements
- Python 3.8+
- Internet connection

## 1. Open the project folder

```bash
cd Website-Monitor
```

## 2. Create a virtual environment

```bash
python -m venv venv
```

## 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure Webhook

Open `config.py` and add your Webhook.site URL:

```python
WEBHOOK_URL = "YOUR_WEBHOOK_URL"
```

## 6. Start the test server

Open the first terminal:

```bash
python test.py
```

Keep it running.

## 7. Start the website monitor

Open a second terminal:

```bash
python main.py
```

The application will continuously monitor the configured websites every 5 minutes.

## 8. Test DOWN and UP

While the application is running, open these URLs in your browser:

- Set website DOWN: http://127.0.0.1:8000/set/down
- Set website UP: http://127.0.0.1:8000/set/up

The monitor will detect the failure and recovery automatically.

## 9. View logs

Check `website_monitor.log` in the project folder.

Webhook notifications can be viewed on your Webhook.site dashboard.

## 10. Stop the application

Press `Ctrl + C` in the monitoring terminal.