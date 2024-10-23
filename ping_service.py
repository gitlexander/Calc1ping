from flask import Flask
import time
import threading
import requests

# Set up a Flask web server to bind to a port
app = Flask(__name__)

# URL of the API to ping
url = "https://calc1-6nke.onrender.com/subtasks"

def ping_api():
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Successfully pinged {url}")
            else:
                print(f"Failed to ping {url}: Status code {response.status_code}")
        except Exception as e:
            print(f"Error pinging {url}: {e}")
        time.sleep(1200)  # Ping every 20 minutes

# Start pinging in a background thread
def start_pinging():
    ping_thread = threading.Thread(target=ping_api)
    ping_thread.start()

# Define a simple route to satisfy the web server requirement
@app.route('/')
def home():
    return "Ping service is running!"

if __name__ == '__main__':
    # Start the pinging service
    start_pinging()
    # Run the Flask web server on the required port
    app.run(host='0.0.0.0', port=8000)
