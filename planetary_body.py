import pygame, sys
from pygame.locals import *
import math

class Planet(pygame.sprite.Sprite):
    def __init__(self, planet_image, screen_width, screen_height, radius, relative_speed):
        super().__init__() 
        self.radius = radius
        self.speed = relative_speed
        self.image = pygame.image.load(planet_image)
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.rect.center=(self.x,self.y) 
        self.orbit_center = (screen_width/2, screen_height/2)
    
    def move(self, angle_deg):
        self.x = self.orbit_center[0] + math.cos(math.radians(angle_deg)) * self.radius
        self.y = self.orbit_center[1] + math.sin(math.radians(angle_deg)) * self.radius
        self.rect.center = (self.x, self.y)

    def draw(self, surface):
        surface.blit(self.image, self.rect) 

class Sun(pygame.sprite.Sprite):
    def __init__(self, sun_image, screen_width, screen_height):
        super().__init__() 
        self.image = pygame.image.load(sun_image)
        self.rect = self.image.get_rect()
        self.x = screen_width/2 
        self.y = screen_height/2
        self.rect.center=(self.x,self.y) 
        
    def draw(self, surface):
        surface.blit(self.image, self.rect) 

 

