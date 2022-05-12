"""
LESSON: Sky Dodge Project
"""

#### ---- LIBRARIES ---- ####

# E1: Import the random library


# B1: Import the tsk library
import tsk

# A1-A2: Import and set up pygame
import pygame
pygame.init()

#### ---- VARIABLES ---- ####

# --- Program variables --- #

# A3: Create a window of size [1018, 573]
window = pygame.display.set_mode([1018, 573])

# B2: Create a background sprite using "SkyScrolling.jpg"
background = tsk.Sprite("SkyScrolling.jpg", 0, 0)

# C1: Create a Clock
c = pygame.time.Clock()

# --- Dragon variables --- #

# D1-D2: Create a dragon sprite using the "DragonFlying.png"
# spritesheet with 4 rows and 6 columns
drs = tsk.ImageSheet("DragonFlying.png", 4, 6)
dragon = tsk.Sprite(drs, 0, 0)

# D3: Create a speed variable for the dragon's movement
dragonspeed = 0.3

# --- Cloud variables --- #

# E2-E3: Create an empty list to store clouds and a
# list of cloud filenames containing "Cloud1.png",
# "Cloud2.png" and "Cloud3.png"
clouds = []
filenames = ["Cloud1.png", "Cloud2.png", "Cloud2.png"]

# E4-E5: Create variables for the total time between
# cloud spawns and the time since the most recent spawn
cloudspawns = 0
recentspawn = 0

# F1: Create a speed for the clouds that's less than
# the dragon's speed
cloudspeed = 0.1

# --- Flame variables --- #

# I1-I2: Create a flame sprite using the "FireBlast.png"
# spritesheet with 4 rows and 6 columns. Start it
# offscreen above the top of the window.
flamesheet = tsk.ImageSheet("FireBlast.png", 4, 6)
flame = tsk.Sprite(flamesheet, 0, 0)

# I3: Create a variable to track whether the flame is
# on or off
flameonoroff = False

# J1-J2: Create variables for the time since the flame
# last turned on, and how long the flame should be on
timesinceflameturnedon = 0
howlongflameshouldbeon = 0

# --- Balloon variables --- #

# K1-K3: Create an empty list for the balloons and
# variables for the time between balloon spawns and
# the time since the last spawn
balloons = []
timebetweenballoonspawns = 0
timesincelastspawn = 0

# L1: Create a variable for the balloon's speed that's
# faster than the clouds but slower than the dragon
balloonspeed = 0.2

# --- Score variables --- #

# O1: Create a variable to track the distance traveled
distancetravelled = 0

# P1: Create a variable to track the score
score = 0

#### ---- MAIN LOOP ---- ####

