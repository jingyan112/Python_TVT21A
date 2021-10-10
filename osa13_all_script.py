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

#osa13-3
"""
Draw 10*10 robots in the whole window with overlapping
"""
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
leveys = robo.get_width()
korkeus = robo.get_height()

naytto.fill((0, 0, 0))
for row in range(1, 11):
    for row1 in range(0, 10):
        naytto.blit(robo, ((640 - leveys*10)/2 + leveys*row1 + row*6, korkeus + row*6))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

#osa13-4
"""
Draw 1000 robots randomly distributing in thge whole window
"""
import random
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
leveys = robo.get_width()
korkeus = robo.get_height()

naytto.fill((0, 0, 0))
for i in range(0, 1000):
    coordinate = (random.randint(0, 640 - leveys), random.randint(0, 480 - korkeus))
    naytto.blit(robo, (coordinate[0], coordinate[1]))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

#osa13-5
"""
Make the robot keep moving up and down, once it reaches the boundry, chgange the direction
"""
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

x = 0
y = 0
nopeus = 1
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y))
    pygame.display.flip()

    y += nopeus
    if nopeus > 0 and y + robo.get_height() >= 480:
        nopeus = -nopeus
    if nopeus < 0 and y <= 0:
        nopeus = -nopeus

    kello.tick(60)