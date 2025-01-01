# Maher Rahman
# Created on 25/7/2024
# Button template class used to create interactive buttons for the game.

import pygame
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (252,36,36)
BLUE = (36,140,252)

# fonts
buttonFontSmall = pygame.font.Font("Fonts/pixelated.ttf", 20)
buttonFontMedium = pygame.font.Font("Fonts/pixelated.ttf", 30)
buttonFontBig = pygame.font.Font("Fonts/pixelated.ttf", 40)
buttonFontBiggest = pygame.font.Font("Fonts/pixelated.ttf", 50)

# audio
hoverSFX = pygame.mixer.Sound("Audio/Button Hover Sound.mp3")
buttonClickSFX = pygame.mixer.Sound("Audio/Regular Button Click Sound.mp3")
playClickSFX = pygame.mixer.Sound("Audio/Play Button Click Sound.mp3")


class Button():
    # constructor method
    def __init__(self, x, y, state, image, scale, text, fontSize, playButton, on):
        # necessary attribute variables
        self.state = state
        self.scale = scale
        self.text = text
        self.fontSize = fontSize
        self.playButton = playButton
        self.on = on
        self.actionColour = WHITE
        self.hovering = False

        # scale image
        self.width = image.get_width() * scale
        self.height = image.get_height() * scale

        # create button using image
        self.image = pygame.transform.scale(image, (int(self.width), int(self.height)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    # method to create the button on the screen and check for clicks
    def drawButton(self, display):
        # draw the button
        display.blit(self.image, (self.rect.x, self.rect.y))

        # if it is the play button draw the triangle
        if self.playButton:
            point1 = (int(self.rect.x + (self.width)/2 - 12 * self.scale), int(self.rect.y + (self.height)/2 - 13 * self.scale))
            point2 = (int(self.rect.x + (self.width)/2 - 12 * self.scale), int(self.rect.y + (self.height)/2 + 13 * self.scale))
            point3 = (int(self.rect.x + (self.width)/2 + 12 * self.scale), int(self.rect.y + (self.height)/2))
            pygame.draw.polygon(display, self.actionColour, [point1, point2, point3])
        # otherwise, display the button's text
        else: 
            # create a text image and display it on the screen
            # if the button is not unlocked don't change text colour
            if not self.on:
                self.actionColour = WHITE

            # use proper font size
            if self.fontSize == 1:
                textImg = buttonFontSmall.render(self.text, True, self.actionColour)
            elif self.fontSize == 2:
                textImg = buttonFontMedium.render(self.text, True, self.actionColour)
            elif self.fontSize == 3:
                textImg = buttonFontBig.render(self.text, True, self.actionColour)
            else:
                # self.fontSize == 4
                textImg = buttonFontBiggest.render(self.text, True, self.actionColour)

            # determine where to place the text in the button
            buttonW = self.width
            buttonH = self.height
            textW = textImg.get_width()
            textH = textImg.get_height()
            startX = self.rect.x + (buttonW - textW) / 2
            startY = self.rect.y + (buttonH - textH) / 2

            display.blit(textImg, (int(startX + 4 * self.scale), int(startY + 2 * self.scale)))

    def checkHovering(self):
        # check mouse position
        pos = pygame.mouse.get_pos()

        # change text colour if hovering
        if self.rect.collidepoint(pos):
            self.actionColour = BLUE

            # play hover sfx the first time button is hovered (if it is on)
            if self.hovering == False:
                if self.on:
                    hoverSFX.play()
                self.hovering = True
        else:
            self.actionColour = WHITE
            self.hovering = False
        
        return self.hovering


    def checkClicked(self):
        # variable used to determine if button's action should be performed
        clicked = False

        hovering = self.checkHovering()

        if hovering:
            # check if clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                if self.on:
                    self.clicked = True
                    clicked = True

                    # play the correct clicking sound
                    if self.playButton:
                        playClickSFX.play()
                    else:
                        buttonClickSFX.play()
        
        # when not clicking
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return clicked
    
    def turnOff(self):
        # turn off the button
        self.on = False

    def turnOn(self):
        # turn on the button
        self.on = True