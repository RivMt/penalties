import pyautogui

def penalty_AltF4(angry_score):
    if (angry_score >= 1500):
        pyautogui.hotkey('alt', 'f4')