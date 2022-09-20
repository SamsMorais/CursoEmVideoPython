import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('ex021Aula08.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()
input()
pygame.event.wait()
