import time
import requests
from datetime import datetime

# URL dan jadwal pemanggilan
SCHEDULES = [
    {"url": "http://192.168.13.160:8000/notifMemowhatsapp", "hour": 9, "minute": 10},
    {"url": "http://192.168.13.160:8000/newprogressreports/whatsappsend", "hour": 16, "minute": 59}
]

def run_scheduler(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[{datetime.now()}] Successfully triggered: {url}")
        else:
            print(f"[{datetime.now()}] Failed to trigger: {url}. Status: {response.status_code}")
    except Exception as e:
        print(f"[{datetime.now()}] Error triggering {url}: {str(e)}")

def main():
    while True:
        now = datetime.now()
        for schedule in SCHEDULES:
            if now.hour == schedule["hour"] and now.minute == schedule["minute"]:
                run_scheduler(schedule["url"])
                time.sleep(60)  # Cegah pemanggilan ulang di menit yang sama
        time.sleep(30)  # Cek setiap 30 detik

if __name__ == "__main__":
    main()
