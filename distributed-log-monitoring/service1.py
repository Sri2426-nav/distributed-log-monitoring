import requests
import random
import time

SERVICE_NAME = "LoginService"

log_levels = ['INFO', 'WARNING', 'ERROR']
messages = [
    "User logged in",
    "Invalid password attempt",
    "Database timeout",
    "Server not responding",
    "Successful logout",
    "User session expired"
]

while True:
    log = {
        "service": SERVICE_NAME,
        "level": random.choice(log_levels),
        "message": random.choice(messages)
    }

    try:
        response = requests.post("http://127.0.0.1:5000/log", json=log)
        print(f"Sent log: {log} | Status: {response.status_code}")
    except Exception as e:
        print("Failed to send log:", e)

    time.sleep(2)  # Wait 2 seconds before sending next log
