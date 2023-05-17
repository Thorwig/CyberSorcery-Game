import pygame
from pygame.sprite import AbstractGroup
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-15,-15)