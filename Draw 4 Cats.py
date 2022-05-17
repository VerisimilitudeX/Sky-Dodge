import tsk
import pygame
pygame.init()

window = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("CatRoom.jpg", 0, 0)
cats = []

for i in range(4):
    x = 50 + i * 250
    cat = tsk.Sprite("Cat.png", x, 200)
    cats.append(cat)
    
drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    background.draw()
    for cat in cats:
        cat.draw()

    pygame.display.flip()
