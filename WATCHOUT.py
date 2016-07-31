import pygame
import sys
from pygame.locals import*

# Constants
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 700
TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 40
ROCK_IN_SIZE = 10
ROCK_MAX_SIZE = 40
ROCK_MIN_SPEED = 1
ROCK_MAX_SPEED = 7
ADD_NEW_ROCK_RATE = 5
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
theClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption("WATCHOUT!")
pygame.mouse.set_visible(False)

# Sounds
pygame.mixer.music.load('itAintHardToTell.mp3')
#gameOver = pygame.mixer.Sound('itAintHardToTell.mp3')

# Font
font = pygame.font.SysFont(None, 48)
DISPLAYSURF.fill(BACKGROUND_COLOR)

# Set up images
playerImage = pygame.image.load('kendrickFace.jpg')
playerRect = playerImage.get_rect()

# Start Screen
drawText('WATCHOUT!!!', font, DISPLAYSURF, (WINDOW_WIDTH / 3), (WINDOW_HEIGHT / 3))
drawText('Press any key to start.', font, DISPLAYSURF, (WINDOW_WIDTH / 3) - 30, (WINDOW_HEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()

topScore = 0
while True:
    score = 0
    enemies = []
    playerRect.topleft = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False

    enemyAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    font.render("Welcome to the show", 1, (255, 255, 255))
    while True:
    # While game is being played, this loop runs
        score += 1 #increase score every second

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == ord('z'):
                    reverseCheat = True
                if event.key == ord('x'):
                    slowCheat = True
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == ord('z'):
                    reverseCheat = False
                    score = 0
                if event.key == ord('x'):
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False

            if event.type == MOUSEMOTION:
                # If the mouse moves, move the player where the cursor is.
                playerRect.move_ip(event.pos[0] - playerRect.centerx, event.pos[1] - playerRect.centery)

        if not reverseCheat and not slowCheat:
            enemyAddCounter += 1

        if enemyAddCounter == ADD_NEW_ROCK_RATE:
            enemyAddCounter = 0
            enemySize = random.randint(ROCK_IN_SIZE, ROCK_MAX_SIZE)
            newEnemy = {'rect':pygame.Rect(random.randint(0, WINDOW_WIDTH-enemySize), 0 - enemySize, enemySize, enemySize),
            'speed':random.randint(ROCK_MIN_SPEED, ROCK_MAX_SPEED),
            'surface':pygame.transform.scale(enemyImage, (enemySize, enemySize)),
            }
        enemies.append(newEnemy)

        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1*PLAYER_MOVE_RATE, 0)

        pygame.display.update()

        break
