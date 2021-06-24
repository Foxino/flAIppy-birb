import pygame
import os
from random import randrange

PIPE_H, PIPE_W = 400, 100
PIPE_PNG = pygame.image.load(os.path.join("assets","pipe.png"))
BOT_PIPE = pygame.transform.scale(PIPE_PNG, (PIPE_W, PIPE_H))
TOP_PIPE = pygame.transform.rotate(BOT_PIPE, 180)


class Pipes():
    def __init__(self, x, max_x):
        self.max_x = max_x
        self.setup(x)
        self.pipe_w = PIPE_W
        self.color = (255,255,0)
        self.scored = False
    def draw(self, w):
        self.x -= 1
        if self.x < -50:
            self.setup(self.max_x)
        w.blit(TOP_PIPE, (self.x, self.top_y))
        ##pygame.draw.rect(w, self.color, pygame.Rect(self.x, self.top_y, PIPE_W, PIPE_H))
        w.blit(BOT_PIPE, (self.x, self.bot_y))
        ##pygame.draw.rect(w, self.color, pygame.Rect(self.x, self.bot_y, PIPE_W, PIPE_H))
    def setup(self, x):
        self.scored = False
        self.x = x
        self.offset = randrange(0, 250)
        self.top_y = -400 + self.offset
        self.top_b_y = self.top_y + PIPE_H
        self.bot_y = self.top_b_y + 200



