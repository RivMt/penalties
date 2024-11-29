import pyautogui

import src.audio as audio


def penalty_AltF4(angry_score):
    if angry_score >= 1500:
        pyautogui.hotkey('alt', 'f4')


async def penalty_sound(angry_score):
    if angry_score >= 1000:
        await audio.play_alert()
        audio.stop()