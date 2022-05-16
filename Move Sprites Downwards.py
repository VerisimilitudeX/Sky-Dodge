"""
LESSON: Sky Dodge Project
WARMUP 4
"""

import tsk
import random
import pygame
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("FantasyPlains.jpg", 0, 0)
first = tsk.Sprite("BoredCat.png", 500, -50)

rain = [first]
images = ["Cat.png", "BoredCat.png", "Pug.png"]

speed = .3
timer = 0

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    timer += c.get_time()
    if timer >= 500:
        timer = 0

        rand_index = random.randint(0, len(images) - 1)
        animal = tsk.Sprite(images[rand_index], random.randint(-50, 900), -100)
        rain.append(animal)

    # The rain falls down
    for rainsprite in rain:
        rainsprite.center_y += 5


    offscreen = []
    for animal in rain:
        if animal.y >= 600:
            offscreen.append(animal)

    for animal in offscreen:
        rain.remove(animal)

    background.draw()
    for animal in rain:
        animal.draw()

    pygame.display.flip()
    c.tick(30)