import pandas as pd
import numpy as np

def transform_weather(raw_record):
    main = raw_record["data"]["main"]
    wind = raw_record["data"]["wind"]
    temp_k = main["temp"]
    temp_c = temp_k - 273.15
    humidity = main["humidity"]
    wind_speed = wind.get("speed", 0)

    df = pd.DataFrame([{
        "city": raw_record["city"],
        "timestamp": raw_record["timestamp"],
        "temp_c": temp_c,
        "humidity": humidity,
        "wind_speed": wind_speed
    }])
    df["temp_deviation"] = df["temp_c"] - df["temp_c"].mean()
    return df
