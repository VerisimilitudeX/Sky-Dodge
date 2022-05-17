"""
LESSON: Sky Dodge Project
EXERCISE: Flame Timer
"""

#### ---- LIBRARIES ---- ####

import pygame
pygame.init()


#### ---- VARIABLES ---- ####

window = pygame.display.set_mode([500, 500])
c = pygame.time.Clock()

circle_x = 250
circle_y = 250
flame = pygame.Rect(0, -100, 50, 50)

on = False
timer = 0
duration = 900


#### ---- MAIN LOOP ---- ####

game_over = False
while not game_over:


    #### ---- EVENT LOOP ---- ####

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


        #### ---- KEYS ---- ####

        if event.type == pygame.KEYDOWN:
            on = True
            timer = 0

            if event.key == pygame.K_RIGHT:
                flame.x = circle_x + 150
                flame.y = circle_y - 25

            elif event.key == pygame.K_LEFT:
                flame.x = circle_x - 200
                flame.y = circle_y - 25

            elif event.key == pygame.K_UP:
                flame.x = circle_x - 25
                flame.y = circle_y - 200

            elif event.key == pygame.K_DOWN:
                flame.x = circle_x - 25
                flame.y = circle_y + 150


    #### ---- STOP DRAWING ---- ####

    if on:
        timer += c.get_time()

        if timer >= duration:
            on = False
            timer = 0
            flame.y = -100


    #### ---- DRAW ---- ####

    window.fill((255, 255, 255))
    pygame.draw.circle(window, (0, 0, 255), (circle_x, circle_y), 50)
    pygame.draw.rect(window, (255, 0, 0), flame)
    pygame.display.flip()
    c.tick(30)
