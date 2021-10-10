#osa13-1
"""
Draw four robots distributed among the four corners
"""
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
leveys = robo.get_width()
korkeus = robo.get_height()

naytto.fill((0, 0, 0))
naytto.blit(robo, (0, 0))
naytto.blit(robo, (0, 480 - korkeus))
naytto.blit(robo, (640 - leveys, 0))
naytto.blit(robo, (640 - leveys, 480 - korkeus))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

#osa13-2
"""
Draw 10 robots in the second row and in the middle of the whole window
"""
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
leveys = robo.get_width()
korkeus = robo.get_height()

naytto.fill((0, 0, 0))
for i in range(0, 10):
    naytto.blit(robo, ((640 - leveys*10)/2 + leveys*i, korkeus))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()