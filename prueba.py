import pygame
from pygame.locals import *
color= pygame.Color(0,140,60)
pygame.init()
venta = pygame.display.set_mode((800,600))
pygame.display.set_caption("Hola profesor")

while True:
    venta.fill(color)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()