'''Tocar música no python com o pygame'''
import pygame
pygame.init()
pygame.mixer.music.load(r'C:\Users\Hector SIlva\Desktop\ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

'''Por algum moivo o pycharm n está reconhecendo '''