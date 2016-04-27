import pygame, sys
from pygame.locals import*

#constants
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 40
ROCK_IN_SIZE = 10
ROCK_MAX_SIZE = 40
ROCK_MIN_SPEED = 1
ROCK_MAX_SPEED = 8
ADD_NEW_ROCK_RATE = 6
PLAYER_MOVE_RATE = 5

def terminate():
    pygame.quit()
    sys.exit()


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, (255, 255, 255))
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption("WATCHOUT!")
pygame.mixer.music.load('massAppeal.mp3')
font = pygame.font.SysFont(None, 48)

pygame.mouse.set_visible(False)

while True:
    enemies = []


    font.render("Welcome to the show", 1, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
    pygame.display.update()

    break
