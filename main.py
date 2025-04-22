from collections import defaultdict

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
    rhythms = []
    amplitudes = []
    with open(file_path, 'r') as file:
        for line in file:
            amplitude, rhythm = line.split()
            amplitudes.append(int(amplitude))
            rhythms.append(int(rhythm))
    # print(f"First 20 Indices of {signal} Signal : {indices[:20]}")
    # print(f"First 20 Values {signal} Signal : {amplitudes[:20]}")
    return amplitudes


def plot_signal(x, y, subplots):
    plt.figure(figsize=(10, 6))
    for i in range(len(subplots)):
        plt.subplot(subplots[i])
        plt.plot(x[i][:400], y[i][:400])
        plt.xlabel("Index")
        plt.ylabel("Amplitudes")

    plt.show()


def create_indices(signal_amplitudes):
    signal_indices = np.arange(0, len(signal_amplitudes))
    return list(signal_indices)


def bandpass_filter(data, low_cutoff=1, high_cutoff=40, sampling_rate=250, order=2):
    nyq = 0.5 * sampling_rate
    low = low_cutoff / nyq
    high = high_cutoff / nyq
    b, a = butter(order, [low, high], btype='band', analog=False, fs=None)
    filtered_data = filtfilt(b, a, data)
    return filtered_data


def apply_bandpass(signal):
    signal_amplitudes = read_signal(signal)
    signal_indices = create_indices(signal_amplitudes)
    print(f"Indices : {signal_indices[:10]}\nN : {len(signal_indices)}")
    print(f"Amplitudes : {signal_amplitudes[:10]}\nN : {len(signal_amplitudes)}")
    filtered_signal = bandpass_filter(signal_amplitudes)
    print(f"Filtered signal : {filtered_signal[:10]}\nN = : {len(filtered_signal)}")
    plot_signal([signal_indices, signal_indices], [signal_amplitudes, filtered_signal], [121, 122])




ali_signal_button = ttk.Button(root, text="Read Ali Signal", command=lambda: apply_bandpass("Ali"))
ali_signal_button.pack(padx=10, pady=5)

mohamed_signal_button = ttk.Button(root, text="Read Mohamed Signal", command=lambda: apply_bandpass("Mohamed"))
mohamed_signal_button.pack(padx=10, pady=5)

root.mainloop()
