import pygame

file = 'TENGO  (Visualizer) - Juliette.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()