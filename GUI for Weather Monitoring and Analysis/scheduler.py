import time
from fetch_weather import fetch_weather
from transform import transform_weather
from db import connect_db

def save_weather():
    raw = fetch_weather()
    df = transform_weather(raw)

    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO weather_raw (city, timestamp, data) VALUES (%s, %s, %s)", 
                    (raw["city"], raw["timestamp"], raw["data"]))
        for _, row in df.iterrows():
            cur.execute("""
                INSERT INTO weather_cleaned (city, timestamp, temp_c, humidity, wind_speed, temp_deviation)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, tuple(row))
        conn.commit()
