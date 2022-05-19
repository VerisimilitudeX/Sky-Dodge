"""
Sky Dodge Project
1. Make clouds travel at different speeds (using 2 lists, one list makes clouds go really fast, another really slow)
2. God mode with right arrow key (makes the sprite go faster)
3. Put a cooldown on the fire for 3 seconds
4. Make the fire shrink the clouds by 25% (easier to pass through areas with many clouds, need strategy)
"""

import random
import tsk
import pygame
pygame.init()

dash = 1
w = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("SkyScrolling.jpg", 0, 0)
c = pygame.time.Clock()

dragonsheet = tsk.ImageSheet("DragonFlying.png", 4, 6)
dragon = tsk.Sprite(dragonsheet, 0, 0)

dragon_speed = 0

clouds = []
cloud_fnms = ["Cloud1.png", "Cloud2.png", "Cloud3.png"]

cloud_timer = 0
cloud_spawn = 3800

cloud_speeds = []
cloud_range = 3

flame_sheet = tsk.ImageSheet("FireBlast.png", 4, 6)
flame = tsk.Sprite(flame_sheet, 100, 100)

flame_on = False

flame_on_timer = 0
flame_on_regulator = 0
flame_cooldown = 0

balloons = []
balloon_timer = 0
balloon_spawn = 7500

balloon_speed = 0.2

distance = 0

score = 0

running = True
while running:
    balloon_timer += c.get_time() * dash
    cloud_timer += c.get_time() * dash
    distance += c.get_time() * dash
    flame_cooldown += c.get_time() * dash

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flame_on = True
            elif event.key == pygame.K_DOWN and dragon.y < (573 - 130):
                dragon_speed = 0.3
            elif event.key == pygame.K_UP and dragon.y > 0:
                dragon_speed = -0.3
            if event.key == pygame.K_RIGHT:
                dash = 3
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                flame_on = True
            dragon_speed = 0
            if event.key == pygame.K_RIGHT:
                dash = 1

    dragon.y += dragon_speed * dash * c.get_time()
    flame.y += dragon_speed * dash * c.get_time()

    for cloud in clouds:
        if pygame.sprite.collide_rect(dragon, cloud):
            running = False
            break

    if flame_on and flame_cooldown > 3000:
        for i in balloons:
            if pygame.sprite.collide_rect(i, flame):
                balloons.remove(i)
                score += 1
                cloud_range += 0.01

    if cloud_timer > cloud_spawn:
        cloud = tsk.Sprite(cloud_fnms[random.randint(0, 2)], 0, 0)
        cloud.x = 1018
        cloud.y = random.randint(0, 573-115)
        clouds.append(cloud)
        cloud_speeds.append(random.randint(1, int(cloud_range))/10)
        cloud_range += 0.1
        cloud_timer = 0
        cloud_spawn = random.randint(2000, 3750)

    if balloon_timer > balloon_spawn:
        balloon_timer = 0
        balloon = tsk.Sprite("Balloon.png", 0, 0)
        balloon.y = random.randint(0, 573-164)
        balloon.x = 1018
        balloons.append(balloon)

    if flame_on:
        flame_on_timer += c.get_time()
        if flame_on_timer > 500:
            flame_on_timer = 0
            flame_on = False
            flame_cooldown = 0

    if background.center_x < 0:
        background.center_x = 1018
    background.center_x -= 0.1 * c.get_time() * dash
    background.draw()

    removeclouds = []
    removespeeds = []

    for i in range(len(clouds)):
        clouds[i].x -= cloud_speeds[i] * c.get_time() * dash
        clouds[i].draw()
        if clouds[i].x < -223:
            removeclouds.append(clouds[i])
            removespeeds.append(cloud_speeds[i])
        if flame_on and pygame.sprite.collide_rect(clouds[i], flame):
            clouds[i].scale = 0.25
            
    for i in removeclouds:
        clouds.remove(i)
    for i in removespeeds:
        cloud_speeds.remove(i)

    for i in balloons:
        i.x -= balloon_speed * c.get_time() * dash

        i.draw()
        if i.x < -102:
            balloons.remove(i)

    dragon.update(c.get_time() * dash)
    flame.update(c.get_time() * dash)

    dragon.draw()

    if flame_on and flame_cooldown > 3000:
        flame.draw()

    pygame.display.flip()

    c.tick(30)

print("Balloons popped: " + str(score))

print("Distance: " + str(distance/1000) + " meters")
