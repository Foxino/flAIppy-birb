import pygame
import os

BIRB_PNG = pygame.image.load(os.path.join("assets","birb_ph.png"))
BIRB = pygame.transform.scale(BIRB_PNG, (45, 45))
GRAVITY = 4

class Birb():
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def draw(self, w):
        self.y += GRAVITY
        w.blit(BIRB, (self.x, self.y))
    def addForce(self):
        self.y -= 60