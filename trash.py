# check collision between mask and a bullet on mouse's position
"""
# create bullet
bullet = pygame.Surface((10,10))
bulletMask = pygame.mask.from_surface(bullet)
pos = pygame.mouse.get_pos()
# check overlap
x = sonicX
if rolling:
    y = sonicY + rollYAdjust
else:
    y = sonicY
if sonicMask.overlap(bulletMask, (pos[0] - x, pos[1] - y)):
    bulletCol = BLUE
else:
    bulletCol = RED
bullet.fill(bulletCol)
screen.blit(bullet, pos)
"""
# create one of each kind of enemy
"""
crab1 = enemy.Enemy(SCREEN_WIDTH + 100, crabY, crabList, crabSteps, crabAniSpd, scrollSpeed)
crab1.move(screen)
enemies.append(crab1)
"""
"""
buzzer1 = enemy.Enemy(SCREEN_WIDTH + 100, 225, buzzerList, buzzerSteps, buzzerAniSpd, scrollSpeed)
buzzer1.move(screen)
enemies.append(buzzer1)
"""
"""
eggman1 = enemy.Enemy(SCREEN_WIDTH + 100, eggmanY, eggmanList, eggmanSteps, eggmanAniSpd, scrollSpeed)
eggman1.move(screen)
enemies.append(eggman1)
"""
# turn off next button if one past the latest available image
"""
# create next and back buttons
    maxImgs = int(highScore / galImgIntervals)
    print(currGalImg)
    print(maxImgs)

    # turn them off if necessary
    if currGalImg == 0:
        back = backOffButton
    else:
        back = backButton
    if currGalImg == len(galleryImages) - 1 or currGalImg > maxImgs + 1:
        next = nextOffButton
    else:
        next = nextButton
    next.drawButton(screen)
    back.drawButton(screen)
"""