"""
LESSON: Sky Dodge Project
"""

#### ---- LIBRARIES ---- ####

# E1:
import random
# B1:
import tsk
# A1-A2:
import pygame
pygame.init()

#### ---- VARIABLES ---- ####

# --- Program variables --- #

# A3:
w = pygame.display.set_mode([1018, 573])
# B2:
bg = tsk.Sprite("SkyScrolling.jpg", 0, 0)
# C1:
c = pygame.time.Clock()

# --- Dragon variables --- #

# D1-D2:
drs = tsk.ImageSheet("DragonFlying.png", 4, 6)
dragon = tsk.Sprite(drs, 0, 0)
# D3:
drg_speed = 0.3


# --- Cloud variables --- #

# E2-E3:
clouds = []
cloud_fnms = ["Cloud1.png", "Cloud2.png", "Cloud3.png"]
# E4-E5:
cld_timer = 0
cld_spn = 5000
# F1:
cld_speed = 0.1


# --- Flame variables --- #

# I1-I2:
flm_sheet = tsk.ImageSheet("FireBlast.png", 4, 6)
flame = tsk.Sprite(flm_sheet, 100, 100)
# I3:
flame_on = False
# J1-J2:
flm_on_timer = 0
flm_on_regulator = 0

# --- Balloon variables --- #

# K1-K3:
balloons = []
bln_timer = 0
bln_spn = 7500
# L1:
bln_speed = 0.2


# --- Score variables --- #

# O1:
distance = 0
# P1:
score = 0


#### ---- MAIN LOOP ---- ####

# A4-A5:
running = True
while running:
    bln_timer += c.get_time()
    cld_timer += c.get_time()
    distance += c.get_time()

    #### ---- EVENT LOOP ---- ####

    # A6-A8:
    for event in pygame.event.get():

        # --- Quit --- #
        if event.type == pygame.QUIT:
            running = False

        # --- Spacebar pressed --- #

        # I4-I5:
        if event.type == pygame.KEYDOWN:
            # I6:
            if event.key == pygame.K_SPACE:
                flame_on = True
            if event.key == pygame.K_DOWN and dragon.y < (593 - 130):
                drg_speed = 10
            if event.key == pygame.K_UP and dragon.y > 0:
                drg_speed = -10
        if event.type == pygame.KEYUP:
            # I6:
            if event.key == pygame.K_SPACE:
                flame_on = True
            drg_speed = 0
    #### ---- MOVE WITH ARROW KEYS ---- ####
   
    # D4-D7:
    dragon.y += drg_speed
    flame.y += drg_speed
    #### ---- CHECK FOR COLLISIONS ---- ####

    # --- Dragon hits a cloud --- #

    # H1-H4:
    for cloud in clouds:
        if pygame.sprite.collide_rect(dragon, cloud):
            running = False
            break

    # --- Flame hits a balloon --- #
    if flame_on:
        for i in balloons:
            if pygame.sprite.collide_rect(i, flame):
                balloons.remove(i)
                score += 1
    #### ---- SPAWN NEW SPRITES ---- ####

    # --- Spawn clouds --- #

    # E6:
    if cld_timer > cld_spn:
    # E7-E10:
        cloud = tsk.Sprite(cloud_fnms[random.randint(0, 2)], 0, 0)
        cloud.x = 1018
        cloud.y = random.randint(0, 573-115)
        # E11-E12:
        clouds.append(cloud)
        # Q1:
        cld_speed += 0.01
        cld_timer = 0

    # --- Spawn balloons --- #

    # K4:
    if bln_timer > bln_spn:
    # K5-K6:
        bln_timer = 0
        # K7-K8:
        bln = tsk.Sprite("Balloon.png", 0, 0)
        bln.y = random.randint(0, 573-164)
        bln.x = 1018
        balloons.append(bln)


    #### ---- STOP FLAME ---- ####

    # J3-J4:
    if flame_on:
        # J5-J8:
        flm_on_regulator += c.get_time()
        if flm_on_regulator > 500:
            flm_on_regulator = 0
            flame_on = False

    #### --- SCROLL SCREEN --- ####

    # --- Background --- #

    # C2-C4:
    if bg.center_x < 0:
        bg.center_x = 1018
    bg.center_x -= 0.1 * c.get_time()
    bg.draw()

    # --- Clouds --- #

    # F2-F3:
    for i in clouds:
        i.x -= cld_speed * c.get_time()
        i.draw()
        if i.x < -223:
    # G2-G4:
            clouds.remove(i)
    # --- Balloons --- #

    # L2-L3:
    for i in balloons:
        i.x -= bln_speed * c.get_time()


    #### ---- REMOVE OFF-SCREEN SPRITES ---- ####

     # --- Clouds --- #
        i.draw()
    # G1:
        if i.x < -102:
    # G2-G4:
            balloons.remove(i)
    # G5-G6:



    # --- Balloons --- #

    # M1:

    # M2-M4:

    # M5-M6:


    #### ---- DRAW FRAME ---- ####
    dragon.update(c.get_time())
    flame.update(c.get_time())
    # B3:
   
    # F4-F5:
   
    # L4-L5:

    # D8-D9:
    dragon.draw()
    # I7-I8:
    if flame_on:
        flame.draw()
    # B4:
    pygame.display.flip()


    #### ---- TIME & SCORE ---- ####

    # C5:

    # O2:

    # Q2-Q3:
    c.tick(30)


#### ---- FINAL SCORE ---- ####

# O3:
print("Balloons popped: " + str(score))
# P3:
print("Distance: " + str(distance/1000) + " meters")
