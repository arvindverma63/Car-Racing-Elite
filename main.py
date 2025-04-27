import pygame
import random
from constants import WIDTH, HEIGHT, BLACK, START, PLAYING, GAME_OVER, ENEMY_FREQ, BLUE, GREEN, RED, WHITE, PLAYER_SPEED
from player import Player
from enemy import Enemy
from road import Road
from ui import draw_text, gradient_button, draw_hud

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Elite - Pygame")
clock = pygame.time.Clock()

# Initialize fonts
title_font = pygame.font.Font(None, 70)  # Replace with pygame.font.Font("Orbitron.ttf", 70)
ui_font = pygame.font.Font(None, 35)     # Replace with pygame.font.Font("Orbitron.ttf", 35)

class Game:
    def __init__(self):
        self.state = START
        self.transition_alpha = 0
        self.player = Player()
        self.enemies = []
        self.score = 0
        self.road = Road()
        self.running = True
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
            
            # Update road
            self.road.update()
            self.road.draw(screen)
            
            if self.state == START:
                draw_text(screen, "Car Racing Elite", title_font, WHITE, WIDTH//2, HEIGHT//2 - 100, center=True)
                draw_text(screen, "<- / -> to Move", ui_font, WHITE, WIDTH//2, HEIGHT - 100, center=True)
                
                gradient_button(screen, "Start", ui_font, WIDTH//2 - 150, HEIGHT//2 - 30, 300, 70, BLUE, GREEN, 
                                lambda: self.set_state(PLAYING, transition=True))
                gradient_button(screen, "Quit", ui_font, WIDTH//2 - 150, HEIGHT//2 + 60, 300, 70, BLUE, RED, 
                                lambda: self.quit_game())
            
            elif self.state == PLAYING:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.player.move(-PLAYER_SPEED)
                if keys[pygame.K_RIGHT]:
                    self.player.move(PLAYER_SPEED)
                
                if random.randint(1, ENEMY_FREQ) == 1:
                    self.enemies.append(Enemy())
                
                for enemy in self.enemies[:]:
                    if enemy.move():
                        self.enemies.remove(enemy)
                        self.score += 1
                    enemy.draw(screen)
                    if self.player.rect.colliderect(enemy.rect):
                        self.set_state(GAME_OVER, transition=True)
                
                self.player.draw(screen)
                draw_hud(screen, self.score, ui_font)
            
            elif self.state == GAME_OVER:
                draw_text(screen, "Game Over!", title_font, RED, WIDTH//2, HEIGHT//4, center=True)
                draw_text(screen, f"Score: {self.score}", ui_font, WHITE, WIDTH//2, HEIGHT//2 - 100, center=True)
                
                gradient_button(screen, "Restart", ui_font, WIDTH//2 - 150, HEIGHT//2 - 30, 300, 70, BLUE, GREEN, 
                                lambda: self.reset_game(PLAYING))
                gradient_button(screen, "Quit", ui_font, WIDTH//2 - 150, HEIGHT//2 + 60, 300, 70, BLUE, RED, 
                                lambda: self.quit_game())
            
            # Fade transition
            if self.transition_alpha > 0:
                fade = pygame.Surface((WIDTH, HEIGHT))
                fade.fill(BLACK)
                fade.set_alpha(self.transition_alpha)
                screen.blit(fade, (0, 0))
                self.transition_alpha = max(0, self.transition_alpha - 10)
            
            pygame.display.flip()
            clock.tick(60)
        
        pygame.quit()
    
    def set_state(self, new_state, transition=False):
        self.state = new_state
        if transition:
            self.transition_alpha = 255
    
    def reset_game(self, state):
        self.player = Player()
        self.enemies = []
        self.score = 0
        self.set_state(state, transition=True)
    
    def quit_game(self):
        self.running = False

if __name__ == "__main__":
    game = Game()
    game.run()