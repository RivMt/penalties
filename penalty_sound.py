import time
import pygame

def penalty_sound(angry_score):
    if (angry_score >= 1000):
        pygame.mixer.music.load('relax.mp3')
        pygame.mixer.music.play()
        time.sleep(30)