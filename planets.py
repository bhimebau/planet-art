import pygame, sys
from pygame.locals import *
import random
from planetary_body import Planet, Sun
 
pygame.init()
 
FPS = 30
FramePerSec = pygame.time.Clock()
 
# Predefined some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Screen information
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Planet Art")

# Instantiate the Object Sprites
mars = Planet("mars.png",SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_WIDTH/2-20,1) 
earth = Planet("earth.png",SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_WIDTH/4,1) 
sun = Sun("sun.png",SCREEN_WIDTH,SCREEN_HEIGHT)
       
# Starting angles for the different planets, the sun will be in the center
mars_angle = 0
earth_angle = 65

# Empty list to hold the lines between the planets
lines = []

# Game Loop 
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # If the key is the "c", then empty the line list to clear it 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                lines = []

    # move the planets based on their new angle, the orbits are unrealistically circular:) 
    mars.move(mars_angle)
    earth.move(earth_angle)

    # Erase everything from the screen
    DISPLAYSURF.fill(WHITE)
    
    # Append the current line between earth and mars to the line list
    lines.append((earth.x,earth.y,mars.x,mars.y))   

    # Draw all of the lines in the list
    for line in lines:
        pygame.draw.aaline(DISPLAYSURF,BLACK,(line[0],line[1]),(line[2],line[3]))
        
    # Add all of the planetary objects, this will write them on top of the lines
    mars.draw(DISPLAYSURF)
    earth.draw(DISPLAYSURF)
    sun.draw(DISPLAYSURF)

    # Write the updated game surface to the screen
    pygame.display.update()

    # Control the framerate to FPS specified above
    FramePerSec.tick(FPS)

    # Increment the angles and wrap them to 360 degrees, the angle increments are not realistic
    # they were chosen to generate a nice looking rose pattern. 
    mars_angle += 3.4
    if mars_angle > 359:
        mars_angle = 0
    earth_angle += 1.25
    if earth_angle > 359:
        earth_angle = 0

    
