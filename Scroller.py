import random
import tsk
import pygame
pygame.init()

window = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("SkyScrolling.jpg", 0, 0)
c = pygame.time.Clock()

clouds = []
cloud_names = ["Cloud1.png", "Cloud2.png", "Cloud3.png"]
time_between_clouds = 3500
cloud_timer = 0
cloud_move_speed = .2

game_over = False
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    cloud_timer += c.get_time()
    if cloud_timer > time_between_clouds:

        random_index = random.randint(0, len(cloud_names) - 1)
        image = cloud_names[random_index]
        cloud = tsk.Sprite(image, 1020, random.randint(-10, 550))

        clouds.append(cloud)

        cloud_timer = 0
        time_between_clouds -= 50

    background.center_x -= .1 * c.get_time()
    if background.center_x <= 0:
        background.center_x = 1018

    for cloud in clouds:
        cloud.center_x -= cloud_move_speed * c.get_time()

    old_clouds = []

    for cloud in clouds:
        if cloud.center_x < -100:
            old_clouds.append(cloud)

    for cloud in old_clouds:
        clouds.remove(cloud)

    background.draw()

    for cloud in clouds:
        cloud.draw()

    pygame.display.flip()
    c.tick(30)

    if time_between_clouds < 750:
        time_between_clouds = 750
