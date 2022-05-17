import tsk
import pygame
pygame.init()

window = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("ScienceLabWithShrinkRay.jpg", 0, 0)
pug = tsk.Sprite("PugBee.png", 400, 250)

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    x, y = pygame.mouse.get_pos()

    if pug.rect.collidepoint(x, y):
        pug.scale = 3

    else:
        pug.scale = 0.5

    background.draw()
    pug.draw()

    pygame.display.flip()
