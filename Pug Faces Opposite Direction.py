"""
LESSON: Sky Dodge Project
WARMUP 5
"""

import tsk
import pygame
pygame.init()

window = pygame.display.set_mode([1018, 573])

background = tsk.Sprite("Stage.png", 0, 0)
pug = tsk.Sprite("PugBee.png", 400, 250)
pug.scale = 1.5

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            # If clicked, flip the sprite
            pug.flip_x = not pug.flip_x


    background.draw()
    pug.draw()

    pygame.display.flip()
