import pygame
import socketio
import numpy as np
from gameFuncts import *

# Socketio Stuff

sio = socketio.Client()
@sio.event
def connect():
    print('connection established')


@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5000')

# Set the pygame window size
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1850

# Define opencv frame size

FRAMESIZE = (1280,720)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

BACKGROUND_COLOR = pygame.Color(251, 251, 248)
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
LIGHTGRAY = pygame.Color(139, 146, 153)
DARKGRAY = pygame.Color(42, 43, 43)

# Intialize all relevant variables for the game
running = True

screen.fill(BACKGROUND_COLOR)

# Synchronize to board

@sio.on('updateBoard')
def updateBoard(data):
    global screen
    prevMouse = data['prevCoord']
    mouse = data['currCoord']
    InterpolatePoints(screen, BLACK, prevMouse[0], prevMouse[1], mouse[0], mouse[1], 5)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Flip the display
    pygame.display.flip()