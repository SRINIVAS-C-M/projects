import psycopg2
from config import POSTGRES

def connect_db():
    return psycopg2.connect(**POSTGRES)

def create_tables():
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS weather_raw (
            id SERIAL PRIMARY KEY,
            city TEXT,
            timestamp TIMESTAMP,
            data JSONB
        );
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS weather_cleaned (
            id SERIAL PRIMARY KEY,
            city TEXT,
            timestamp TIMESTAMP,
            temp_c FLOAT,
            humidity INT,
            wind_speed FLOAT,
            temp_deviation FLOAT
        );
        """)
        conn.commit()
