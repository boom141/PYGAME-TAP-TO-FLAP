import pygame, os, sys, time
from pygame.locals import*
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

RESOLUTION = (500,500)

FPS = 60

window = pygame.display.set_mode(RESOLUTION)

display = pygame.Surface((300,300))

pygame.display.set_caption('Pygame: Tap To Flap')

clock = pygame.time.Clock()

