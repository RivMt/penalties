import tkinter as tk
from tkinter import ttk
import time
import random


# ウィンドウの作成
window = tk.Tk()
window.title("Progress Bar Example")
window.geometry("300x100")

# 進行状況を追跡するための変数を設定
progress_var = tk.IntVar()

# プログレスバーの設定
progress_bar = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate", variable=progress_var)
progress_bar.pack(pady=20)

# グローバル変数の初期化
angry_point = 50  # 任意の初期値
gauge = 0  # 初期値は0とする

# 関数の定義
def update_progress():
    global gauge, angry_point  # グローバル変数を参照

    while True:
        # `gauge` が `angry_point` より小さい場合、上昇させる
        if gauge <= angry_point:
            while gauge <= angry_point and gauge <= 100:  # プログレスバーの上限を100に設定
                progress_var.set(int(gauge))
                gauge += 1
                window.update_idletasks()
                time.sleep(0.05)
            gauge = angry_point  # 値を固定

        # `gauge` が `angry_point` より大きい場合、減少させる
        if gauge > angry_point:
            while gauge >= angry_point and gauge >= 0:  # プログレスバーの下限を0に設定
                progress_var.set(int(gauge))
                gauge -= 1
                window.update_idletasks()
                time.sleep(0.05)
            gauge = angry_point  # 値を固定
        random_int = random.randint(-20, 20)
        angry_point += random_int
        print("怒りポイントは",angry_point,"です")
# ウィンドウを表示した後に自動で関数を呼び出す
window.after(100, update_progress)  # 100ミリ秒後に update_progress を実行

# メインループの開始
window.mainloop()
