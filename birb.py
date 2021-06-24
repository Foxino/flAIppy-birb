import pygame
import os

BIRB_PNG = pygame.image.load(os.path.join("assets","birb.png"))
BIRB_SIZE = 55
BIRB = pygame.transform.scale(BIRB_PNG, (BIRB_SIZE, BIRB_SIZE))
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)

GRAVITY = 0.5
VEL_CAP = 8

class Birb():
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.vel = 0
        self.alive = True
        self.score = 0

    def draw(self, w, pipes):

        ## grav logic
        self.vel += GRAVITY
        if self.vel > VEL_CAP:
            self.vel = VEL_CAP

        
        ## update vel
        self.y += int(self.vel)

        ## rotate
        self.image = pygame.transform.rotate(BIRB, self.vel * -3)

        ## pipe detection
        for pipe in pipes:
            if (self.x + BIRB_SIZE) > pipe.x and self.x < (pipe.x + pipe.pipe_w):
                if(self.y < pipe.top_b_y or (self.y+BIRB_SIZE) > pipe.bot_y):
                    self.alive = False
            elif ((self.x + BIRB_SIZE) > (pipe.x + pipe.pipe_w) and pipe.scored == False and self.alive == True):
                pipe.scored = True
                self.score += 1
                

        w.blit(self.image, (self.x, self.y))

        if self.alive == True:
            sc = str(self.score)
            col = (255,255,255)
        else:
            sc = "X__X"
            col = (255,0,0)
        
        text = font.render(sc, True, col)
        w.blit(text, (self.x + (BIRB_SIZE/2), self.y - 25))

    def flap(self):
        if self.alive == True:
            self.vel = -10