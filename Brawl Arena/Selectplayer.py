import pygame
import sys
from button import Button
from FighterData import *
from fighter import Fighter
from RangedFighter import RangedFighter
from FighterData import load_spritesheets, load_animation_steps, fighter_variables

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
Knight_sprite_sheets = sprite_sheets["Knight"]
Huntress_sprite_sheets = sprite_sheets["Huntress"]

# Extract animation steps for each fighter
fantasy_warrior_animation_steps = animation_steps["fantasy_warrior"]
wizard_animation_steps = animation_steps["wizard"]
martial_hero_animation_steps = animation_steps["martial_hero"]
oni_samurai_animation_steps = animation_steps["oni_samurai"]
samurai_animation_steps = animation_steps["samurai"]
Squire_animation_steps = animation_steps["Squire"]
Knight_animation_steps = animation_steps["Knight"]
Huntress_animation_steps = animation_steps["Huntress"]

# defining fighter variables
fighter_data = fighter_variables()

fantasy_warrior_data = fighter_data["fantasy_warrior"]
wizard_data = fighter_data["wizard"]
martial_hero_data = fighter_data["martial_hero"]
oni_samurai_data = fighter_data["oni_samurai"]
samurai_data = fighter_data["samurai"]
Squire_data = fighter_data["Squire"]
Knight_data = fighter_data["Knight"]
Huntress_data = fighter_data["Huntress"]

projectiles = projectiles()

Huntress = projectiles["Huntress"]

# Colors
WHITE = (255, 255, 255)
BLACK_2 = (25, 25, 25)
AZURE_2 = (20, 150, 255)


def draw_text(text, font, text_color, x, y, screen):
    image = font.render(text, True, text_color)
    screen.blit(image, (x, y))


def select_player(screen, player_number):
    selecting_player = True
    main_menu_font = pygame.font.Font("Assets/Fonts/Turok.ttf", 60)
    screen.fill(BLACK_2)

    # Load selected images and scale them
    selected_FW = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/selected.png")
    selected_FW = pygame.transform.scale(selected_FW, (200, 200))
    selected_wizard = pygame.image.load("Assets/Fighters/EVil Wizard/Sprites/selected.png")
    selected_wizard = pygame.transform.scale(selected_wizard, (200, 200))
    selected_oni_Samurai = pygame.image.load("Assets/Fighters/Oni Samurai/Sprites/selected.png")
    selected_oni_Samurai = pygame.transform.scale(selected_oni_Samurai, (200, 200))
    selected_samurai = pygame.image.load("Assets/Fighters/Samurai/Sprites/selected.png")
    selected_samurai = pygame.transform.scale(selected_samurai, (200, 200))
    selected_MH = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/selected.png")
    selected_MH = pygame.transform.scale(selected_MH, (200, 200))
    selected_Squire = pygame.image.load("Assets/Fighters/Squire/Sprites/selected.png")
    selected_Squire = pygame.transform.scale(selected_Squire, (200, 200))
    selected_Knight = pygame.image.load("Assets/Fighters/Knight/Sprites/selected.png")
    selected_Knight = pygame.transform.scale(selected_Knight, (200, 200))
    selected_Huntress = pygame.image.load("Assets/Fighters/Huntress/Sprites/Character/selected.png")
    selected_Huntress = pygame.transform.scale(selected_Huntress, (200, 200))

    # Create instances of the Button class for each image
    selected_FW_button = Button(50, 100, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)
    selected_wizard_button = Button(275, 100, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)
    selected_oni_Samurai_button = Button(500, 100, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)
    selected_samurai_button = Button(725, 100, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)
    selected_MH_button = Button(950, 100, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)
    selected_Squire_button = Button(175, 333, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)
    selected_Knight_button = Button(400, 333, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)
    selected_Huntress_button = Button(625, 333, 200, 200, BLACK_2, AZURE_2, "", None, None, screen)

    # List of selected images and their corresponding buttons
    selected_images = [selected_FW, selected_wizard, selected_oni_Samurai, selected_samurai, selected_MH,
                       selected_Squire, selected_Knight, selected_Huntress]
    selected_buttons = [selected_FW_button, selected_wizard_button, selected_oni_Samurai_button,
                        selected_samurai_button, selected_MH_button, selected_Squire_button, selected_Knight_button,
                        selected_Huntress_button]

    # select loop

    while selecting_player:
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
                        elif i == 6:
                            return "Knight"
                        elif i == 7:
                            return "Huntress"

        # Draw selected images and buttons on the screen
        screen.fill(BLACK_2)
        for image, button in zip(selected_images, selected_buttons):
            # Draw a blue outline around the button
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (AZURE_2), button.rect, 3)
            # Draw image
            screen.blit(image, button.rect.topleft)

        # Draw text
        draw_text("Player " + player_number + " : Select your fighter", main_menu_font, WHITE, 250, 20, screen)
        pygame.display.flip()


def initialize_fighter(player_choice, player_number):
    third_attack = False  # Default value
    Ranged = False
    if player_choice == "Fantasy Warrior":
        player_data = fantasy_warrior_data
        player_sprite_sheet = fantasy_warrior_sprite_sheet
        player_animation_steps = fantasy_warrior_animation_steps
        third_attack = True  # Set to True for Fantasy Warrior

    elif player_choice == "Evil Wizard":
        player_data = wizard_data
        player_sprite_sheet = wizard_sprite_sheet
        player_animation_steps = wizard_animation_steps

    elif player_choice == "Oni Samurai":
        player_data = oni_samurai_data
        player_sprite_sheet = oni_samurai_sprite_sheets
        player_animation_steps = oni_samurai_animation_steps

    elif player_choice == "samurai":
        player_data = samurai_data
        player_sprite_sheet = samurai_sprite_sheets
        player_animation_steps = samurai_animation_steps

    elif player_choice == "martial hero":
        player_data = martial_hero_data
        player_sprite_sheet = martial_hero_sprite_sheets
        player_animation_steps = martial_hero_animation_steps
        third_attack = True  # Set to True for martial hero

    elif player_choice == "Squire":
        player_data = Squire_data
        player_sprite_sheet = Squire_sprite_sheets
        player_animation_steps = Squire_animation_steps
        third_attack = True

    elif player_choice == "Knight":
        player_data = Knight_data
        player_sprite_sheet = Knight_sprite_sheets
        player_animation_steps = Knight_animation_steps
        third_attack = False

    elif player_choice == "Huntress":
        player_data = Huntress_data
        player_sprite_sheet = Huntress_sprite_sheets
        player_animation_steps = Huntress_animation_steps
        projectile_sprite_sheet = Huntress[0]
        projectile_animation_steps = Huntress[1]
        third_attack = False
        Ranged = True

    if player_number == 1:
        global fighter_1
        if Ranged == False:
            fighter_1 = Fighter(1, 200, 400, 581, True, third_attack, player_data, player_sprite_sheet,
                                player_animation_steps)
        else:
            fighter_1 = RangedFighter(1, 200, 400, 581, True, third_attack, player_data, player_sprite_sheet,
                                      player_animation_steps, projectile_sprite_sheet, projectile_animation_steps)
        return fighter_1
    else:
        global fighter_2
        if Ranged == False:
            fighter_2 = Fighter(2, 925, 400, 581, False, third_attack, player_data, player_sprite_sheet,
                                player_animation_steps)
        else:
            fighter_2 = RangedFighter(2, 925, 400, 581, False, third_attack, player_data, player_sprite_sheet,
                                      player_animation_steps, projectile_sprite_sheet, projectile_animation_steps)
        return fighter_2