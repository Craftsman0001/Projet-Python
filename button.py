import pygame

class Button:
    def __init__(self, x, y, width, height, color, hover_color, text, font_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.default_color = color  # Couleur par défaut du bouton
        self.hover_color = hover_color
        self.text = text
        self.font = pygame.font.Font(None, font_size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_pressed(self, mouse_pos, mouse_pressed):
        return self.rect.collidepoint(mouse_pos) and mouse_pressed[0]

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def update_color(self, mouse_pos):
        if self.is_hovered(mouse_pos):
            self.color = self.hover_color
        else:
            self.color = self.default_color
