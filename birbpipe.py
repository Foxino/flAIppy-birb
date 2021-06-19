import pygame
import os
from random import randrange

PIPE_H, PIPE_W = 400, 100
PIPE_PNG = pygame.image.load(os.path.join("assets","pipe.png"))
BOT_PIPE = pygame.transform.scale(PIPE_PNG, (PIPE_W, PIPE_H))
TOP_PIPE = pygame.transform.rotate(BOT_PIPE, 180)

class Pipe():
    def __init__(self, x, max_x):
        self.max_x = max_x
        self.setup(x)
    def draw(self, w):
        self.x -= 1
        if self.x < -50:
            self.setup(self.max_x)
        w.blit(TOP_PIPE, (self.x, self.top_y))
        w.blit(BOT_PIPE, (self.x, self.bot_y))
    def setup(self, x):
        self.x = x
        self.offset = randrange(0, 370)
        self.top_y = -400 + self.offset
        self.top_b_y = self.top_y + PIPE_H
        self.bot_y = self.top_b_y + 150



