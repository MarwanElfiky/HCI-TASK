import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

root = tk.Tk()
root.title("Task HCI")
root.geometry("400x400")


def read_signal(signal):
    file_path = filedialog.askopenfilename(title=f"Choose Signal {signal}")
    indices = []
    amplitudes = []
    with open(file_path, 'r') as file:
        for line in file:
            index, amplitude = line.split()
            indices.append(int(index))
            amplitudes.append(int(amplitude))
    print(f"First 20 Indices : {indices[:20]}")
    print(f"First 20 Values : {amplitudes[:20]}")
    return indices, amplitudes


ali_signal = ttk.Button(root, text="Read Ali Signal", command=lambda: read_signal("Ali"))
ali_signal.pack(padx=10, pady=5)

mohamed_signal = ttk.Button(root, text="Read Mohamed Signal", command=lambda: read_signal("Mohamed"))
mohamed_signal.pack(padx=10, pady=5)

root.mainloop()
