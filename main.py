import pygame
from birbpipe import Pipes
from birb import Birb

## game window dimensions
WIDTH, HEIGHT = 700, 450
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)

## window paras
FPS = 60

## game window name
pygame.display.set_caption("FlAIppy Birb")

pipe = Pipes(WIDTH, WIDTH)
pipe2 = Pipes(WIDTH + (WIDTH/2), WIDTH)
birb = Birb(WIDTH/2, HEIGHT/4)
birbs = [birb]

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
                    birb.flap()
        
        ##draw function
        draw()
            


    
    pygame.quit()


def draw():
    ## background colour
    WIN.fill((0, 200, 255))

    pipe.draw(WIN)
    pipe2.draw(WIN)

    birb.draw(WIN, [pipe, pipe2])

    if any(x.alive == True for x in birbs) == False:
        text = font.render("Game Over!", True, (255,255,255))
        WIN.blit(text, (WIDTH/2, HEIGHT/2))

    ## update window
    pygame.display.update()
    



if __name__ == "__main__":
    main();