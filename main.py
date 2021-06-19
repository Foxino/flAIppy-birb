import pygame
from birbpipe import Pipe
from birb import Birb

## game window dimensions
WIDTH, HEIGHT = 700, 450
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

## window paras
FPS = 60

## game window name
pygame.display.set_caption("FlAIppy Birb")

pipe = Pipe(WIDTH, WIDTH)
pipe2 = Pipe(WIDTH + (WIDTH/2), WIDTH)
birb = Birb(WIDTH/2, HEIGHT/4)

def main():
    gameRunning = True
    clock = pygame.time.Clock()

    ## game loop
    while gameRunning:
        clock.tick(FPS)

        ## window close event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    birb.addForce()
        
        ##draw function
        draw()

    
    pygame.quit()


def draw():
    ## background colour
    WIN.fill((0, 200, 255))

    pipe.draw(WIN)
    pipe2.draw(WIN)
    birb.draw(WIN)

    ## update window
    pygame.display.update()



if __name__ == "__main__":
    main();