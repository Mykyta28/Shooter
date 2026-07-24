import pygame

pygame.init()

set_with = 800
set_high = 600
screen = pygame.display.set_mode((set_with, set_high))
pygame.display.set_caption("My Game")

running = True
STEP = 10
radius = 50
x, y = set_with / 2, set_high / 2


while running:
    screen.fill((202, 135, 94))
    pygame.draw.circle(screen, (0, 255, 0), (x, y), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= STEP
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y += STEP

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= STEP
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x += STEP

        if x < radius:
             x = radius
        elif x > set_with - radius:
            x = set_with - radius

        if y < radius:
            y = radius
        elif y > set_high - radius:
            y = set_high - radius

    pygame.display.flip()

pygame.quit()