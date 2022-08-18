import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Projeto Individual Python Game')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela,(100,50,192),(40,40,100,5))
    pygame.draw.circle(tela,(255,255,255),(250,250),40)
    pygame.display.update()
