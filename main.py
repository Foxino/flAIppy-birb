import pygame
from birbpipe import Pipes
from birb import Birb
from qbot import QBot
import math
import argparse


## game window dimensions
WIDTH, HEIGHT = 450, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)

pipe = Pipes(WIDTH, WIDTH)
pipe2 = Pipes(WIDTH + (WIDTH/2), WIDTH)

pipes = [pipe, pipe2]

MODE_AI, MODE_HUMAN = 'AI', 'HUMAN'
DEBUG, MODE = False, MODE_HUMAN

## window paras
FPS = 60

def main(birbs, clear):
    gameRunning = True
    clock = pygame.time.Clock()

    ## in AI mode, creates the bot and attaches the agent to it.
    if MODE == MODE_AI:
        bot = QBot()
        if clear == True:
            bot.reset()
        bot.addAgent(birbs[0])
    else:
        bot = None

    t = 0

    ## game loop
    while gameRunning:
        clock.tick(FPS)

        t += 1

        ## window close event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False
            if event.type == pygame.KEYDOWN and MODE != MODE_AI:
                if event.key == pygame.K_SPACE:
                    if any(x.alive == True for x in birbs) == False:
                        reset(birbs, pipes)
                    else:
                        birbs[0].flap()

        ## in AI mode, checks for action
        if MODE == MODE_AI:
            fl = bot.action()
            if fl == 1:
                bot.birb.flap()

        
        ##draw function
        draw(birbs, bot, math.floor(t/60))
            
        if MODE == MODE_AI:
            bot.reward()
            ## if birb perished, start over
            if any(x.alive == True for x in birbs) == False:
                bot.count += 1
                bot.saveQValues()
                if bot.record < math.floor(t/60):
                    bot.record = math.floor(t/60)
                t = 0
                reset(birbs, pipes)

    if MODE == MODE_AI:
        bot.saveQValues()
    
    pygame.quit()

def reset(birbs, pipes):
    for birb in birbs:
        birb.reset(WIDTH/4, HEIGHT/4)
    pipes[0].reset(WIDTH, WIDTH)
    pipes[1].reset(WIDTH + (WIDTH/2), WIDTH)

def draw(birbs, bot, t):
    ## background colour
    WIN.fill((0, 200, 255))

    for pipe in pipes: 
        pipe.draw(WIN)

    for birb in birbs:
        birb.draw(WIN, pipes)

    if any(x.alive == True for x in birbs) == False and MODE == MODE_HUMAN:
        text = font.render("Game Over!", True, (255,255,255))
        text2 = font.render("Press SPACE to try again!", True, (255,255,255))
        WIN.blit(text, (WIDTH * .2, HEIGHT * .4))
        WIN.blit(text2, (5, HEIGHT * .6))

    
    if MODE == MODE_AI:
        text = font.render("Generation : {0}".format(bot.count), True, (255,255,255))
        text2 = font.render("Record : {0}s".format(bot.record), True, (255,255,255))
        text3 = font.render("Current : {0}s".format(t), True, (255,255,255))
        WIN.blit(text, (5, 5))
        WIN.blit(text2, (5, 45))
        WIN.blit(text3, (5, 85))
    ## update window
    pygame.display.update()
    

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--bot', '-b', action='store_true', help='Run with bot.')
    parser.add_argument('--showdebug', '-d', action='store_true', help='Show debug info')
    parser.add_argument('--clear', '-c',action='store_true', help='Clear training data')

    args = parser.parse_args()
 
    DEBUG = args.showdebug
    CLEAR = args.clear

    if args.bot == True:
        MODE = MODE_AI
        pygame.display.set_caption("FlAIppy Birb - AI Mode")
    else:
        MODE = MODE_HUMAN
        pygame.display.set_caption("FlAIppy Birb - Human Mode")

    birb = Birb(WIDTH/4, HEIGHT * .75, DEBUG)

    birbs = [birb]

    main(birbs, CLEAR)