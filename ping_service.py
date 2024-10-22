import time
import requests

# URL of the API to ping
url = "https://calc1-6nke.onrender.com/subtasks"

def ping_api():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successfully pinged {url}")
        else:
            print(f"Failed to ping {url}: Status code {response.status_code}")
    except Exception as e:
        print(f"Error pinging {url}: {e}")

if __name__ == "__main__":
    while True:
        ping_api()
        time.sleep(1200)  # Ping every 20 minutes (1200 seconds)
