import pygame
import sys
from moviepy.editor import VideoFileClip
from fighter import Fighter
from FighterData import *
from button import *

# Initialize all imported pygame modules
pygame.init()

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
knight_sprite_sheets = sprite_sheets["Knight"]

# Extract animation steps for each fighter
fantasy_warrior_animation_steps = animation_steps["fantasy_warrior"]
wizard_animation_steps = animation_steps["wizard"]
martial_hero_animation_steps = animation_steps["martial_hero"]
oni_samurai_animation_steps = animation_steps["oni_samurai"]
samurai_animation_steps = animation_steps["samurai"]
Squire_animation_steps = animation_steps["Squire"]
knight_animation_steps = animation_steps["Knight"]

# defining fighter variables
fighter_data = fighter_variables()

fantasy_warrior_data = fighter_data["fantasy_warrior"]
wizard_data = fighter_data["wizard"]
martial_hero_data = fighter_data["martial_hero"]
oni_samurai_data = fighter_data["oni_samurai"]
samurai_data = fighter_data["samurai"]
Squire_data = fighter_data["Squire"]
knight_data = fighter_data["Knight"]

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

# defining game variables
countdown = 4
last_count_update = pygame.time.get_ticks()
score = [0, 0]  # player scores : [player1, player2]
round_over = False
ROUND_OVER_COOLDOWN = 3000
game_paused = False
player1_choice = None
player2_choice = None


# defining the font
countdown_font_1 = pygame.font.Font("Assets/Fonts/Turok.ttf", 200)
countdown_font_2 = pygame.font.Font("Assets/Fonts/Turok.ttf", 220)
score_font = pygame.font.Font("Assets/Fonts/Turok.ttf", 30)


# function for displaying introduction video and wait for user to press space bar to continue
def display_intro_video():
    clip = VideoFileClip("Assets/intro/intro.mp4")
    clip = clip.without_audio()  # disable audio track
    clip = clip.set_fps(60)

    # loop to display each frame of the video
    for frame in clip.iter_frames():
        frame_surface = pygame.image.frombuffer(frame, clip.size, "RGB")
        screen.blit(frame_surface, (0, 0))
        pygame.display.update()

        # check if space bar is pressed to skip intro video
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

    # wait a certain time after the end of the video
    pygame.time.wait(100)

def reset_game():
    global score, countdown, round_over, fighter_1, fighter_2, last_count_update

    score = [0, 0]
    countdown = 4
    round_over = False
    fighter_1.reset(238, 491)  # Reset fighter 1 position
    fighter_2.reset(963, 491)  # Reset fighter 2 position

    # Reset countdown timer
    last_count_update = pygame.time.get_ticks()

# function to draw text
def draw_text(text, font, text_color, x, y):
    image = font.render(text, True, text_color)
    screen.blit(image, (x, y))

def smooth_attack_animation(fighter_1, fighter_2):
    # Draw fighter
    if fighter_1.attacking == True:
        fighter_2.draw(screen)
        fighter_1.draw(screen)
    elif fighter_2.attacking == True:
        fighter_1.draw(screen)
        fighter_2.draw(screen)
    else:
        fighter_2.draw(screen)
        fighter_1.draw(screen)

