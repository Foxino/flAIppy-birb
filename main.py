import pygame
from birbpipe import Pipes
from birb import Birb
from qbot import QBot
import argparse


## game window dimensions
WIDTH, HEIGHT = 700, 450
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

def main(birbs):
    gameRunning = True
    clock = pygame.time.Clock()

    ## in AI mode, creates the bot and attaches the agent to it.
    if MODE == MODE_AI:
        bot = QBot()
        bot.addAgent(birbs[0])

    ## game loop
    while gameRunning:
        clock.tick(FPS)

        ## window close event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False
            if event.type == pygame.KEYDOWN and MODE != MODE_AI:
                if event.key == pygame.K_SPACE:
                    birbs[0].flap()

        ## in AI mode, checks for action
        if MODE == MODE_AI:
            fl = bot.action()
            if fl == 1:
                bot.birb.flap()

        
        ##draw function
        draw(birbs)
            
        if MODE == MODE_AI:
            print("@?")
    
    pygame.quit()


def draw(birbs):
    ## background colour
    WIN.fill((0, 200, 255))

    for pipe in pipes:
        pipe.draw(WIN)

    for birb in birbs:
        birb.draw(WIN, pipes)

    if any(x.alive == True for x in birbs) == False:
        text = font.render("Game Over!", True, (255,255,255))
        WIN.blit(text, (WIDTH/2, HEIGHT/2))

    ## update window
    pygame.display.update()
    

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--bot', '-b', action='store_true', help='Run with bot.')
    parser.add_argument('--showdebug', '-d', action='store_true', help='Show debug info')

    args = parser.parse_args()

    DEBUG = args.showdebug

    if args.bot == True:
        MODE = MODE_AI
        pygame.display.set_caption("FlAIppy Birb - AI Mode")
    else:
        MODE = MODE_HUMAN
        pygame.display.set_caption("FlAIppy Birb - Human Mode")

    birb = Birb(WIDTH/2, HEIGHT/4, DEBUG)

    birbs = [birb]

    main(birbs)