# Maher Rahman
# Created on 2/8/2024
# enemy template class, used to create enemies that move across the screen from
# right to left

import pygame

pygame.init()


class Enemy():
    def __init__(self, x, y, images, steps, animationSpd, moveAmnt, isBoss):
        # initialize attribute variables
        self.alive = True
        self.currFrame = 0
        self.moves = 0
        self.drops = 0
        self.lastUpdate = pygame.time.get_ticks()
        self.x = x
        self.y = y
        self.images = images
        self.steps = steps
        self.animationSpd = animationSpd
        self.moveAmnt = moveAmnt
        self.isBoss = isBoss
        self.alive = True

    def move(self, display):
        currTime = pygame.time.get_ticks()
        display.blit(self.images[self.currFrame], (self.x - self.moves, self.y))
        
        # change frame every interval (animationSpd)
        if currTime - self.lastUpdate >= self.animationSpd:
            if self.currFrame == self.steps - 1:
                self.currFrame = 0
            else:
                self.currFrame += 1
            self.lastUpdate = currTime

        # move 
        self.moves += self.moveAmnt
    
    def draw(self, display):
        currTime = pygame.time.get_ticks()
        display.blit(self.images[self.currFrame], (self.x, self.y))
        
        # change frame every interval (animationSpd)
        if currTime - self.lastUpdate >= self.animationSpd:
            if self.currFrame == self.steps - 1:
                self.currFrame = 0
            else:
                self.currFrame += 1
            self.lastUpdate = currTime

    def getRect(self):
        # get enemy's current rect
        rect = self.images[self.currFrame].get_rect()
        return rect
    
    def getMask(self):
        # get enemy's mask
        mask = pygame.mask.from_surface(self.images[self.currFrame])
        return mask
    
    def getX(self):
        # get x coordinate
        return self.x - self.moves
    
    def getY(self):
        # get y coordinate
        return self.y + self.drops
    
    def getWidth(self):
        # return the current frame's width
        return self.images[self.currFrame].get_rect().width
    
    def getHeight(self):
        # return the current frame's width
        return self.images[self.currFrame].get_rect().width
    
    def changeMoveAmnt(self, newAmnt):
        # change the enemy's movement speed
        self.moveAmnt = newAmnt

    def makeDead(self):
        # change the enemy's status to dead
        self.alive = False

    def deathAnimation(self, display):
        currTime = pygame.time.get_ticks()
        display.blit(self.images[self.currFrame], (self.x - self.moves, self.y + self.drops))

        # move down
        self.drops += self.moveAmnt

        # make dead
        self.alive = False


