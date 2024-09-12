import pygame
import os

pygame.init()

mp3_path = 'C:/Users/FELIPE/Desktop/python study/ex17.mp3'

if not os.path.isfile(mp3_path):
    print("File does not exist:", mp3_path)
else:
    pygame.mixer.music.load(mp3_path)
    pygame.mixer.music.play()
    input("Press Enter to stop the music and exit...")
    pygame.quit()