import pygame
import random
from constants import GRAY

class TrailParticle:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.radius = random.randint(5, 10)
        self.life = 30
    
    def update(self):
        self.pos[1] += 2
        self.life -= 1
        self.radius = max(2, self.radius - 0.5)
        if self.life <= 0:
            return True
        return False
    
    def draw(self, screen):
        pygame.draw.circle(screen, GRAY, (int(self.pos[0]), int(self.pos[1])), int(self.radius), 1)