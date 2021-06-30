import pygame
import os
from operator import attrgetter

BIRB_PNG = pygame.image.load(os.path.join("assets","birb.png"))
BIRB_SIZE = 55
BIRB = pygame.transform.scale(BIRB_PNG, (BIRB_SIZE, BIRB_SIZE))
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)

GRAVITY = 0.5
VEL_CAP = 8

class Birb():
    def __init__(self, x, y, debug):
        self.y = y
        self.x = x
        self.vel = 0
        self.alive = True
        self.score = 0
        self.lastPipe = None
        self.nextPipe = None
        self.debug = debug

    def reset(self, x, y):
        self.y = y
        self.x = x
        self.vel = 0
        self.alive = True
        self.score = 0
        self.lastPipe = None
        self.nextPipe = None

    def draw(self, w, pipes):

        ## grav logic
        self.vel += GRAVITY
        if self.vel > VEL_CAP:
            self.vel = VEL_CAP

        
        ## update vel
        self.y += int(self.vel)

        ## rotate
        self.image = pygame.transform.rotate(BIRB, self.vel * -3)

        ## set target pipes
        if self.nextPipe == None:
            self.nextPipe = min(pipes, key=attrgetter('x'))
            self.lastPipe = max(pipes, key=attrgetter('x'))

        ## pipe detection
        for pipe in pipes:
            if (self.x + BIRB_SIZE) > pipe.x and self.x < (pipe.x + pipe.pipe_w):
                if(self.y < pipe.top_b_y or (self.y+BIRB_SIZE) > pipe.bot_y):
                    self.alive = False
            elif ((self.x + BIRB_SIZE) > (pipe.x) and self.alive == True and pipe != self.lastPipe):
                self.score += 1
                self.nextPipe, self.lastPipe = self.lastPipe, pipe

        
        ## visualize target pipe
        if self.alive == True and self.debug == True:
            pygame.draw.line(w, (255,0,0), ((self.x + BIRB_SIZE), self.y), (self.nextPipe.x, self.nextPipe.top_b_y), 3)
            pygame.draw.line(w, (255,0,0), ((self.x + BIRB_SIZE), self.y), (self.nextPipe.x, self.nextPipe.bot_y), 3)
            pygame.draw.line(w, (255,255,255), ((self.x + BIRB_SIZE), self.y), ((self.x + BIRB_SIZE), self.nextPipe.top_b_y), 2)
            pygame.draw.line(w, (255,255,255), ((self.x + BIRB_SIZE), self.y), ((self.x + BIRB_SIZE), self.nextPipe.bot_y), 2)
            pygame.draw.line(w, (255,255,255), ((self.x + BIRB_SIZE), self.y), (self.nextPipe.x, self.y), 2)
            txt = font.render(str(self.vel), True, (255,255,255))
            w.blit(txt, (self.x + (BIRB_SIZE/2), (self.y + BIRB_SIZE *1.5)))

        w.blit(self.image, (self.x, self.y))

        ## if bird goes off screen, it dies
        if self.y > 400 or self.y < 0:
            self.alive = False


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