import pygame

class Button:
    def __init__(self, x, y, width, height, button_color, hover_color, text, text_font, text_color, screen):
        self.rect = pygame.Rect(x, y, width, height)
        self.button_color = button_color
        self.hover_color = hover_color
        self.text = text
        self.font = text_font
        self.text_color = text_color
        self.screen = screen
        self.border_radius = 15

    # Function to draw text on the button
    def draw_text(self, text, font, text_color):
        # Render the text
        text_surface = font.render(text, True, text_color)

        # Get the rectangle of the rendered text surface
        text_rect = text_surface.get_rect()

        # Center the text rectangle on the button's rectangle
        text_rect.center = self.rect.center

        # Blit the text surface onto the screen
        self.screen.blit(text_surface, text_rect)

    def update_button_color(self):
        # Draw button rectangle with hover color
        pygame.draw.rect(self.screen, self.hover_color, self.rect, border_radius=self.border_radius)

        # Draw text on hover
        self.draw_text(self.text, self.font, self.text_color)

    def update_button(self):
        # Draw button rectangle with default color
        pygame.draw.rect(self.screen, self.button_color, self.rect, border_radius=self.border_radius)

        # Draw text on default
        self.draw_text(self.text, self.font, self.text_color)