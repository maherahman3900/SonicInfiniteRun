# Maher Rahman
# Version 1.0
# Created on 24/7/2024

# good spritesheet source: https://www.vg-resource.com/archive/index.php/thread-27627-8.html

import pygame
import math
import random
import button
import spritesheet
import enemy

pygame.init()

clock = pygame.time.Clock()
FPS = 60

# set up display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sonic Infinite Run")

# colours
SPRITEBG = (0,0,0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (252,36,36)
BLUE = (36,140,252)
GREEN = (0, 255, 0)

# fonts
fontSize1 = pygame.font.Font("Fonts/pixelated.ttf", 30)
fontSize2 = pygame.font.Font("Fonts/pixelated.ttf", 40)
fontSize3 = pygame.font.Font("Fonts/pixelated.ttf", 50)

# audio
runningSound = pygame.mixer.Sound("Audio/Sonic Running Sound.mp3")
jumpingSound = pygame.mixer.Sound("Audio/Sonic Jumping Sound.mp3")
rollingSound = pygame.mixer.Sound("Audio/Sonic Rolling Sound.mp3")
rollingSound.set_volume(0.5)
deathSound = pygame.mixer.Sound("Audio/Sonic Death Sound.mp3")
currMusic = ""
jwPos = 0.0

# load in images
logo = pygame.image.load("Images/Sonic Infinite Run Logo (Original, Smaller).png").convert_alpha()
background = pygame.image.load("Images/Pixel Background.jpg").convert_alpha()
helpScreenImg = pygame.image.load("Images/Help Image (Original, Smaller).jpeg").convert_alpha()
galleryImgLocked = pygame.image.load("Images/Gallery Image Locked Background.jpg").convert_alpha()
galleryCoverImg = pygame.image.load("Images/Gallery Cover Image.png").convert_alpha()
galleryImg1 = pygame.image.load("Images/Gallery Image 1.jpeg").convert_alpha()
galleryImg2 = pygame.image.load("Images/Gallery Image 2.jpeg").convert_alpha()
galleryImg3 = pygame.image.load("Images/Gallery Image 3.jpeg").convert_alpha()
galleryImg4 = pygame.image.load("Images/Gallery Image 4.jpeg").convert_alpha()
galleryImg5 = pygame.image.load("Images/Gallery Image 5.jpeg").convert_alpha()
galleryImg6 = pygame.image.load("Images/Gallery Image 6.jpeg").convert_alpha()
galleryImg7 = pygame.image.load("Images/Gallery Image 7.jpeg").convert_alpha()
galleryImg8 = pygame.image.load("Images/Gallery Image 8.jpeg").convert_alpha()
galleryImg9 = pygame.image.load("Images/Gallery Image 9.jpeg").convert_alpha()
galleryImg10 = pygame.image.load("Images/Gallery Image 10.jpeg").convert_alpha()
galleryImg11 = pygame.image.load("Images/Gallery Image 11.jpeg").convert_alpha()
runningAnimation = pygame.image.load("Images/Sonic Running Animation.png").convert_alpha()
jumpingAnimation = pygame.image.load("Images/Sonic Jumping Animation.png").convert_alpha()
rollingAnimation = pygame.image.load("Images/Sonic Rolling Animation.png").convert_alpha()
playImg = pygame.image.load("Images/playbuttonbase.png").convert_alpha()
helpImg = pygame.image.load("Images/helpbuttonbase.png").convert_alpha()
galleryClosedImg = pygame.image.load("Images/galleryclosedbase.png").convert_alpha()
galleryOpenImg = pygame.image.load("Images/galleryopenbase.png").convert_alpha()
galleryNextImg = pygame.image.load("Images/nextbuttonbase.png").convert_alpha()
galleryBackImg = pygame.image.load("Images/backbuttonbase.png").convert_alpha()
galleryNextOffImg = pygame.image.load("Images/nextbuttonoffbase.png").convert_alpha()
galleryBackOffImg = pygame.image.load("Images/backbuttonoffbase.png").convert_alpha()
menuButtonImg = pygame.image.load("Images/menubuttonbase.png").convert_alpha()
crabAnimation = pygame.image.load("Images/Crabmeat Animation.png").convert_alpha()
buzzerAnimation = pygame.image.load("Images/Buzzer Animation.png").convert_alpha()
drEggmanAnimation = pygame.image.load("Images/Dr Eggman Animation.png").convert_alpha()
"""
drEggManAnimation1 = pygame.image.load("Images/Dr Eggman Animation 1.png").convert_alpha()
drEggManAnimation2 = pygame.image.load("Images/Dr Eggman Animation 2.png").convert_alpha()
drEggManAnimation3 = pygame.image.load("Images/Dr Eggman Animation 3.png").convert_alpha()
drEggManAnimation4 = pygame.image.load("Images/Dr Eggman Animation 4.png").convert_alpha()
drEggManAnimation5 = pygame.image.load("Images/Dr Eggman Animation 5.png").convert_alpha()
"""

# running variables
runningSheet = spritesheet.SpriteSheet(runningAnimation)
runningList = []
runningSteps = 4
runningLastUpdate = pygame.time.get_ticks()
for i in range(runningSteps):
    runningList.append(runningSheet.get_image(i, 31, 40, 3, False, SPRITEBG))
runningFrame = 0
running = True
runningSpeeds = (175, 100)
runningSpeed = runningSpeeds[0]
runningSoundPlaying = False

# jumping variables
jumpingSheet = spritesheet.SpriteSheet(jumpingAnimation)
jumpingList = []
jumpingSteps = 2
jumpingLastUpdate = pygame.time.get_ticks()
for i in range(jumpingSteps):
    jumpingList.append(jumpingSheet.get_image(i, 25, 44, 3, False, SPRITEBG))
jumpingFrame = 0
jumping = False
jumpingSpeed = 20
# control up to down speed
gravity = 1.5
jumpHeight = 22.5
jumpVelocity = jumpHeight

# rolling variables
rollingSheet = spritesheet.SpriteSheet(rollingAnimation)
rollingList = []
rollingSteps = 4
rollingLastUpdate = pygame.time.get_ticks()
for i in range(rollingSteps):
    rollingList.append(rollingSheet.get_image(i, 25, 28, 3, False, SPRITEBG))
rollingFrame = 0
rolling = False
rollingSpeeds = (100, 60)
rollingSpeed = rollingSpeeds[0]
sPressed = False
rollYAdjust = 35

# crabmeat variables
crabSheet = spritesheet.SpriteSheet(crabAnimation)
crabList1 = []
crabList2 = []
crabList3 = []
crabSteps = 3
for i in range(crabSteps):
    crabList1.append(crabSheet.get_image(i, 47, 38, 1.75, False, SPRITEBG))
    crabList2.append(crabSheet.get_image(i, 47, 38, 2.25, False, SPRITEBG))
    crabList3.append(crabSheet.get_image(i, 47, 38, 2.5, False, SPRITEBG))
crabAniSpds = (500, 200)
crabAniSpd = crabAniSpds[0]
crabY1 = 283
crabY2 = 265
crabY3 = 255
crab2Min = 6
crab3Min = 7

# buzzer variables
buzzerSheet = spritesheet.SpriteSheet(buzzerAnimation)
buzzerList = []
buzzerSteps = 3
for i in range(buzzerSteps):
    buzzerList.append(buzzerSheet.get_image(i, 37, 25, 2, False, SPRITEBG))
buzzerAniSpds = (300, 200)
buzzerAniSpd = buzzerAniSpds[0]
buzzerYRange1 = (180, 225)
buzzerYRange2 = (170, 260)
buzzer2Min = 7

# dr eggman variables
eggmanSheet = spritesheet.SpriteSheet(drEggmanAnimation)
eggmanList1 = []
eggmanList2 = []
# eggmanList2 = [drEggManAnimation1, drEggManAnimation2, drEggManAnimation3, drEggManAnimation4, drEggManAnimation5]
eggmanSteps = 5
for i in range(eggmanSteps):
    # sswap the 4th and 5th frames
    if i == 3:
        i = 4
    elif i == 4:
        i = 3
    eggmanList1.append(eggmanSheet.get_image(i, 79, 77, 2, True, GREEN))
    eggmanList2.append(eggmanSheet.get_image(i, 79, 77, 3.5, True, GREEN))
eggmanAniSpds = (250, 100)
eggmanAniSpd = eggmanAniSpds[0]
eggmanY = 112
eggmanMin = 10
eggmanProb = 6
lastEggman = 0
eggmanInterval = 3

# used for collisions
sonicMask = pygame.mask.from_surface(runningList[0])
maskImg = sonicMask.to_surface()

# -- game progress variables --
# used to adjust scrolling background speed
scroll = 0
STARTSCROLLSPEED = 8
scrollSpeed = STARTSCROLLSPEED
maxSpeed = 20
# used to contain and create enemies
enemies = []
needEnemy = False
# used to maintain the score and speed up the scrolling
finalScore = -1
score = 0
lastSpeedUp = score
STARTSPEEDINTERVAL = 5
speedInterval = STARTSPEEDINTERVAL
# other
alive = True
collisionCount = 0

# high score
def getHighScore():
    # return the high score from the hs text file
    file = open("hs.txt", "r")
    hs = file.read()
    file.close()

    return int(hs)

def updateHighScore(newHS):
    file = open("hs.txt", "w")
    file.write(str(newHS))
    file.close()

highScore = getHighScore()

# used to adjust Sonic's position
MENUX = 585
MENUY = 235
GAMEX = 120
GAMEY = 235
sonicX = 585
sonicY = 235

# states (start on menu)
MENUSTATE = 0
GAMESTATE = 1
HELPSTATE = 2
GALLERYSTATE = 3
DEADSTATE = 4
currState = MENUSTATE

# buttons for states
# MENU
menuButtons = []
# GAME
gameMenuButton = button.Button(20, 20, MENUSTATE, menuButtonImg, 0.25, "MENU", 2, False, True)
gameButtons = [gameMenuButton]
# HELP
helpMenuButton = button.Button(20, 20, MENUSTATE, menuButtonImg, 0.25, "MENU", 2, False, True)
helpButtons = [helpMenuButton]
# GALLERY
galleryMenuButton = button.Button(20, 20, MENUSTATE, menuButtonImg, 0.25, "MENU", 2, False, True)
galleryButtons = [galleryMenuButton]
# create next and back buttons
nextButton = button.Button(SCREEN_WIDTH / 2 + 20, 471, -1, galleryNextImg, 0.15, "NEXT", 1, False, True)
backButton = button.Button(SCREEN_WIDTH / 2 - galleryBackImg.get_rect().width * 0.15 - 20, 471, -1, galleryBackImg, 0.15, "BACK", 1, False, True)
nextOffButton = button.Button(SCREEN_WIDTH / 2 + 20, 471, -1, galleryNextOffImg, 0.15, "NEXT", 1, False, False)
backOffButton = button.Button(SCREEN_WIDTH / 2 - galleryBackImg.get_rect().width * 0.15 - 20, 471, -1, galleryBackOffImg, 0.15, "BACK", 1, False, False)
# DEAD
deadMenuButton = button.Button(150, 390, MENUSTATE, menuButtonImg, 0.5, "MENU", 4, False, True)
deadPlayButton = button.Button(480, 380, GAMESTATE, playImg, 2.1, "", 0, True, True)
deadButtons = [deadMenuButton, deadPlayButton]

# help screen variables
sonicJumpingHS = enemy.Enemy(60, 100, jumpingList, jumpingSteps, 200, scrollSpeed, False)
sonicRollingHS = enemy.Enemy(60, 300, rollingList, rollingSteps, rollingSpeeds[0], scrollSpeed, False)
crabHS = enemy.Enemy(410, 120, crabList1, crabSteps, crabAniSpds[0], scrollSpeed, False)
buzzerHS = enemy.Enemy(420, 245, buzzerList, buzzerSteps, buzzerAniSpds[0], scrollSpeed, False)
eggmanHS = enemy.Enemy(370, 315, eggmanList1, eggmanSteps, eggmanAniSpds[0], scrollSpeed, True)
helpscreenAnimations = [sonicJumpingHS, sonicRollingHS, crabHS, buzzerHS, eggmanHS]

# gallery variables
galleryImages = [galleryCoverImg, galleryImg1, galleryImg2, galleryImg3, galleryImg4, galleryImg5, galleryImg6, galleryImg7, galleryImg8, galleryImg9, galleryImg10, galleryImg11]
numGalImages = 11
currGalImg = 0
galImgIntervals = 15
minGalleryHS = galImgIntervals


def createMenuButtons():
    global menuButtons
    # create menu buttons
    playButton = button.Button(530, 380, GAMESTATE, playImg, 2.1, "", 0, True, True)
    helpButton = button.Button(66, 390, HELPSTATE, helpImg, 0.5, "HELP", 3, False, True)
    # create the right gallery button based off the high score
    if highScore >= minGalleryHS:
        galleryButton = button.Button(296, 390, GALLERYSTATE, galleryOpenImg, 0.5, "GALLERY", 3, False, True)
    else:
        galleryButton = button.Button(296, 390, -1, galleryClosedImg, 0.5, "?", 4, False, False)
    buttons = [playButton, helpButton, galleryButton]

    menuButtons = buttons

createMenuButtons()

# state functions
def runMenu():
    global currState, sonicX, sonicY, menuButtons
    global running, jumping, rolling

    # background
    drawBackground(False)

    # logo
    screen.blit(logo, (-20, -200))

    # high score
    hsText = fontSize2.render("HIGH SCORE", True, WHITE)
    numText = fontSize2.render(str(highScore), True, RED)
    hsX = 600
    numX = hsX + hsText.get_width() - numText.get_width()
    hsY = 15
    numY = hsY + 40
    screen.blit(hsText, (hsX, hsY))
    screen.blit(numText, (numX, numY))

    # make sure sonic is always running in the menu
    # jumping will turn into running by itselfs
    if rolling:
        rolling = False
        running = True

    # move Sonic into position
    drawSonic()
    if (sonicX < MENUX):
        sonicX += 5

    # check buttons
    checkButtons(menuButtons)

def runGame():
    global currState, sonicX, sonicY, enemies, highScore
    global running, runningSoundPlaying
    global jumping, jumpingLastUpdate, jumpVelocity
    global rolling, rollingLastUpdate, sPressed
    global scrollSpeed, lastSpeedUp, speedInterval
    global finalScore

 
    # moving background
    drawBackground(True)

    if alive:
        # score
        scoreTextImg = fontSize1.render("SCORE", True, WHITE)
        numberTextImg = fontSize1.render(str(score), True, RED)
        numberX = SCREEN_WIDTH - (numberTextImg.get_width() + 20)
        scoreX = SCREEN_WIDTH - 130
        # adjust scoreX based on the length of the score
        digits = len(str(score))
        scoreX -= (digits - 1) * 10
        textY = 20
        screen.blit(scoreTextImg, (scoreX, textY))
        screen.blit(numberTextImg, (numberX, textY))

        # check buttons
        checkButtons(gameButtons)

    else:
        # update the high score if necessary
        if score > highScore:
            updateHighScore(score)
            highScore = score

        finalScore = score

        # move to dead state
        currState = DEADSTATE

    drawSonic()
    # move sonic into position
    if (sonicX > GAMEX):
        sonicX -= 5
    else:
        # after, start the game

        keysPressed = pygame.key.get_pressed()
        if keysPressed[pygame.K_SPACE]:
            # check for jumping
            # only play the sound when already mid-jump (prevents sound from playing multiple times)
            if not jumping:
                jumpingSound.play()
            jumping = True
            running = False
            jumpingLastUpdate = pygame.time.get_ticks()
        elif keysPressed[pygame.K_s]:
            # check for rolling
            # only update time when initially pressing s
            if not sPressed:
                # play rolling sound
                rollingSound.play(-1)
                rollingLastUpdate = pygame.time.get_ticks()
                sPressed = True
            if not jumping:
                rolling = True
                running = False
        elif not jumping and not keysPressed[pygame.K_s]:
            # if neither jumping nor rolling then running
            # play running sound
            if not runningSoundPlaying:
                runningSound.play(-1)
                runningSoundPlaying = True
            running = True
            jumping = False
            rolling = False
        
        # stop running sound
        if not running or not alive or not currState == GAMESTATE:
            runningSound.stop()
            runningSoundPlaying = False

        # stop jumping sound
        if not jumping or not alive or not currState == GAMESTATE:
            jumpingSound.stop()
            
        # stop rolling sound
        if not rolling or not alive or not currState == GAMESTATE:
            rollingSound.stop()
            sPressed = False

        # create enemies
        manageEnemies()
        checkCollisions()

        # update the speed every interval (truncate off decimals)
        if score - lastSpeedUp == int(speedInterval):
            # increase the interval to slow down speed up frequency
            speedInterval += 0.5

            # increase scroll speed if possible
            if scrollSpeed < maxSpeed:
                scrollSpeed += 1
                lastSpeedUp = score

                # update the speed of all enemies
                for enemy in enemies:
                    enemy.changeMoveAmnt(scrollSpeed)

                # increment the animation speeds
                incrementAniSpds()

def helpScreen():
    # display the background
    screen.blit(helpScreenImg, (0, 0))

    # check buttons
    checkButtons(helpButtons)

    # create animations
    for animation in helpscreenAnimations:
        animation.draw(screen)

def showGallery():
    global currGalImg

    if highScore >= currGalImg * galImgIntervals:
        canDisplay = True
    else:
        canDisplay = False

    # only display the image if the high score is high enough
    if canDisplay:
        screen.blit(galleryImages[currGalImg], (0, 0))
    else:
        # otherwise state the necessary high score
        screen.blit(galleryImgLocked, (0, 0))
        text = fontSize2.render("UNLOCKS AT A HIGH SCORE OF", True, WHITE)
        textX = SCREEN_WIDTH / 2 - text.get_width() / 2
        textY = SCREEN_HEIGHT / 2 - text.get_height()
        # get the minimum high score
        if currGalImg == len(galleryImages) - 1:
            # necessary score for QR Code is same as last picture
            minHS = numGalImages * galImgIntervals
        else:
            minHS = currGalImg * galImgIntervals
        minHSText = fontSize3.render(str(minHS), True, WHITE)
        hsX = SCREEN_WIDTH / 2 - minHSText.get_width() / 2
        hsY = SCREEN_HEIGHT / 2
        screen.blit(text, (textX, textY))
        screen.blit(minHSText, (hsX, hsY))

    # create next and back buttons
    # turn them off if necessary
    if currGalImg == 0:
        back = backOffButton
    else:
        back = backButton
    if currGalImg == len(galleryImages) - 1:
        next = nextOffButton
    else:
        next = nextButton
    next.drawButton(screen)
    back.drawButton(screen)

    # allow changing the picture
    nextClicked = next.checkClicked()
    backClicked = back.checkClicked()
    if nextClicked and currGalImg < len(galleryImages) - 1:
        currGalImg += 1
    elif backClicked and currGalImg > 0:
        currGalImg -= 1

    # display current page number
    num = fontSize1.render(str(currGalImg + 1), True, BLUE)
    numX = SCREEN_WIDTH / 2 - num.get_width() / 2
    numY = 465
    screen.blit(num, (numX + 2, numY))

    # check buttons
    checkButtons(galleryButtons)
        
def deadScreen():
    global currState

    # display the score
    totalText = fontSize3.render("SCORE  " + str(finalScore), True, RED)
    scoreText = fontSize3.render("SCORE", True, WHITE)
    numText = fontSize3.render(str(finalScore), True, RED)
    startX = SCREEN_WIDTH / 2 - totalText.get_width() / 2
    endX = SCREEN_WIDTH / 2 + totalText.get_width() / 2
    scoreX = startX
    numX = endX - numText.get_width()
    y = 40

    screen.blit(scoreText, (scoreX, y))
    screen.blit(numText, (numX, y))

    # check buttons
    checkButtons(deadButtons)


# other functions
def resetGameVariables():
    global scrollSpeed, enemies, needEnemy, score, lastSpeedUp, speedInterval, alive, collisionCount
    global runningSpeed, rollingSpeed, crabAniSpd, buzzerAniSpd, eggmanAniSpd

    # reset game progress variables
    scrollSpeed = STARTSCROLLSPEED
    enemies = []
    needEnemy = False
    score = 0
    lastSpeedUp = score
    speedInterval = STARTSPEEDINTERVAL
    alive = True
    collisionCount = 0

    # reset animation variables
    runningSpeed = runningSpeeds[0]
    rollingSpeed = rollingSpeeds[0]
    crabAniSpd = crabAniSpds[0]
    buzzerAniSpd = buzzerAniSpds[0]
    eggmanAniSpd = eggmanAniSpds[0]


def manageEnemies():
    global needEnemy, enemies, score

    # need a new enemy if there are none or the oldest one passed Sonic/is off the screen
    if len(enemies) == 0:
        needEnemy = True
    elif enemies[-1].getX() + enemies[-1].getWidth() < sonicX or enemies[-1].getY() > SCREEN_HEIGHT:
        needEnemy = True
        # update the score
        score += 1
        

    # if there are no enemies or the last enemy passed sonic, create a random one
    if needEnemy:
        generateEnemy()
        needEnemy = False
    
    # move each current enemy, and delete if they're off the screen
    remainingEnemies = []
    for e in enemies:
        if e.alive:
            e.move(screen)
        else:
            e.deathAnimation(screen)
        # only keep enemies still on the screen
        if e.getX() + e.getWidth() > 0 and e.getY() < SCREEN_HEIGHT:
            remainingEnemies.append(e)

    enemies = remainingEnemies

def generateEnemy():
    global lastEggman

    randNum = random.randint(1, 50)
    randDist = random.randint(0, 50) # random dist to spawn from

    # create a different enemy based off the randNum
    if randNum % 2 != 0:
        # number is odd
        # create a random number of crabmeats
        if scrollSpeed < 8:
            numCrabs = 1
        elif scrollSpeed < 12:
            numCrabs = random.randint(1, 2)
        else:
            numCrabs = random.randint(2, 3)

        createCrabs(numCrabs, randDist)
    else:
        if randNum % eggmanProb == 0 and score > eggmanMin and score - lastEggman >= eggmanInterval:
            # number is divisible by 6, score is at least eggmanMin, and enough enemies have spawned between eggmans
            # create an eggman
            newEnemy = enemy.Enemy(SCREEN_WIDTH + randDist, eggmanY, eggmanList2, eggmanSteps, eggmanAniSpd, scrollSpeed, True)
            lastEggman = score
        else:
            # number is even
            # create a buzzer
            if scrollSpeed < buzzer2Min:
                randY = random.randint(buzzerYRange1[0], buzzerYRange1[1])
            else:
                randY = random.randint(buzzerYRange2[0], buzzerYRange2[1])
            newEnemy = enemy.Enemy(SCREEN_WIDTH + randDist, randY, buzzerList, buzzerSteps, buzzerAniSpd, scrollSpeed, False)
    
        
        enemies.append(newEnemy)

def createCrabs(num, dist):
    global enemies

    x = SCREEN_WIDTH + dist

    # X - TEST SIZES
    if num == 1:
        if scrollSpeed < 6:
            maxSize = [1]
        elif scrollSpeed < 7:
            maxSize = [2]
        else:
            maxSize = [3]
    elif num == 2:
        if 8 <= scrollSpeed <= 9:
            maxSize = [1,1]
        elif 10 <= scrollSpeed <= 11:
            maxSize = [2,1]
        elif 12 <= scrollSpeed <= 13:
            maxSize = [2,2]
        elif 14 <= scrollSpeed <= 15:
            maxSize = [3,2]
        else:
            maxSize = [3,3]
    else:
        # num == 3
        if 12 <= scrollSpeed <= 13:
            maxSize = [1, 1, 1]
        elif 14 <= scrollSpeed <= 15:
            maxSize = [2, 1, 1]
        elif 16 <= scrollSpeed <= 17:
            maxSize = [3, 2, 1]
        elif 18 <= scrollSpeed <= 19:
            maxSize = [3, 3, 1]
        else:
            maxSize = [3, 3, 2]

    currMax = 0

    # create as many crabs as required
    # move each crab's x over by the width of the previous (1st frame)
    for i in range(num):
        max = maxSize[currMax]

        # if the max size has been made, move on to the next max size
        size = random.randint(1, max)
        if size == max:
            currMax += 1
        
        # create the correct size crab
        if size == 1:
            crabList = crabList1
            crabY = crabY1
        elif size == 2:
            crabList = crabList2
            crabY = crabY2
        else:
            # crabSize == 3
            crabList = crabList3
            crabY = crabY3

        # add the crab to the enemies list
        newCrab = enemy.Enemy(x, crabY, crabList, crabSteps, crabAniSpd, scrollSpeed, False)
        enemies.append(newCrab)

        # move the next crab over by the width of the first crab (first frame)
        x += crabList[0].get_rect().width

def checkCollisions():
    global alive, collisionCount

    # get sonic's current coordinates
    x = sonicX
    if rolling:
        y = sonicY + rollYAdjust
    else:
        y = sonicY

    # get sonic's current rect
    if running:
        sonicRect = runningList[runningFrame].get_rect()
    elif jumping:
        sonicRect = jumpingList[jumpingFrame].get_rect()
    else:
        # rolling
        sonicRect = rollingList[rollingFrame].get_rect()
    sonicRect.topleft = (x, y)

    """
    surface1 = pygame.Surface((sonicRect.width, sonicRect.height))
    screen.blit(surface1, (sonicRect.x, sonicRect.y))
    """

    # compare sonic's rect to the rect of all current enemies
    for enemy in enemies:
        enemyRect = enemy.getRect()
        enemyX, enemyY = enemy.getX(), enemy.getY()
        enemyRect.topleft = (enemyX, enemyY)
        """
        surface2 = pygame.Surface((enemyRect.width, enemyRect.height))
        screen.blit(surface2, (enemyRect.x, enemyRect.y))
        """
        
        # if the rects are colliding, check for actual collision
        if sonicRect.colliderect(enemyRect):
            enemyMask = enemy.getMask()
            """
            enemyMaskImg = enemyMask.to_surface()
            screen.blit(enemyMaskImg, (enemyX, enemyY))
            """
            if sonicMask.overlap(enemyMask, (enemyX - x, enemyY - y)):
                collisionCount += 1
                # print("collision " + str(collisionCount))
                # allow sonic to kill eggman/bosses
                if not (enemy.isBoss and rolling) and enemy.alive:
                    # print("dead")
                    alive = False
                    deathSound.play()
                else:
                    # kill the boss
                    enemy.makeDead()

def incrementAniSpds():
    global runningSpeed, rollingSpeed, crabAniSpd, buzzerAniSpd, eggmanAniSpd

    decreases = maxSpeed - STARTSCROLLSPEED

    # decrease the time taken for each animation
    if runningSpeed - (runningSpeeds[0] - runningSpeeds[1]) / decreases > runningSpeeds[1]:
        runningSpeed -= (runningSpeeds[0] - runningSpeeds[1]) / decreases
    
    if rollingSpeed - (rollingSpeeds[0] - rollingSpeeds[1]) / decreases > rollingSpeeds[1]:
        rollingSpeed -= (rollingSpeeds[0] - rollingSpeeds[1]) / decreases
    
    if crabAniSpd - (crabAniSpds[0] - crabAniSpds[1]) / decreases > crabAniSpds[1]:
        crabAniSpd -= (crabAniSpds[0] - crabAniSpds[1]) / decreases
    
    if buzzerAniSpd - (buzzerAniSpds[0] - buzzerAniSpds[1]) / decreases > buzzerAniSpds[1]:
        buzzerAniSpd -= (buzzerAniSpds[0] - buzzerAniSpds[1]) / decreases

    if eggmanAniSpd - (eggmanAniSpds[0] - eggmanAniSpds[1]) / decreases > eggmanAniSpds[1]:
        eggmanAniSpd -= (eggmanAniSpds[0] - eggmanAniSpds[1]) / decreases


def checkButtons(buttonList):
    global currState, currGalImg

    # display buttons
    for i in range(len(buttonList)):
        button = buttonList[i]
        clicked = button.checkClicked()
        button.drawButton(screen)
        if clicked:
            # change state if button is clicked
            # don't change state if the button is locked
            if button.on:
                currState = button.state
                # reset menu buttons every time you go to the menu
                if button.state == MENUSTATE:
                    createMenuButtons()
                # reset game variables every time game starts
                if button.state == GAMESTATE:
                    resetGameVariables()
                # always start the gallery at the first picture
                if button.state == GALLERYSTATE:
                    currGalImg = 0
                # print("state changed to " + str(currState))


def drawText(text, font, colour, x, y):
    # create a text image and display it on the screen
    textImg = font.render(text, True, colour)
    textImg.get_width()
    screen.blit(textImg, (x, y))

def drawSonic():
    global sonicX, sonicY
    global sonicMask, maskImg
    global running, runningFrame, runningLastUpdate
    global jumping, jumpingFrame, jumpingLastUpdate, jumpVelocity
    global rolling, rollingFrame, rollingLastUpdate

    if running:
        runTime = pygame.time.get_ticks()
        screen.blit(runningList[runningFrame], (sonicX, sonicY))
        # update mask
        sonicMask = pygame.mask.from_surface(runningList[runningFrame])
        # change frame every interval (runningSpeed)
        if runTime - runningLastUpdate >= runningSpeed:
            if runningFrame == runningSteps - 1:
                runningFrame = 0
            else:
                runningFrame += 1
            runningLastUpdate = runTime
    elif jumping:
        jumpTime = pygame.time.get_ticks()
        screen.blit(jumpingList[jumpingFrame], (sonicX, sonicY))
        # update mask
        sonicMask = pygame.mask.from_surface(jumpingList[jumpingFrame])
        # change frame every interval (jumpingSpeed)
        if jumpTime - jumpingLastUpdate >= jumpingSpeed:
            # change the frames and stop at the last jumping frame
            if jumpingFrame < jumpingSteps - 1:
                jumpingFrame += 1
            jumpingLastUpdate = jumpTime
        # increase Sonic's height
        sonicY -= jumpVelocity
        # decrease the speed at which the height is increasing
        jumpVelocity -= gravity
        # check if the jump has finished
        if jumpVelocity < -jumpHeight:
            jumpVelocity = jumpHeight
            jumping = False
            running = True
            # reset jump animation
            jumpingFrame = 0
    else:
        # rolling
        rollTime = pygame.time.get_ticks()
        screen.blit(rollingList[rollingFrame], (sonicX, sonicY + rollYAdjust))
        # update mask
        sonicMask = pygame.mask.from_surface(rollingList[rollingFrame])
        # change frame every interval (rollingSpeed)
        if rollTime - rollingLastUpdate >= rollingSpeed:
            if rollingFrame == rollingSteps - 1:
                rollingFrame = 0
            else:
                rollingFrame += 1
            rollingLastUpdate = rollTime
    # update mask
    maskImg = sonicMask.to_surface()
       

def drawBackground(moving):
    global scroll

    bgWidth = background.get_width()
    tiles = math.ceil(SCREEN_WIDTH / bgWidth) + 1

    # draw enough bg img tiles to fill the screen
    for i in range(0, tiles):
        screen.blit(background, (i * bgWidth + scroll, -190))
    
    if moving:
        # scroll background
        scroll -= scrollSpeed

        # reset scroll
        if abs(scroll) > bgWidth:
            scroll = 0


# main while loop
runningGame = True

while runningGame:

    clock.tick(FPS)

    # check state
    if currState == MENUSTATE:
        runMenu()
    elif currState == GAMESTATE:
        runGame()
    elif currState == HELPSTATE:
        helpScreen()
    elif currState == GALLERYSTATE:
        showGallery()
    elif currState == DEADSTATE:
        deadScreen()
    else:
        # currState == GALLERYSTATE
        pass


    # check keyboard, mouse, etc. clicks
    for event in pygame.event.get():

        # close if X is pressed
        if event.type == pygame.QUIT:
            runningGame = False

    # play the correct music based off the current state
    if currState == MENUSTATE or currState == HELPSTATE or currState == GALLERYSTATE:
        if currMusic != "Juice WRLD":
            pygame.mixer.music.load("Audio/Keep Up (Sonic) by Juice WRLD.mp3")
            # print(jwPos)
            pygame.mixer.music.play(-1, jwPos / 1000, 5000)
            currMusic = "Juice WRLD"
    elif currState == GAMESTATE:
        if currMusic == "Juice WRLD":
            # save the point the song left off at
            jwPos = pygame.mixer.music.get_pos()
        if currMusic != "Sonic":
            pygame.mixer.music.load("Audio/Sonic Background Music.mp3")
            pygame.mixer.music.play(-1, 0, 5000)
            currMusic = "Sonic"
    else:
        # no music on dead state
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            currMusic = ""
    
    pygame.display.update()

# close pygame
pygame.quit()