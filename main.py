#test
import asyncio
from random import randint
import pygame
import random

pygame.init()

pygame.display.set_caption("Alien Invasion")

screen_height = 800
screen_width = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

game_font = pygame.font.SysFont("Arial", 50)
score = pygame.font.SysFont("Arial-Bold", 20)
start_over = pygame.font.SysFont("Arial-Bold", 20)

fighter_image = pygame.image.load("images/warship.jpeg").convert_alpha()
alien_image = pygame.image.load("images/alien.png")
rocket_image = pygame.image.load("images/rocket.png")

fighter_width = fighter_image.get_width()
fighter_height = fighter_image.get_height()
fighter_x = screen_width / 2 - fighter_width
fighter_y = screen_height - fighter_height

alien_width = alien_image.get_width()
alien_height = alien_image.get_height()
alien_x = randint(0, screen_width - alien_width)
alien_y = 0
aliens = []

rocket_width = rocket_image.get_width()
rocket_height = rocket_image.get_height()
rocket_x = 400
rocket_y = 100

FIGHTER_STEP = 7
ROCKET_STEP = 9
ALIEN_STEP = 2
alien_speed = ALIEN_STEP

counter = 0
record = 0
btn_rect = pygame.Rect(screen_width / 2 - 55, screen_height / 2, 120, 45)


stars = []
for _ in range(65):
    stars.append([
        random.randrange(screen_width),
        random.randrange(screen_height),
        randint(1, 2)
    ])

alien_killed = False
rockets = []
clock = pygame.time.Clock()

game_over = False


