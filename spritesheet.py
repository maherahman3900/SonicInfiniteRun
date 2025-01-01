# Maher Rahman
# Created on ???
# SpriteSheet template class used to extract frames from a spritesheet

import pygame

class SpriteSheet():
    def __init__(self, sheet):
        self.sheet = sheet
    
    def get_image(self, frame, width, height, scale, flipX, colour):
        # make a surface to display the image on
        image = pygame.Surface((width, height)).convert_alpha()
        # make the surface a colour which is not in the frames
        image.fill(colour)
        # cut out the frame from the spritesheet and blit it on the top left corner of the surface
        image.blit(self.sheet, (0,0), ((frame * width), 0, width, height))
        # scale the frame
        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        # flip each frame horizontally if required
        if flipX:
            image = pygame.transform.flip(image, True, False)
        # get rid of background on frame
        image.set_colorkey(colour)

        return image