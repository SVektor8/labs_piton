from operator import index

import pygame
from pygame.draw import *


def sector(x_center, y_center, radius):
    '''
    Draws a 90-degree circle sector
    (in the third cootdinats' quarter)
    x_center - x-coordinate of the producting circle center
    y_center - y-coordinate of the producting circle center
    radius - radius of the producting circle 
    '''
    
    coords = []
    
    for kx in range(x_center - radius, x_center):
        y = y_center + (radius ** 2 - (kx - x_center) ** 2) ** (1 / 2)
        coords.append((kx, y))
    coords.append((x_center, y_center))
    
    polygon(screen, colours[8], coords, 0)

def cloud(screen, coordinats, radius):
    '''
    Draws a group of circles
    screen - surface, where the group will be placedd
    coordinats - a list of pairs like (x, y) where x and y are x- abnd y- coordinats of each circle
    '''
    
    for i in coordinats:
        circle(screen, colours[0], i, radius, 0)
        circle(screen, colours[1], i, radius, 1)

def ship(x, y):
    '''
    Draws a ship
    x, y are x- and y- coordinats of the left top point of the mast
    '''
    
    sector(x - 58, y + 95, 30)  # backside
    polygon(screen, (255, 153, 0), [(x - 58, y + 95), (x + 149, y + 95), (x + 85, y + 125), (x - 58, y + 125)], 0)   # board
    
    circle(screen, colours[0], (x + 99, y + 106), 7, 0)  # window
    circle(screen, colours[5], (x + 99, y + 106), 7, 2)  
    
    polygon(screen, colours[5], [(x - 5, y + 96), (x, y + 96), (x, y), (x - 5, y)], 0)  # mast
    
    polygon(screen, colours[6], [(x + 57, y + 47), (x + 17, y + 47), (x, y), (x + 57, y + 47), (x, y + 96), (x + 17, y + 47)], 0)  # sail
    polygon(screen, colours[5], [(x + 57, y + 47), (x + 17, y + 47), (x, y), (x + 57, y + 47), (x, y + 96), (x + 17, y + 47)], 1)

def umbrella(x, y): #96 383
    '''
    Draws an umbrella
    x, y are x- and y- coordinats of the right bottom point
    '''

    polygon(screen, colours[8], [(x - 6, y - 150), (x, y - 150), (x, y), (x - 6, y)], 0)  # umbrella
    polygon(screen, colours[9], [(x - 6, y - 150), (x - 70, y - 120), (x + 66, y - 120), (x, y - 150)], 0)
    
    umbrella_left = [26, 41, 61, 80, 90]  # lines on the umbrella
    umbrella_right = [96, 108, 127, 147, 162]
    
    for dot in umbrella_left:
        polygon(screen, (55, 55, 55), [(x - 6, y - 150), (x - 96 + dot, y - 120), (x - 6, y - 150)], 1)
    for dot in umbrella_right:
        polygon(screen, (55, 55, 55), [(x, y - 150), (x - 96 + dot, y - 120), (x, y - 150)], 1)
  


colours = [
    (255, 255, 255),  # 0 white
    ( 55,  55,  55),  # 1 dark gray
    ( 76, 241, 252),  # 2 light blue
    ( 31,  94, 255),  # 3 dark blue
    (255, 231,  18),  # 4 yellow
    (  0,   0,   0),  # 5 black
    (200, 200, 200),  # 6 light gray
    (255, 153,   0),  # 7 orange
    (224, 161,   0),  # 8 bitter orange
    (255,   0, 170)  # 9 pink
           ]
FPS = 30
screen = pygame.display.set_mode((600, 400))

pygame.init()


rect(screen, colours[2], (0, 0, 700, 180), 0)  #beach
rect(screen, colours[3], (0, 180, 700, 100), 0)
rect(screen, colours[4], (0, 280, 700, 120), 0)

circle(screen, colours[4], (535, 55), 35, 0)  #sun

for i in range(14):  # waves on the beach
    circle(screen, colours[3 + int((-1) ** i == -1)], ((25 + 50 * i), (280 - (-1) ** i * 25)), 35, 0)
        

cloud_0 = [(132, 47), (120, 60), (151, 49), (139, 63), (160, 62), (170, 50), (177, 63)]  # clouds
cloud(screen, cloud_0, 12)

cloud_1 = [(i[0] - 40, i[1] + 60) for i in cloud_0]
cloud(screen, cloud_1, 15)

cloud_2 = [(i[0] + 140, i[1] + 40) for i in cloud_0]
cloud(screen, cloud_2, 11)


umbrella(96, 383)

ship(410, 110)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
