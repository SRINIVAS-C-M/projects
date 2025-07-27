import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from db import connect_db
from scheduler import save_weather

def get_cleaned_data():
    with connect_db() as conn:
        df = pd.read_sql("SELECT * FROM weather_cleaned ORDER BY timestamp DESC LIMIT 7", conn)
    return df

def refresh_data():
    save_weather()
    messagebox.showinfo("Success", "Data fetched and saved.")

def plot_graph(frame):
    df = get_cleaned_data()
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(df["timestamp"], df["temp_c"], marker="o")
    ax.set_title("Temperature Trend (°C)")
    ax.set_ylabel("Temp (°C)")
    ax.set_xlabel("Date")
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def run_gui():
    root = tk.Tk()
    root.title("Weather Collector")

    tk.Label(root, text="Weather Dashboard", font=("Arial", 16)).pack(pady=10)

    btn = tk.Button(root, text="Fetch & Save Now", command=refresh_data)
    btn.pack(pady=5)

    frame = tk.Frame(root)
    frame.pack(pady=10)

    plot_graph(frame)

    root.mainloop()
