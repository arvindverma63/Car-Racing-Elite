import pygame
from constants import WIDTH, HEIGHT, GRAY, YELLOW, WHITE, ROAD_SPEED

class Road:
    def __init__(self):
        self.surface = pygame.Surface((WIDTH, HEIGHT * 2))
        self.surface.fill(GRAY)
        for y in range(0, HEIGHT * 2, 40):
            pygame.draw.rect(self.surface, YELLOW, (WIDTH//4 - 10, y, 20, 20))  # Left lane line
            pygame.draw.rect(self.surface, YELLOW, (3 * WIDTH//4 - 10, y, 20, 20))  # Right lane line
            pygame.draw.rect(self.surface, WHITE, (WIDTH//2 - 5, y, 10, 20))  # Center line
        self.pos = 0
    
    def update(self):
        self.pos = (self.pos + ROAD_SPEED) % (HEIGHT * 2)
    
    def draw(self, screen):
        screen.blit(self.surface, (0, self.pos - HEIGHT * 2))
        screen.blit(self.surface, (0, self.pos))