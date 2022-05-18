"""
LESSON: Sky Dodge Project
WARMUP 6
"""

import tsk
import pygame
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("AlienSpace.jpg", 0, 0)
star = tsk.Sprite("ShootingStar.png", 0, 0)

sheet = tsk.ImageSheet("RoundShipSpin.png", 5, 3)
ship = tsk.Sprite(sheet, 400, 250)
ship.image_animation_rate = 0

star_h_speed = .2
star_v_speed = .2

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Speed up the ship when the star hits it
    if pygame.sprite.collide_rect(star, ship):
        ship.image_animation_rate += 1

    star.x += star_h_speed * c.get_time()
    star.y += star_v_speed * c.get_time()

    if star.center_x < 0 or star.center_x > 1018:
        star_h_speed *= -1
        star.flip_x = not star.flip_x

    if star.center_y < 0 or star.center_y > 573:
        star_v_speed *= -1
        star.flip_y = not star.flip_y

    background.draw()
    star.draw()
    ship.draw()
    ship.update(c.get_time())

    pygame.display.flip()
    c.tick(30)
