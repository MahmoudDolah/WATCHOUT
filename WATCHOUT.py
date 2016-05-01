import pygame
import sys
from pygame.locals import*

# Constants
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


def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    terminate()
                return


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, (255, 255, 255))
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def playerHitEnemy(playerRect, enemies):
    for enemy in enemies:
        if playerRect.colliderect(enemy['rect']):
            return True
    return False

# Game Initialization
pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption("WATCHOUT!")
pygame.mouse.set_visible(False)


# Sounds
pygame.mixer.music.load('massAppeal.mp3')
gameOver = pygame.mixer.Sound('massAppeal.mp3')

# Font
font = pygame.font.SysFont(None, 48)
DISPLAYSURF.fill(BACKGROUND_COLOR)

# Set up images
playerRect = playerImage.get_rect()

# Start Screen
drawText('WATCHOUT!!!', font, DISPLAYSURF, (WINDOW_WIDTH / 3), (WINDOW_HEIGHT / 3))
drawText('Press any key to start.', font, DISPLAYSURF, (WINDOW_WIDTH / 3) - 30, (WINDOW_HEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()

while True:
    enemies = []
    playerRect.topleft = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False

    enemyAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    font.render("Welcome to the show", 1, (255, 255, 255))
    while True:
    # While game is being played, this loop runs
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        pygame.display.update()

        break
