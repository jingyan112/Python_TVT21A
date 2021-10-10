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

#osa13-6
"""
Make the robot keep moving around all the boundries
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
        y = 480 - robo.get_height()
        x += nopeus
        if nopeus > 0 and x+robo.get_width() >= 640:
            nopeus = -nopeus
        if nopeus < 0 and x <= 0:
            nopeus = -nopeus
    if nopeus < 0 and y <= 0:
        y = 0
        x += nopeus
        if nopeus > 0 and x + robo.get_width() >= 640:
            nopeus = -nopeus
        if nopeus < 0 and x <= 0:
            nopeus = -nopeus

    kello.tick(60)

#osa13-7
"""
Make two robotes keep moving left and right, once it reaches the boundry, chgange the direction
The moving speed of the second robot is twice of the first robot
"""
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

x1 = 0
x2 = 0
y1 = robo.get_width()*2
y2 = robo.get_width()*4
nopeus1 = 1
nopeus2 = 2
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x1, y1))
    naytto.blit(robo, (x2, y2))
    pygame.display.flip()
    
    x1 += nopeus1
    if nopeus1 > 0 and x1 + robo.get_width() >= 640:
        nopeus1 = -nopeus1
    if nopeus1 < 0 and x1 <= 0:
        nopeus1 = -nopeus1

    x2 += nopeus2
    if nopeus2 > 0 and x2 + robo.get_width() >= 640:
        nopeus2 = -nopeus2
    if nopeus2 < 0 and x2 <= 0:
        nopeus2 = -nopeus2

    kello.tick(60)
