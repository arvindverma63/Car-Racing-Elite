import pygame
import time
from constants import WHITE, DARK_GRAY, GREEN, BLUE, RED

def draw_text(screen, text, font, color, x, y, center=False):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    if center:
        textrect.center = (x, y)
    else:
        textrect.topleft = (x, y)
    screen.blit(textobj, textrect)

def gradient_button(screen, text, font, x, y, w, h, base_color, hover_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    rect = pygame.Rect(x, y, w, h)
    color = hover_color if rect.collidepoint(mouse) else base_color
    
    surf = pygame.Surface((w, h))
    for i in range(h):
        alpha = int(255 * (i / h))
        pygame.draw.line(surf, (*color, alpha), (0, i), (w, i))
    pygame.draw.rect(surf, WHITE, (0, 0, w, h), 3, border_radius=15)
    screen.blit(surf, rect)
    
    draw_text(screen, text, font, WHITE, x + w//2, y + h//2, center=True)
    
    if rect.collidepoint(mouse) and click[0] == 1 and action:
        time.sleep(0.2)
        action()

def draw_hud(screen, score, font):
    hud = pygame.Surface((200, 80), pygame.SRCALPHA)
    pygame.draw.rect(hud, DARK_GRAY, (0, 0, 200, 80), border_radius=15)
    pygame.draw.arc(hud, GREEN, (20, 10, 60, 60), 0, score / 10 % 6.28, 5)  # Speedometer effect
    screen.blit(hud, (10, 10))
    draw_text(screen, f"Score: {score}", font, WHITE, 90, 30)