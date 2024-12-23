import pygame

# time.sleep(3)
# pyautogui.hotkey('alt', 'f4')

pygame.init()

# ミキサーを初期化
pygame.mixer.init()
sound_alert = pygame.mixer.Sound("./res/alert.mp3")
sound_relax = pygame.mixer.Sound("./res/relax.mp3")
channel_alert = pygame.mixer.Channel(0)
channel_relax = pygame.mixer.Channel(1)

async def play_alert():
    if not channel_alert.get_busy():
        channel_alert.play(sound_alert)

async def play_relax():
    if not channel_relax.get_busy():
        channel_relax.play(sound_relax)

async def display_black():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.fill((0, 0, 0))  # RGB(0, 0, 0) は黒色
    pygame.display.flip()

async def display_restore():
    pygame.display.quit()
    
def stop():
    channel_alert.stop()
    channel_relax.stop()