import os
import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd
import mplfinance as mpf

class ChartingGUI:
    def __init__(self, master):
        self.master = master
        master.title("Charting Tool")

        self.file_label = ttk.Label(master, text="Select data file:")
        self.file_label.grid(row=0, column=0, padx=10, pady=10)

        self.file_var = tk.StringVar()
        self.file_dropdown = ttk.Combobox(master, textvariable=self.file_var, state="readonly")
        self.file_dropdown.grid(row=0, column=1, padx=10, pady=10)

        self.plot_button = ttk.Button(master, text="Plot", command=self.plot)
        self.plot_button.grid(row=0, column=2, padx=10, pady=10)

        self.load_files()

    def load_files(self):
        data_path = os.path.join(os.getcwd(), "data")
        if not os.path.exists(data_path):
            os.makedirs(data_path)
        data_files = [f for f in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, f))]
        self.file_dropdown["values"] = data_files

    def plot(self):
        data_path = os.path.join(os.getcwd(), "data")
        selected_file = self.file_var.get()
        file_path = os.path.join(data_path, selected_file)

        try:
            data = pd.read_csv(file_path, header=None, names=["date", "time", "open", "high", "low", "close", "volume"])
            data["time"] = data["time"].astype(str).str.zfill(4)
            datetime_str = data["date"].str.cat(data["time"], sep=" ")
            data.index = pd.to_datetime(datetime_str, format="%d/%m/%Y %H%M")
            last_100_data = data.tail(100)
            mpf.plot(last_100_data, type='candle', volume=True, title=str(selected_file))
        except Exception as e:
            print(f"Error plotting {selected_file}: {e}")

root = tk.Tk()
gui = ChartingGUI(root)
root.mainloop()