async def main():
    global fighter_x, fighter_y, alien_x, alien_y, alien_speed, counter, game_over, rockets
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_over and btn_rect.collidepoint(event.pos):
                    game_over = False
                    alien_y = 0
                    alien_x = randint(0, screen_width - alien_width)
                    rockets.clear()
                    counter = 0
                    alien_speed = ALIEN_STEP

            if not game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        rockets.append([
                            fighter_x + fighter_width // 2 - rocket_width // 2,
                            fighter_y - rocket_height
                        ])

        if not game_over:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and fighter_x > 0:
                fighter_x -= FIGHTER_STEP
            if keys[pygame.K_RIGHT] and fighter_x < screen_width - fighter_width:
                fighter_x += FIGHTER_STEP

        screen.fill((0, 0, 0))
        screen.blit(fighter_image, (fighter_x, fighter_y))
        screen.blit(alien_image, (alien_x, alien_y))

        alien_y += alien_speed
        if alien_y + alien_height + fighter_height - 30 > screen_height:
            game_over = True

        for rocket in rockets[:]:
            rocket[1] -= ROCKET_STEP
            if (
                    alien_x < rocket[0] < alien_x + alien_width and
                    alien_y < rocket[1] < alien_y + alien_height
            ):
                rockets.remove(rocket)
                alien_y = 0
                alien_x = randint(0, screen_width - alien_width)
                alien_speed += .5
                counter += 1
                continue

            screen.blit(rocket_image, (rocket[0], rocket[1]))

        score_text = score.render("Score: " + str(counter), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        for star in stars:
            star[1] += 1

            if star[1] > screen_height:
                star[1] = 0
                star[0] = random.randrange(screen_width)

            pygame.draw.circle(screen, (255, 255, 255),
                               (star[0], star[1]), star[2])

        if game_over:
            game_over_text = game_font.render("ALIENS INVADED", True, "green")
            screen.blit(game_over_text, (screen_width // 2 - 200, screen_height // 2 - 100))

            pygame.draw.rect(screen, (0, 150, 255), btn_rect, border_radius=15)
            start_over_text = start_over.render("START OVER", True, (255, 255, 255))
            start_over_rect = start_over_text.get_rect(center=btn_rect.center)

            screen.blit(start_over_text, start_over_rect)
        else:
            screen.blit(fighter_image, (fighter_x, fighter_y))
            screen.blit(alien_image, (alien_x, alien_y))

        pygame.display.flip()
        await asyncio.sleep(0)  # ⬅️ ВАЖНО: отдаёт управление браузеру
        clock.tick(60)

asyncio.run(main())






# import asyncio
# from random import randint
# import pygame
# import random

# pygame.init()

# pygame.display.set_caption("Alien Invasion")

# screen_height = 800
# screen_width = 1000
# screen = pygame.display.set_mode((screen_width, screen_height))

# game_font = pygame.font.SysFont("Arial", 50)
# score = pygame.font.SysFont("Arial-Bold", 20)
# start_over = pygame.font.SysFont("Arial-Bold", 20)

# fighter_image = pygame.image.load("images/warship.jpeg").convert_alpha()
# alien_image = pygame.image.load("images/alien.png")
# rocket_image = pygame.image.load("images/rocket.png")

# fighter_width = fighter_image.get_width()
# fighter_height = fighter_image.get_height()
# fighter_x = screen_width / 2 - fighter_width
# fighter_y = screen_height - fighter_height

# alien_width = alien_image.get_width()
# alien_height = alien_image.get_height()
# alien_x = randint(0, screen_width - alien_width)
# alien_y = 0
# aliens = []

# rocket_width = rocket_image.get_width()
# rocket_height = rocket_image.get_height()
# rocket_x = 400
# rocket_y = 100

# FIGHTER_STEP = 7
# ROCKET_STEP = 9
# ALIEN_STEP = 2
# alien_speed = ALIEN_STEP

# counter = 0
# record = 0
# btn_rect = pygame.Rect(screen_width / 2 - 55, screen_height / 2, 120, 45)


# stars = []
# for _ in range(65):
#     stars.append([
#         random.randrange(screen_width),
#         random.randrange(screen_height),
#         randint(1, 2)
#     ])

# alien_killed = False
# rockets = []
# clock = pygame.time.Clock()

# game_over = False
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if game_over and btn_rect.collidepoint(event.pos):
#                 game_over = False
#                 alien_y = 0
#                 alien_x = randint(0, screen_width - alien_width)
#                 rockets.clear()
#                 counter = 0
#                 alien_speed = ALIEN_STEP

#         if not game_over:
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     rockets.append([
#                         fighter_x + fighter_width // 2 - rocket_width // 2,
#                         fighter_y - rocket_height
#                     ])

#     if not game_over:
#         keys = pygame.key.get_pressed()

#         if keys[pygame.K_LEFT] and fighter_x > 0:
#             fighter_x -= FIGHTER_STEP
#         if keys[pygame.K_RIGHT] and fighter_x < screen_width - fighter_width:
#             fighter_x += FIGHTER_STEP


#     screen.fill((0, 0, 0))
#     screen.blit(fighter_image, (fighter_x, fighter_y))

#     screen.blit(alien_image, (alien_x, alien_y))

#     alien_y += alien_speed
#     if alien_y + alien_height + fighter_height - 30 > screen_height:
#         game_over = True


#     for rocket in rockets[:]:
#         rocket[1] -= ROCKET_STEP
#         if (
#                 alien_x < rocket[0] < alien_x + alien_width and
#                 alien_y < rocket[1] < alien_y + alien_height
#         ):
#             rockets.remove(rocket)
#             alien_y = 0
#             alien_x = randint(0, screen_width - alien_width)
#             alien_speed += .5
#             counter += 1
#             counter += record
#             continue

#         screen.blit(rocket_image, (rocket[0], rocket[1]))

#     score_text = score.render("Score: " + str(counter), True, (255, 255, 255))
#     screen.blit(score_text, (10,10))

#     for star in stars:
#         star[1] += 1

#         if star[1] > screen_height:
#             star[1] = 0
#             star[0] = random.randrange(screen_width)

#         pygame.draw.circle(screen, (255, 255, 255),
#                            (star[0], star[1]), star[2])

#     if game_over:
#         game_over_text = game_font.render("ALIENS INVADED", True, "green")
#         screen.blit(game_over_text, (screen_width // 2 - 200, screen_height // 2 - 100))

#         pygame.draw.rect(screen, (0, 150, 255), btn_rect, border_radius=15)
#         start_over_text = start_over.render("START OVER", True, (255, 255, 255))
#         start_over_rect = start_over_text.get_rect(center=btn_rect.center)

#         screen.blit(start_over_text, start_over_rect)
#     else:
#         screen.blit(fighter_image, (fighter_x, fighter_y))
#         screen.blit(alien_image, (alien_x, alien_y))

#     pygame.display.flip()
#     clock.tick(60)