# A4-A5: Create a main loop
running = True
while running:

    #### ---- EVENT LOOP ---- ####

    # A6-A8: Create an event loop
    # ---> TEST AFTER THESE LINES <--- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # --- Spacebar pressed --- #

        # I4-I5: If the user hit spacebar, create a new
        # fire sprite with the same variable and
        # ImageSheet as the first one, and put it in
        # front of the dragon
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flameonoroff = True

    #### ---- MOVE WITH ARROW KEYS ---- ####
    
    # D4-D7: If the up or down keys are held down and
    # the dragon isn't off the screen, move the dragon.
    # (Hint: use tsk.is_key_down())
    if tsk.is_key_down(pygame.K_UP):
        dragon.y -= dragonspeed
    if tsk.is_key_down(pygame.K_DOWN):
        dragon.y += dragonspeed

    #### ---- CHECK FOR COLLISIONS ---- ####

    # --- Dragon hits a cloud --- #

    # H1-H4: Go through every cloud in the list and see
    # if they collide with the dragon. If so, end the
    # main loop and don't check any more collisions.
    # ---> TEST AFTER THESE LINES <--- #
    for cloud in clouds:
        if pygame.sprite.collide_rect(dragon, cloud):
            running = False
            break





    # --- Flame hits a balloon --- #

    # N1: Create a new list for balloons to remove


    # N2-N4: Go through all the balloons and, if they
    # collide with the flame, add them to the new list




            # P2: Increment the score by 1


    # N5-N6: Go through the new list and remove
    # everything in it from the original balloons list
    # ---> TEST AFTER THESE LINES <--- #




    #### ---- SPAWN NEW SPRITES ---- ####

    # --- Spawn clouds --- #

    # E6: Track time in the time since last cloud
    # spawned variable


    # E7-E10: If enough time has passed since the last
    # cloud spawned that it's time to spawn a new one,
    # create a new cloud sprite using a random image
    # from the list of cloud filenames. Start it
    # offscreen on the right at a random height.





        # E11-E12: Put the cloud in the list of clouds
        # and re-set the time since last spawn timer
        # ---> TEST AFTER THESE LINES <--- #



        # Q1: Decrease the time between cloud spawns by
        # 50 milliseconds



    # --- Spawn balloons --- #

    # K4: Track the time since the last balloon
    # spawned.


    # K5-K6: If enough time has passed that it's time
    # to spawn a new balloon, create a new balloon
    # sprite with the image "Balloon.png" offscreen on
    # the right at a random height.



        # K7-K8: Put the balloon in the list of
        # balloons and re-set the time since last spawn
        # ---> TEST AFTER THESE LINES <--- #




    #### ---- STOP FLAME ---- ####

    # J3-J4: If the flame is on, keep track of how long
    # using the timer



        # J5-J8: If the flame has been on long enough,
        # set its status to off, re-set the timer, and
        # move the flame above the top of the screen
        # ---> TEST AFTER THESE LINES <--- #






    #### --- SCROLL SCREEN --- ####

    # --- Background --- #

    # C2-C4: Move the background to the left. If its
    # center reaches the left edge of the screen, set
    # it back to the right edge.





    # --- Clouds --- #

    # F2-F3: Move every cloud in the list to the left




    # --- Balloons --- #

    # L2-L3: Move every balloon in the list to the left




    #### ---- REMOVE OFF-SCREEN SPRITES ---- ####

     # --- Clouds --- #

    # G1: Create a list for the clouds to remove


    # G2-G4: Go through every cloud in the clouds list
    # and, if it's offscreen on the left, put it in the
    # new list




    # G5-G6: Go through the new list and remove
    # everything in it from the original clouds list
    # ---> TEST AFTER THESE LINES <--- #



    # --- Balloons --- #

    # M1: Create an list for the balloons to remove


    # M2-M4: Go through every balloon in the balloon
    # list and, if it's offscreen on the left, put it
    # in the new list




    # M5-M6: Go through the new list and remove
    # everything in it from the original balloons list
    # ---> TEST AFTER THESE LINES <--- #




    #### ---- DRAW FRAME ---- ####

    # B3: Draw the background
    background.draw()

    # F4-F5: Draw every cloud in the list
    # ---> TEST AFTER THESE LINES <--- #



    # L4-L5: Draw every balloon in the list
    # ---> TEST AFTER THESE LINES <--- #



    # D8-D9: Update and draw the dragon
    # ---> TEST AFTER THESE LINES <--- #



    # I7-I8: Update and draw the flame
    # ---> TEST AFTER THESE LINES <--- #


    # B4: Flip the display
    # ---> TEST AFTER THIS LINE <--- #
    pygame.display.flip()


    #### ---- TIME & SCORE ---- ####

    # C5: Tick the clock with 30 framerate
    # ---> TEST AFTER THIS LINE <--- #


    # O2: Increment the distance traveled by 1


    # Q2-Q3: Don't let the time between cloud spawns
    # become less than 750 milliseconds
    # ---> TEST AFTER THESE LINES <--- #




#### ---- FINAL SCORE ---- ####

# O3: Print the distance traveled / 100 as part of a
# message to the user
# ---> TEST AFTER THIS LINE <--- #


# P3: Print the score as part of a message to the user
# ---> TEST AFTER THIS LINE <--- #









