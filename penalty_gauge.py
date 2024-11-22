import tkinter as tk
from tkinter import ttk
import time
import random

def penalty_gauge(angry_score, angry_score_before):
    

    gauge = angry_score_before

    if angry_score >= 500:
        window = tk.Tk()
        window.title("Progress Bar Example")
        window.geometry("300x100")
        window.attributes('-topmost', True)

        progress_var = tk.IntVar()

        progress_bar = ttk.Progressbar(window, orient="horizontal", length=1500, mode="determinate", variable=progress_var)
        progress_bar.pack(pady=20)
        
        if gauge <= angry_score:
            while gauge <= angry_score and gauge <= 1500:  # プログレスバーの上限を1500に設定
                progress_var.set(int(gauge))
                gauge += 1
                window.update_idletasks()
                time.sleep(0.05)
            gauge = angry_score

        if gauge > angry_score:
            while gauge >= angry_score and gauge >= 500:  # プログレスバーの下限を500に設定
                progress_var.set(int(gauge))
                gauge -= 1
                window.update_idletasks()
                time.sleep(0.05)
            gauge = angry_score

        print("angry_score is ",angry_score,)
    