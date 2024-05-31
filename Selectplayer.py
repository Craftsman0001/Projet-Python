import pygame
import sys
from button import Button
from FighterData import *
from fighter import Fighter
from FighterData import load_spritesheets, load_animation_steps, fighter_variables

# Creation of the Game Window
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brawl Arena")

# Load background image and scale it to fit the screen
original_background_image = pygame.image.load("Assets/BackGrounds/trees.jpg")
background_image = pygame.transform.scale(original_background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# load the victory image
original_victory_image = pygame.image.load("Assets/Images/victory_3.png")
victory_image = pygame.transform.scale(original_victory_image, (400, 150))

# Load sprite sheets and animation steps
sprite_sheets = load_spritesheets()
animation_steps = load_animation_steps()

# Extract sprite sheets for each fighter
fantasy_warrior_sprite_sheet = sprite_sheets["fantasy_warrior"]
wizard_sprite_sheet = sprite_sheets["wizard"]
martial_hero_sprite_sheets = sprite_sheets["martial_hero"]
oni_samurai_sprite_sheets = sprite_sheets["oni_samurai"]
samurai_sprite_sheets = sprite_sheets["samurai"]
Squire_sprite_sheets = sprite_sheets["Squire"]
#knight_sprite_sheets = sprite_sheets["Knight"]

# Extract animation steps for each fighter
fantasy_warrior_animation_steps = animation_steps["fantasy_warrior"]
wizard_animation_steps = animation_steps["wizard"]
martial_hero_animation_steps = animation_steps["martial_hero"]
oni_samurai_animation_steps = animation_steps["oni_samurai"]
samurai_animation_steps = animation_steps["samurai"]
Squire_animation_steps = animation_steps["Squire"]
#knight_animation_steps = animation_steps["knight"]

# defining fighter variables
fighter_data = fighter_variables()

fantasy_warrior_data = fighter_data["fantasy_warrior"]
wizard_data = fighter_data["wizard"]
martial_hero_data = fighter_data["martial_hero"]
oni_samurai_data = fighter_data["oni_samurai"]
samurai_data = fighter_data["samurai"]
Squire_data = fighter_data["Squire"]
#knight_data = fighter_data["Knight"]

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLACK_2 = (25, 25, 25)
GREEN = (0, 255, 0)
AZURE = (0, 100, 255)
AZURE_2 = (20, 150, 255)
AQUAMARINE = (0, 255, 100)
GREY = (128, 128, 128)
GREY_2 = (93, 93, 93)
GREY_3 = (50, 50, 50)
PURPLE = (200, 0, 255)

def draw_text(text, font, text_color, x, y):
    image = font.render(text, True, text_color)
    screen.blit(image, (x, y))

def select_player_1() :
    selecting_player_1 = True
    main_menu_font_1 = pygame.font.Font("Assets/Fonts/Turok.ttf", 60)
    screen.fill(BLACK_2)

    # Load selected images and scale them
    selected_FW = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/selected.png")
    selected_FW = pygame.transform.scale(selected_FW, (200, 200))
    selected_wizard = pygame.image.load("Assets/Fighters/EVil Wizard/Sprites/selected.png")
    selected_wizard = pygame.transform.scale(selected_wizard, (200, 200))
    selected_Samurai = pygame.image.load("Assets/Fighters/Oni Samurai/Sprites/selected.png")
    selected_Samurai = pygame.transform.scale(selected_Samurai, (200, 200))
    selected_samurai = pygame.image.load("Assets/Fighters/Samurai/Sprites/selected.png")
    selected_samurai = pygame.transform.scale(selected_samurai, (200, 200))
    selected_MH = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/selected.png")
    selected_MH = pygame.transform.scale(selected_MH, (200, 200))
    selected_Squire = pygame.image.load("Assets/Fighters/Squire/Sprites/selected.png")
    selected_Squire = pygame.transform.scale(selected_Squire, (200, 200))

    # Create instances of the Button class for each image
    selected_FW_button = Button(50, 100, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)
    selected_wizard_button = Button(275, 100, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)
    selected_Samurai_button = Button(500, 100, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)
    selected_samurai_button = Button(725, 100, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)
    selected_MH_button = Button(950, 100, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)
    selected_Squire_button = Button(175, 333, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)



    # List of selected images and their corresponding buttons
    selected_images = [selected_FW, selected_wizard, selected_Samurai, selected_samurai, selected_MH, selected_Squire]
    selected_buttons = [selected_FW_button, selected_wizard_button, selected_Samurai_button, selected_samurai_button, selected_MH_button, selected_Squire_button]

    # select loop

    while selecting_player_1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, button in enumerate(selected_buttons):
                    if button.rect.collidepoint(event.pos):
                        if i == 0:
                            return "Fantasy Warrior"
                        elif i == 1:
                            return "Evil Wizard"
                        elif i == 2:
                            return "Oni Samurai"
                        elif i == 3:
                            return "samurai"
                        elif i == 4:
                            return "martial hero"
                        elif i == 5:
                            return "Squire"


        # Draw selected images and buttons on the screen
        screen.fill(BLACK_2)
        for image, button in zip(selected_images, selected_buttons):
            # Draw a blue outline around the button
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (AZURE_2), button.rect, 3)
            # Draw image
            screen.blit(image, button.rect.topleft)

        # Draw text
        draw_text("Player 1: Select your fighter", main_menu_font_1, WHITE, 250, 20)
        pygame.display.flip()

