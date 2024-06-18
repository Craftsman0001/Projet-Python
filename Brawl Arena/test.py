import pygame
from FighterData import load_idle_animation
# Colors
WHITE = (255, 255, 255)
BLACK_2 = (25, 25, 25)
AZURE_2 = (20, 150, 255)
idle_animations = {
    "Fantasy Warrior": load_idle_animation("Fantasy Warrior"),
    "Evil Wizard": load_idle_animation("Evil Wizard"),
    "Martial Hero": load_idle_animation("Martial Hero"),
    "Oni Samurai": load_idle_animation("Oni Samurai"),
    "Samurai": load_idle_animation("Samurai"),
    "Squire": load_idle_animation("Squire")}

def draw_text(text, font, text_color, x, y, screen):
    image = font.render(text, True, text_color)
    screen.blit(image, (x, y))

def idle_draw():
    #draw fantasy warrior
    THIRD_ATTACK = None
    player_data = idle_animations("Fantasy Warrior")
    player_sprite_sheet = idle_animations("Fantasy Warrior")
    player_animation_steps = idle_animations("Fantasy Warrior")

def select_player(screen, player_number):
    selecting_player = True
    main_menu_font = pygame.font.Font("Assets/Fonts/Turok.ttf", 60)
    screen.fill(BLACK_2)

    idle_draw(screen, 200, 400, "Fantasy Warrior")

    # Draw text
    draw_text("Player " + player_number + " : Select your fighter", main_menu_font, WHITE, 250, 20, screen)
    pygame.display.flip()