def manage_music(action):
    if action == "play1":
        # Charger et jouer la musique en boucle indéfiniment (-1)
        pygame.mixer.music.load("Assets/musics/music_game_2.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.45)
    if action == "play2":
        # Charger et jouer la musique en boucle indéfiniment (-1)
        pygame.mixer.music.load("Assets/musics/music_game_1.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.45)
    elif action == "stop":
        # Arrêter la musique
        pygame.mixer.music.stop()

# Define a function to display the pause menu
def display_pause_menu():
    main_menu_font = pygame.font.Font("Assets/Fonts/Turok.ttf", 40)

    # create rectangles for the window and buttons
    window_rect = pygame.Rect(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80)

    # Create buttons
    resume_button = Button(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2 - 100, SCREEN_WIDTH // 3, SCREEN_HEIGHT // 8, GREY_2,
                           AZURE_2, "Resume", main_menu_font, BLACK, screen)
    restart_button = Button(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2, SCREEN_WIDTH // 3, SCREEN_HEIGHT // 8, GREY_2,
                            AZURE_2, "Restart", main_menu_font, BLACK, screen)
    exit_button = Button(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2 + 100, SCREEN_WIDTH // 3, SCREEN_HEIGHT // 8, GREY_2,
                         AZURE_2, "Main Menu", main_menu_font, BLACK, screen)

    game_paused = True
    while game_paused == True :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :  # Resume game on ESC key press
                    return "resume"

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if resume_button.rect.collidepoint(mouse_position) :
                    return "resume"

                elif restart_button.rect.collidepoint(mouse_position):
                    manage_music("stop")
                    manage_music("play1")
                    return "restart"

                elif exit_button.rect.collidepoint(mouse_position) :
                    # Set flag to return to main menu
                    manage_music("stop")
                    manage_music("play2")
                    return "Main menu"


        # Draw a pause window/rectangle
        pygame.draw.rect(screen, BLACK_2, window_rect)

        # Draw buttons
        resume_button.update_button()
        restart_button.update_button()
        exit_button.update_button()

        # Highlight buttons if mouse hovers over them
        mouse_position = pygame.mouse.get_pos()
        if resume_button.rect.collidepoint(mouse_position):
            resume_button.update_button_color()
        elif restart_button.rect.collidepoint(mouse_position):
            restart_button.update_button_color()
        elif exit_button.rect.collidepoint(mouse_position):
            exit_button.update_button_color()

        # Update display
        pygame.display.update()

    return None

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

# Define the intro_screen function
def intro_screen():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    manage_music("play2")
    # Load background image and scale it to fit the screen
    original_background_image = pygame.image.load("Assets/BackGrounds/Background_start_menu2.png")
    background_image = pygame.transform.scale(original_background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    ### main_menu_font = pygame.font.Font(None, 32)
    main_menu_font_1 = pygame.font.Font("Assets/Fonts/Turok.ttf", 80)
    main_menu_font_2 = pygame.font.Font("Assets/Fonts/Turok.ttf", 38)

    # Create buttons
    play_button = Button(SCREEN_WIDTH // 2 - 150, 200, 300, 75, GREY_2, AZURE_2, "Start Game", main_menu_font_2, BLACK,
                         screen)
    exit_button = Button(SCREEN_WIDTH // 2 - 150, 300, 300, 75, GREY_2, AZURE_2, "Exit Game", main_menu_font_2, BLACK,
                         screen)

    clock = pygame.time.Clock()
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if play_button.rect.collidepoint(mouse_position):
                    # Play the game
                    intro = False
                    global player1_choice, player2_choice
                    player1_choice = select_player_1()
                    player2_choice = select_player_2()

                    initialize_fighter_1(player1_choice)
                    initialize_fighter_2(player2_choice)
                    manage_music("play1")
                elif exit_button.rect.collidepoint(mouse_position):
                    # Close the game window
                    pygame.quit()
                    sys.exit()


        clock.tick(60)

        # Draw background Image
        screen.blit(original_background_image, (0, 0))

        # Draw text
        draw_text("Brawl Arena", main_menu_font_1, BLACK, SCREEN_WIDTH // 2 - 210, 70)
        draw_text("Brawl Arena", main_menu_font_1, AZURE_2, SCREEN_WIDTH // 2 - 220, 70)

        # Draw buttons
        play_button.update_button()
        exit_button.update_button()

        # Highlight buttons if mouse hovers over them
        mouse_position = pygame.mouse.get_pos()
        if play_button.rect.collidepoint(mouse_position):
            play_button.update_button_color()
        elif exit_button.rect.collidepoint(mouse_position):
            exit_button.update_button_color()

        # Update display
        pygame.display.update()

# call intro function
display_intro_video()

# Call the intro_screen function
intro_screen()

# Game Loop
clock = pygame.time.Clock()  # Setting up framerate
run = True
while run:

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Press ESC key
                game_paused = True  # Toggle pause state

    if game_paused == True:
        # Enter pause menu loop
        pause_action = display_pause_menu()
        if pause_action == "resume":
            game_paused = False
        elif pause_action == "restart":
            reset_game()
            game_paused = False
        elif pause_action == "Main menu":
            intro_screen()
            game_paused = False

    else:
        # Limit frame rate
        clock.tick(60)

        # Draw background Image
        screen.blit(background_image, (0, 0))

        # Displaying the players stats
        fighter_1.update_health(fighter_2, 20, 20, screen)
        fighter_2.update_health(fighter_1, 780, 20, screen)

        draw_text(" P1 : " + str(score[0]), score_font, BLACK, 430, 20)
        draw_text(" P2 : " + str(score[1]), score_font, BLACK, 695, 20)

        # update countdown
        if countdown <= 0:
            # fighters can move
            fighter_1.move(round_over, SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
            fighter_2.move(round_over, SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1)
        else:
            # Ensure fighters face each other during countdown
            if fighter_2.rect.centerx > fighter_1.rect.centerx:
                fighter_2.flip = True
            else:
                fighter_2.flip = False
            # display the countdown timer
            if countdown == 1:
                draw_text(str(countdown), countdown_font_2, BLACK, SCREEN_WIDTH / 2 - 20, SCREEN_HEIGHT / 3)
                draw_text(str(countdown), countdown_font_1, RED, SCREEN_WIDTH / 2 - 20, SCREEN_HEIGHT / 3)
            else:
                draw_text(str(countdown), countdown_font_2, BLACK, SCREEN_WIDTH / 2 - 40, SCREEN_HEIGHT / 3)
                draw_text(str(countdown), countdown_font_1, RED, SCREEN_WIDTH / 2 - 40, SCREEN_HEIGHT / 3)
            # update countdown
            if (pygame.time.get_ticks() - last_count_update) >= 1000:
                countdown -= 1
                last_count_update = pygame.time.get_ticks()

        # update fighters
        fighter_2.update(fighter_1)
        fighter_1.update(fighter_2)

        if round_over == False :
            fighter_1.add_mana(0.01)
            fighter_2.add_mana(0.01)

        smooth_attack_animation(fighter_1, fighter_2)

        # check if player was defeated
        if round_over == False:
            if fighter_1.alive == False:
                score[1] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
            elif fighter_2.alive == False:
                score[0] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
        else:
            # Display the victory image
            screen.blit(victory_image, (400, 50))
            # Reset the fighters based on player choices for round 2
            if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
                round_over = False
                countdown = 4
                initialize_fighter_2(player2_choice)
                initialize_fighter_1(player1_choice)


    # Update display
    pygame.display.update()

# Exit the game and uninitialize all pygame modules
pygame.mixer.music.stop()
pygame.quit()
sys.exit()

