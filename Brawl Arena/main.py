import pygame
import sys
import random
from moviepy.editor import VideoFileClip
from fighter import Fighter
from button import *
from Selectplayer import *


# Initialize all imported pygame modules
pygame.init()

# Creation of the Game Window
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brawl Arena")

# Load background image and scale it to fit the screen
i = random.randint(0, 1)
image = BackGrounds()
background_image = pygame.transform.scale(image[i], (SCREEN_WIDTH, SCREEN_HEIGHT))

# load the victory image
original_victory_image = pygame.image.load("Assets/Images/victory_3.png")
victory_image = pygame.transform.scale(original_victory_image, (400, 150))

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
AZURE = (0, 100, 255)
AQUAMARINE = (0, 255, 100)
GREY = (128, 128, 128)
GREY_2 = (93, 93, 93)
GREY_3 = (50, 50, 50)
PURPLE = (200, 0, 255)
LIGHT_GOLD = (255, 255, 150)

# defining game variables
countdown = 4
last_count_update = pygame.time.get_ticks()
score = [0, 0]  # player scores : [player1, player2]
game_time = 120
round_over = False
ROUND_OVER_COOLDOWN = 3000
game_paused = False
player1_choice = None
player2_choice = None

# defining the font
countdown_font_1 = pygame.font.Font("Assets/Fonts/Turok.ttf", 200)
countdown_font_2 = pygame.font.Font("Assets/Fonts/Turok.ttf", 220)
score_font = pygame.font.Font("Assets/Fonts/Turok.ttf", 35)
Mana_maxed_font = pygame.font.Font("Assets/Fonts/Shock.ttf", 35)

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
    global score, countdown, round_over, fighter_1, fighter_2, last_count_update, game_time

    score = [0, 0]
    game_time = 120
    countdown = 4
    round_over = False
    fighter_1.reset(238, 491)  # Reset fighter 1 position
    fighter_2.reset(963, 491)  # Reset fighter 2 position

    # Reset countdown timer
    last_count_update = pygame.time.get_ticks()

# function to draw text
def draw_text( text, font, text_color, x, y):
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
    play_button = Button(SCREEN_WIDTH // 2 - 150, 200, 300, 75, GREY_2, AZURE_2, "Start Game", main_menu_font_2, BLACK, screen)
    exit_button = Button(SCREEN_WIDTH // 2 - 150, 300, 300, 75, GREY_2, AZURE_2, "Exit Game", main_menu_font_2, BLACK, screen)

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
                    global player1_choice, player2_choice, fighter_1, fighter_2
                    player1_choice = select_player(screen, "1")
                    player2_choice = select_player(screen, "2")
                    fighter_1 = initialize_fighter(player1_choice, 1)
                    fighter_2 = initialize_fighter(player2_choice, 2)

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
X = 15
Y = 500
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
            game_time = 120
            countdown = 4
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

        if fighter_1.mana == 50 :
            draw_text("MAX", Mana_maxed_font, WHITE, 85, 66)
        if fighter_2.mana == 50 :    
            draw_text("MAX", Mana_maxed_font, WHITE, 1045, 66)        

        pygame.draw.rect(screen, WHITE, (Y, X, 200, 50), border_radius=10)
        pygame.draw.rect(screen, BLACK_2, (Y, X, 50, 50), 5, border_radius=10)
        pygame.draw.rect(screen, BLACK_2, (Y + 150, X, 50, 50), 5, border_radius=10)
        pygame.draw.rect(screen, BLACK_2, (Y + 43, X, 114, 50))

        draw_text(str(game_time), score_font, WHITE, Y + 85, X + 5)

        if score[0]==1 or score[1]==1 :
            draw_text(str(score[0]), score_font, BLACK, Y + 20, X + 5)
            draw_text(str(score[1]), score_font, BLACK, Y + 171, X + 5)
        else :
            draw_text(str(score[0]), score_font, BLACK, Y + 17, X + 5)
            draw_text(str(score[1]), score_font, BLACK, Y + 168, X + 5)

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

        # when the countdown finishes start game clock
        if countdown == 0 :
            if (pygame.time.get_ticks() - last_count_update) >= 1000:
                game_time -= 1
                last_count_update = pygame.time.get_ticks()
        # when game clock finished verify who is the winner and reset accordingly
        if game_time == 0 :
            if fighter_2.health > fighter_1.health :
                score[1] += 1
            elif fighter_1.health > fighter_2.health :
                score[0] += 1
            elif fighter_1.health == fighter_2.health :
                score[1] = 0
                score[0] = 0
            countdown = 4
            game_time = 120
            fighter_1 = initialize_fighter(player1_choice, 1)
            fighter_2 = initialize_fighter(player2_choice, 2)

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
                game_time = 120
                fighter_1 = initialize_fighter(player1_choice, 1)
                fighter_2 = initialize_fighter(player2_choice, 2)


    # Update display
    pygame.display.update()

# Exit the game and uninitialize all pygame modules
pygame.mixer.music.stop()
pygame.quit()
sys.exit()