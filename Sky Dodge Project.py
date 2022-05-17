import random
import tsk
import pygame
pygame.init()

w = pygame.display.set_mode([1018, 573])

bg = tsk.Sprite("SkyScrolling.jpg", 0, 0)

c = pygame.time.Clock()

drs = tsk.ImageSheet("DragonFlying.png", 4, 6)
dragon = tsk.Sprite(drs, 0, 0)
drg_speed = 0.3

clouds = []
cloud_fnms = ["Cloud1.png", "Cloud2.png", "Cloud3.png"]
cld_timer = 0
cld_spn = 5000

cld_speed = 0.1

flm_sheet = tsk.ImageSheet("FireBlast.png", 4, 6)
flame = tsk.Sprite(flm_sheet, 100, 100)

flame_on = False

flm_on_timer = 0
flm_on_regulator = 0

balloons = []
bln_timer = 0
bln_spn = 7500

bln_speed = 0.2

distance = 0
score = 0

running = True
while running:
    bln_timer += c.get_time()
    cld_timer += c.get_time()
    distance += c.get_time()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flame_on = True
            if event.key == pygame.K_DOWN and dragon.y < (593 - 130):
                drg_speed = 10
            if event.key == pygame.K_UP and dragon.y > 0:
                drg_speed = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                flame_on = True
            drg_speed = 0
    dragon.y += drg_speed
    flame.y += drg_speed
    for cloud in clouds:
        if pygame.sprite.collide_rect(dragon, cloud):
            running = False
            break

    if flame_on:
        for i in balloons:
            if pygame.sprite.collide_rect(i, flame):
                balloons.remove(i)
                score += 1
    if cld_timer > cld_spn:
        cloud = tsk.Sprite(cloud_fnms[random.randint(0, 2)], 0, 0)
        cloud.x = 1018
        cloud.y = random.randint(0, 573-115)
        clouds.append(cloud)
        cld_speed += 0.01
        cld_timer = 0

    if bln_timer > bln_spn:
        bln_timer = 0
        bln = tsk.Sprite("Balloon.png", 0, 0)
        bln.y = random.randint(0, 573-164)
        bln.x = 1018
        balloons.append(bln)

    if flame_on:
        flm_on_regulator += c.get_time()
        if flm_on_regulator > 500:
            flm_on_regulator = 0
            flame_on = False

    if bg.center_x < 0:
        bg.center_x = 1018
    bg.center_x -= 0.1 * c.get_time()
    bg.draw()

    for i in clouds:
        i.x -= cld_speed * c.get_time()
        i.draw()
        if i.x < -223:
            clouds.remove(i)
    for i in balloons:
        i.x -= bln_speed * c.get_time()
        i.draw()
        if i.x < -102:
            balloons.remove(i)
    dragon.update(c.get_time())
    flame.update(c.get_time())
    dragon.draw()
    if flame_on:
        flame.draw()
    pygame.display.flip()

    c.tick(30)

print("Balloons popped: " + str(score))
print("Distance: " + str(distance/1000) + " meters")
