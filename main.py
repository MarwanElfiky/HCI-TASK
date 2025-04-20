import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from scipy.signal import butter, filtfilt

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
    # print(f"First 20 Indices of {signal} Signal : {indices[:20]}")
    # print(f"First 20 Values {signal} Signal : {amplitudes[:20]}")
    return indices, amplitudes


def plot_signal(signal_indices, signal_values):
    plt.plot(signal_indices[:100], signal_values[:100])
    plt.xlabel("Index")
    plt.ylabel("Amplitudes")
    plt.show()


def bandpass_filter(data, low_cutoff=1, high_cutoff=40, sampling_rate=250, order=2):
    nyq = 0.5 * sampling_rate
    low = low_cutoff / nyq
    high = high_cutoff / nyq
    b, a = butter(order, [low, high], btype='band', analog=False, fs=None)
    filtered_data = filtfilt(b, a, data)
    return filtered_data


def apply_bandpass(signal):
    signal_indices, signal_values = read_signal(signal)
    filtered_signal = bandpass_filter(signal_values)
    plot_signal(signal_indices, filtered_signal)
    return signal_indices, filtered_signal


ali_signal_button = ttk.Button(root, text="Read Ali Signal", command=lambda: apply_bandpass("Ali"))
ali_signal_button.pack(padx=10, pady=5)

mohamed_signal_button = ttk.Button(root, text="Read Mohamed Signal", command=lambda: apply_bandpass("Mohamed"))
mohamed_signal_button.pack(padx=10, pady=5)

root.mainloop()
