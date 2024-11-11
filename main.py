import pyautogui
import time
import pygame



pygame.init()

# ミキサーを初期化
pygame.mixer.init()

# 音声ファイルのロードと再生
pygame.mixer.music.load('Warning-Siren05-01(Fast-Mid).mp3')
pygame.mixer.music.play()

# 音が鳴っている間、プログラムが終了しないように待機
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)

#音を停止
#pygame.mixer.music.stop()

# time.sleep(3)

# pyautogui.hotkey('alt', 'f4')