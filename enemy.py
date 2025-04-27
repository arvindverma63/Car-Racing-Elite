import pygame
import random
from constants import WIDTH, HEIGHT, CAR_WIDTH, CAR_HEIGHT, RED, GREEN, ORANGE, ENEMY_SPEED
from player import create_car

class Enemy:
    def __init__(self):
        self.image = create_car(random.choice([RED, GREEN, ORANGE]))
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH - CAR_WIDTH), -CAR_HEIGHT))
    
    def move(self):
        self.rect.y += ENEMY_SPEED
        if self.rect.top > HEIGHT:
            return True
        return False
    
    def draw(self, screen):
        shadow = pygame.Surface((CAR_WIDTH + 10, CAR_HEIGHT + 10), pygame.SRCALPHA)
        pygame.draw.rect(shadow, (0, 0, 0, 80), (0, 0, CAR_WIDTH + 10, CAR_HEIGHT + 10), border_radius=10)
        screen.blit(shadow, (self.rect.x - 5, self.rect.y + 5))
        screen.blit(self.image, self.rect)