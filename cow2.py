import pygame

pygame.init()

WIDTH = 700
HEIGHT = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BG = (67,143,229)
FPS = 60
clock = pygame.time.Clock()


posX = 20
posY = 20
speed = 15



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My name')
run_game = True
while run_game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game  = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                posY -= speed
            elif event.key == pygame.K_s:
                posY += speed
            elif event.key == pygame.K_a:
                posX -= speed
            elif event.key == pygame.K_d:
                posX += speed

    screen.fill(BG)


    pygame.draw.circle(screen, BLACK, (WIDTH/2, HEIGHT/2), 140)
    pygame.draw.circle(screen, WHITE, (WIDTH/2, HEIGHT/2), 120)
    pygame.draw.circle(screen, BLACK, (WIDTH/2, HEIGHT/2), 80)
    pygame.draw.circle(screen, WHITE, (WIDTH/2, HEIGHT/2), 40)
    pygame.draw.circle(screen, GREEN, (posX, posY), 15)
    pygame.display.flip()
pygame.quit()