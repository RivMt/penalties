import pygame

# time.sleep(3)
# pyautogui.hotkey('alt', 'f4')

pygame.init()

# ミキサーを初期化
pygame.mixer.init()

async def play_alert():
    pygame.mixer.music.load('./res/alert.mp3')
    pygame.mixer.music.play()
    
def stop():
    pygame.mixer.music.stop()