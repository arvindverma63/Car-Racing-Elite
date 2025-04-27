import pygame
import random
from constants import WIDTH, HEIGHT, BLUE, WHITE, DARK_GRAY, BLACK, CAR_WIDTH, CAR_HEIGHT, PLAYER_SPEED
from trail_particle import TrailParticle

def create_car(color, details=True):
    car = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
    pygame.draw.rect(car, color, (10, 20, CAR_WIDTH - 20, CAR_HEIGHT - 40), border_radius=10)
    if details:
        pygame.draw.circle(car, WHITE, (CAR_WIDTH//2, 20), 15)  # Headlight
        pygame.draw.rect(car, DARK_GRAY, (15, CAR_HEIGHT - 30, CAR_WIDTH - 30, 10))  # Spoiler
        pygame.draw.rect(car, BLACK, (15, 40, CAR_WIDTH - 30, 20))  # Window
    return car

class Player:
    def __init__(self):
        self.image = create_car(BLUE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 150))
        self.trails = []
    
    def move(self, dx):
        self.rect.x += dx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if random.randint(1, 5) == 1:  # Add trail randomly
            self.trails.append(TrailParticle(self.rect.centerx, self.rect.bottom))
    
    def draw(self, screen):
        # Shadow
        shadow = pygame.Surface((CAR_WIDTH + 10, CAR_HEIGHT + 10), pygame.SRCALPHA)
        pygame.draw.rect(shadow, (0, 0, 0, 100), (0, 0, CAR_WIDTH + 10, CAR_HEIGHT + 10), border_radius=10)
        screen.blit(shadow, (self.rect.x - 5, self.rect.y + 5))
        screen.blit(self.image, self.rect)
        for trail in self.trails[:]:
            if trail.update():
                self.trails.remove(trail)
            trail.draw(screen)