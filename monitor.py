import requests

def check_website(name, url):

    try:
        response = requests.get(url, timeout=10)

        if 200 <= response.status_code < 400:
            return "UP"

        return "DOWN"

    except requests.RequestException:
        return "DOWN"