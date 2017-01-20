import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 800
WINDOWHEIGHT = 800
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 40
FANMINSIZE = 10
FANMAXSIZE = 40
FANMINSPEED = 1
FANMAXSPEED = 8
ADDNEWFANRATE = 6
PLAYERMOVERATE = 5

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

def playerHasHitFan(playerRect, fans):
    for f in fans:
        if playerRect.colliderect(f['rect']):
            return True
    return False

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('WATCHOUT!!!')
pygame.mouse.set_visible(False)

# set up fonts
font = pygame.font.SysFont(None, 48)

# set up sounds
num = random.randint(0, 1)
if num == 0:
    pygame.mixer.music.load('songs/maadCity.mp3')
else:
    pygame.mixer.music.load('songs/alright.mp3')

# set up images
playerImage = pygame.image.load('images/kendrickLamar.png')
playerRect = playerImage.get_rect()
fanImage = pygame.image.load('images/screamingFan.png')

# show the "Start" screen
drawText('WATCHOUT', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()

topScore = 0
while True:
    # set up the start of the game
    fans = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    fanAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # the game loop runs while the game part is playing
        score += 1 # increase score

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

        # Add new fans at the top of the screen, if needed.
        if not reverseCheat and not slowCheat:
            fanAddCounter += 1
        if fanAddCounter == ADDNEWFANRATE:
            fanAddCounter = 0
            fanSize = random.randint(FANMINSIZE, FANMAXSIZE)
            newFan = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-fanSize), 0 - fanSize, fanSize, fanSize),
                        'speed': random.randint(FANMINSPEED, FANMAXSPEED),
                        'surface':pygame.transform.scale(fanImage, (fanSize, fanSize)),
                        }

            fans.append(newFan)

        # Move the player around.
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)

        # Move the mouse cursor to match the player.
        pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)

        # Move the fans down.
        for f in fans:
            if not reverseCheat and not slowCheat:
                f['rect'].move_ip(0, f['speed'])
            elif reverseCheat:
                f['rect'].move_ip(0, -5)
            elif slowCheat:
                f['rect'].move_ip(0, 1)

         # Delete fans that have fallen past the bottom.
        for f in fans[:]:
            if f['rect'].top > WINDOWHEIGHT:
                fans.remove(f)

        # Draw the game world on the window.
        windowSurface.fill(BACKGROUNDCOLOR)

        # Draw the score and top score.
        drawText('Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)

        # Draw the player's rectangle
        windowSurface.blit(playerImage, playerRect)

        # Draw each fan
        for f in fans:
            windowSurface.blit(f['surface'], f['rect'])

        pygame.display.update()

        # Check if any of the fans have hit the player.
        if playerHasHitFan(playerRect, fans):
            if score > topScore:
                topScore = score # set new top score
            break

        mainClock.tick(FPS)

    # Stop the game and show the "Game Over" screen.

    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()
