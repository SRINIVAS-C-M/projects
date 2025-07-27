import requests
from datetime import datetime
from config import API_KEY, CITY

def fetch_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return {
        "city": CITY,
        "timestamp": datetime.utcnow(),
        "data": data
    }
