import random
import tsk
import pygame
pygame.init()

w = pygame.display.set_mode([1018, 573])

background = tsk.Sprite("SkyScrolling.jpg", 0, 0)

c = pygame.time.Clock()

dragonimagesheet = tsk.ImageSheet("DragonFlying.png", 4, 6)
dragon = tsk.Sprite(dragonimagesheet, 0, 0)
dragonspeed = 0.3

clouds = []
cloudfilenames = ["Cloud1.png", "Cloud2.png", "Cloud3.png"]
cloudtimer = 0
cloudspawn = 5000

cloudspeed = 0.1

flameimagesheet = tsk.ImageSheet("FireBlast.png", 4, 6)
flame = tsk.Sprite(flameimagesheet, 100, 100)

flame_on = False

flame_on_timer = 0
flame_on_regulator = 0

balloons = []
balloon_timer = 0
balloon_spn = 7500

balloon_speed = 0.2

distance = 0
score = 0

running = True
while running:
    balloon_timer += c.get_time()
    cloudtimer += c.get_time()
    distance += c.get_time()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flame_on = True
            if event.key == pygame.K_DOWN and dragon.y < (593 - 130):
                dragonspeed = 10
            if event.key == pygame.K_UP and dragon.y > 0:
                dragonspeed = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                flame_on = True
            dragonspeed = 0
    dragon.y += dragonspeed
    flame.y += dragonspeed
    for cloud in clouds:
        if pygame.sprite.collide_rect(dragon, cloud):
            running = False
            break

    if flame_on:
        for i in balloons:
            if pygame.sprite.collide_rect(i, flame):
                balloons.remove(i)
                score += 1
    if cloudtimer > cloudspawn:
        cloud = tsk.Sprite(cloudfilenames[random.randint(0, 2)], 0, 0)
        cloud.x = 1018
        cloud.y = random.randint(0, 573-115)
        clouds.append(cloud)
        cloudspeed += 0.01
        cloudtimer = 0

    if balloon_timer > balloon_spn:
        balloon_timer = 0
        balloon = tsk.Sprite("Balloon.png", 0, 0)
        balloon.y = random.randint(0, 573-164)
        balloon.x = 1018
        balloons.append(balloon)

    if flame_on:
        flame_on_regulator += c.get_time()
        if flame_on_regulator > 500:
            flame_on_regulator = 0
            flame_on = False
    for cloud in clouds:
        if pygame.sprite.collide_rect(flame, cloud):
            cloud.scale = 0.25
    if background.center_x < 0:
        background.center_x = 1018
    background.center_x -= 0.1 * c.get_time()
    background.draw()

    for i in clouds:
        i.x -= cloudspeed * c.get_time()
        i.draw()
        if i.x < -223:
            clouds.remove(i)
    for i in balloons:
        i.x -= balloon_speed * c.get_time()
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
