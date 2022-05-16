"""
LESSON: Sky Dodge Project
EXERCISE: Scroller
"""

# Place the comments below in the numbered locations
# based on the code that they describe. You will use
# each comment exactly once.















import random
import tsk
import pygame
pygame.init()


# 1:# Program variables
window = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("SkyScrolling.jpg", 0, 0)
c = pygame.time.Clock()


# 2:# Clouds have a max spawn speed
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

        # 3:# Draw clouds
        random_index = random.randint(0, len(cloud_names) - 1)
        image = cloud_names[random_index]
        cloud = tsk.Sprite(image, 1020, random.randint(-10, 550))

        # 4:# Track clouds
        clouds.append(cloud)

        # 5:# Move clouds
        cloud_timer = 0
        time_between_clouds -= 50


    # 6:# Random cloud
    background.center_x -= .1 * c.get_time()
    if background.center_x <= 0:
        background.center_x = 1018

    # 7:# Draw background
    for cloud in clouds:
        cloud.center_x -= cloud_move_speed * c.get_time()


    old_clouds = []

    # 8:# Remove
    for cloud in clouds:
        if cloud.center_x < -100:
            old_clouds.append(cloud)

    # 9:# Cloud variables
    for cloud in old_clouds:
        clouds.remove(cloud)


    # 10:# Move background
    background.draw()

    # 11:# Mark for removal
    for cloud in clouds:
        cloud.draw()

    pygame.display.flip()
    c.tick(30)

    # 12:# Set new timing
    if time_between_clouds < 750:
        time_between_clouds = 750