def initialize_fighter_1(player1_choice):
    THIRD_ATTACK = False  # Default value
    if player1_choice == "Fantasy Warrior":
        player1_data = fantasy_warrior_data
        player1_sprite_sheet = fantasy_warrior_sprite_sheet
        player1_animation_steps = fantasy_warrior_animation_steps
        THIRD_ATTACK = True  # Set to True for Fantasy Warrior

    elif player1_choice == "Evil Wizard":
        player1_data = wizard_data
        player1_sprite_sheet = wizard_sprite_sheet
        player1_animation_steps = wizard_animation_steps

    elif player1_choice == "Oni Samurai":
        player1_data = oni_samurai_data
        player1_sprite_sheet = oni_samurai_sprite_sheets
        player1_animation_steps = oni_samurai_animation_steps

    elif player1_choice == "samurai":
        player1_data = samurai_data
        player1_sprite_sheet = samurai_sprite_sheets
        player1_animation_steps = samurai_animation_steps

    elif player1_choice == "martial hero":
        player1_data = martial_hero_data
        player1_sprite_sheet = martial_hero_sprite_sheets
        player1_animation_steps = martial_hero_animation_steps
        THIRD_ATTACK = True  # Set to True for martial hero

    elif player1_choice == "Squire":
        player1_data = Squire_data
        player1_sprite_sheet = Squire_sprite_sheets
        player1_animation_steps = Squire_animation_steps
        THIRD_ATTACK = True



    global fighter_1
    fighter_1 = Fighter(1, 200, 400, 581, True, THIRD_ATTACK, player1_data, player1_sprite_sheet, player1_animation_steps)
    return fighter_1

def select_player_2():
    selecting_player_2 = True
    main_menu_font_1 = pygame.font.Font("Assets/Fonts/Turok.ttf", 60)
    screen.fill(BLACK_2)

    # Load selected images and scale them
    selected_FW = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/selected.png")
    selected_FW = pygame.transform.scale(selected_FW, (200, 200))
    selected_wizard = pygame.image.load("Assets/Fighters/EVil Wizard/Sprites/selected.png")
    selected_wizard = pygame.transform.scale(selected_wizard, (200, 200))
    selected_Samurai = pygame.image.load("Assets/Fighters/Oni Samurai/Sprites/selected.png")
    selected_Samurai = pygame.transform.scale(selected_Samurai, (200, 200))
    selected_samurai = pygame.image.load("Assets/Fighters/Samurai/Sprites/selected.png")
    selected_samurai = pygame.transform.scale(selected_samurai, (200, 200))
    selected_MH = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/selected.png")
    selected_MH = pygame.transform.scale(selected_MH, (200, 200))
    selected_Squire = pygame.image.load("Assets/Fighters/Squire/Sprites/selected.png")
    selected_Squire = pygame.transform.scale(selected_Squire, (200, 200))

    # Create instances of the Button class for each image
    selected_FW_button = Button(50, 100, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)
    selected_wizard_button = Button(275, 100, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)
    selected_Samurai_button = Button(500, 100, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)
    selected_samurai_button = Button(725, 100, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)
    selected_MH_button = Button(950, 100, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)
    selected_Squire_button = Button(175, 333, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)

    # List of selected images and their corresponding buttons
    selected_images = [selected_FW, selected_wizard, selected_Samurai, selected_samurai, selected_MH, selected_Squire]
    selected_buttons = [selected_FW_button, selected_wizard_button, selected_Samurai_button, selected_samurai_button, selected_MH_button, selected_Squire_button]

    # selected loop
    while selecting_player_2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for j, button in enumerate(selected_buttons):
                    if button.rect.collidepoint(event.pos):
                        if j == 0:
                            return "Fantasy Warrior"
                        elif j == 1:
                            return "Evil Wizard"
                        elif j == 2:
                            return "Oni Samurai"
                        elif j == 3:
                            return "samurai"
                        elif j == 4:
                            return "martial hero"
                        elif j == 5:
                            return "Squire"

        # Draw selected images and buttons on the screen
        screen.fill(BLACK_2)
        for image, button in zip(selected_images, selected_buttons):
            # Draw a blue outline around the button
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (AZURE_2), button.rect, 3)
            # Draw image
            screen.blit(image, button.rect.topleft)

        # Draw text
        draw_text("Player 2: Select your fighter", main_menu_font_1, WHITE, 250, 20)
        pygame.display.flip()

def initialize_fighter_2(player2_choice):
    THIRD_ATTACK = False
    if player2_choice == "Fantasy Warrior":
        player2_data = fantasy_warrior_data
        player2_sprite_sheet = fantasy_warrior_sprite_sheet
        player2_animation_steps = fantasy_warrior_animation_steps
        THIRD_ATTACK = True  # Set to True for martial hero

    elif player2_choice == "Evil Wizard":
        player2_data = wizard_data
        player2_sprite_sheet = wizard_sprite_sheet
        player2_animation_steps = wizard_animation_steps

    elif player2_choice == "Oni Samurai":
        player2_data = oni_samurai_data
        player2_sprite_sheet = oni_samurai_sprite_sheets
        player2_animation_steps = oni_samurai_animation_steps

    elif player2_choice == "samurai":
        player2_data = samurai_data
        player2_sprite_sheet = samurai_sprite_sheets
        player2_animation_steps = samurai_animation_steps

    elif player2_choice == "martial hero":
        player2_data = martial_hero_data
        player2_sprite_sheet = martial_hero_sprite_sheets
        player2_animation_steps = martial_hero_animation_steps
        THIRD_ATTACK = True

    elif player2_choice == "Squire":
        player2_data = Squire_data
        player2_sprite_sheet = Squire_sprite_sheets
        player2_animation_steps = Squire_animation_steps
        THIRD_ATTACK = True


    global fighter_2
    fighter_2 = Fighter(2, 925, 400, 581, False, THIRD_ATTACK, player2_data, player2_sprite_sheet, player2_animation_steps)
    return fighter_2

