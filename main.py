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

# Extract animation steps for each fighter
fantasy_warrior_animation_steps = animation_steps["fantasy_warrior"]
wizard_animation_steps = animation_steps["wizard"]
martial_hero_animation_steps = animation_steps["martial_hero"]
oni_samurai_animation_steps = animation_steps["oni_samurai"]

# defining fighter variables
fighter_data = fighter_variables()

fantasy_warrior_data = fighter_data["fantasy_warrior"]
wizard_data = fighter_data["wizard"]
martial_hero_data = fighter_data["martial_hero"]
oni_samurai_data = fighter_data["oni_samurai"]

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

# defining game variables
countdown = 4
last_count_update = pygame.time.get_ticks()
score = [0, 0]  # player scores : [player1, player2]
round_over = False
ROUND_OVER_COOLDOWN = 3000
game_paused = False


# defining the font
countdown_font_1 = pygame.font.Font("Assets/Fonts/Turok.ttf", 200)
countdown_font_2 = pygame.font.Font("Assets/Fonts/Turok.ttf", 220)
score_font = pygame.font.Font("Assets/Fonts/Turok.ttf", 30)


# Creation of instances for fighters
fighter_1 = Fighter(1, 200, 400, 581, True, True, fantasy_warrior_data, fantasy_warrior_sprite_sheet,
                    fantasy_warrior_animation_steps)
## fighter_2 = Fighter(2, 925, 400, 581, False, True, martial_hero_data, martial_hero_sprite_sheets,
##                    martial_hero_animation_steps)
fighter_2 = Fighter(2, 925, 400, 581, False, False, oni_samurai_data, oni_samurai_sprite_sheets,
                    oni_samurai_animation_steps)


# function for displaying introduction video and wait for user to press space bar to continue
def display_intro_video() :
    clip = VideoFileClip("Assets/intro/intro.mp4")
    clip = clip.without_audio()  # disable audio track
    clip = clip.set_fps(60)

    # loop to display each frame of the video
    for frame in clip.iter_frames() :
        frame_surface = pygame.image.frombuffer(frame, clip.size, "RGB")
        screen.blit(frame_surface, (0, 0))
        pygame.display.update()

        # check if space bar is pressed to skip intro video
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    return

    # wait a certain time after the end of the video
    pygame.time.wait(100)

def reset_game() :
    global score, countdown, round_over, fighter_1, fighter_2
    score = [0, 0]
    countdown = 4
    round_over = False
    fighter_1.reset(238, 491)  # Reset fighter 1 position
    fighter_2.reset(963, 491)  # Reset fighter 2 position

    # Reset countdown timer
    last_count_update = pygame.time.get_ticks()



# Function to draw fighter health bars
def draw_health_bar(fighter, x, y) :
    ratio = fighter.health / 100
    pygame.draw.rect(screen, BLACK, (x - 5, y -5, 410, 40) )
    pygame.draw.rect(screen, BLUE, (x, y, 400, 30) )
    pygame.draw.rect(screen, GREEN, (x, y, 400 * ratio, 30) )


# function to draw text
def draw_text(text, font, text_color, x, y) :
    image = font.render(text, True, text_color)
    screen.blit(image, (x, y))

# function to have music
def manage_music(action, filepath=None, loops=-1, start=0.0):
    if action == "load":
        pygame.mixer.init()
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play(loops=loops, start=start)
    elif action == "play":
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(loops=loops, start=start)
    elif action == "pause":
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
    elif action == "unpause":
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
    elif action == "stop":
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
    else:
        print("Invalid action")


def smooth_attack_animation(fighter_1, fighter_2) :
    # Draw fighter
    if fighter_1.attacking == True :
        fighter_2.draw(screen)
        fighter_1.draw(screen)
    elif fighter_2.attacking == True :
        fighter_1.draw(screen)
        fighter_2.draw(screen)
    else :
        fighter_2.draw(screen)
        fighter_1.draw(screen)


# Define a function to display the pause menu
def display_pause_menu() :

    main_menu_font = pygame.font.Font("Assets/Fonts/Turok.ttf", 40)

    # create rectangles for the window and buttons
    window_rect = pygame.Rect(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80)

    # Create buttons
    resume_button = Button(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2 -100, SCREEN_WIDTH // 3, SCREEN_HEIGHT // 8, GREY_2, AZURE_2, "Resume", main_menu_font, BLACK, screen)
    restart_button = Button(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2 , SCREEN_WIDTH // 3, SCREEN_HEIGHT // 8, GREY_2, AZURE_2, "Restart", main_menu_font, BLACK, screen)
    exit_button = Button(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2 + 100, SCREEN_WIDTH // 3, SCREEN_HEIGHT // 8, GREY_2, AZURE_2, "Exit Game", main_menu_font, BLACK, screen)

    game_paused = True
    while game_paused == True :
        #pygame.mixer.music.pause()
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :  # Resume game on ESC key press
                    return "resume"

            elif event.type == pygame.MOUSEBUTTONDOWN :
                mouse_position = pygame.mouse.get_pos()
                if resume_button.rect.collidepoint(mouse_position) :
                    return "resume"

                elif restart_button.rect.collidepoint(mouse_position) :
                    return "restart"

                elif exit_button.rect.collidepoint(mouse_position) :
                    # Set flag to return to main menu
                    return "exit"



        # Draw a pause window/rectangle
        pygame.draw.rect(screen, BLACK_2, window_rect)

        # Draw buttons
        resume_button.update_button()
        restart_button.update_button()
        exit_button.update_button()

        # Highlight buttons if mouse hovers over them
        mouse_position = pygame.mouse.get_pos()
        if resume_button.rect.collidepoint(mouse_position) :
            resume_button.update_button_color()
        elif restart_button.rect.collidepoint(mouse_position) :
            restart_button.update_button_color()
        elif exit_button.rect.collidepoint(mouse_position) :
            exit_button.update_button_color()

        # Update display
        pygame.display.update()

    return None

# Define the intro_screen function
def intro_screen():

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
    
            elif event.type == pygame.MOUSEBUTTONDOWN :
                mouse_position = pygame.mouse.get_pos()
                if play_button.rect.collidepoint(mouse_position) :
                    # Play the game
                    intro = False

                elif exit_button.rect.collidepoint(mouse_position) :
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
        if play_button.rect.collidepoint(mouse_position) :
            play_button.update_button_color()
        elif exit_button.rect.collidepoint(mouse_position) :
            exit_button.update_button_color()

        # Update display
        pygame.display.update()

# call intro function
display_intro_video()

# Call the intro_screen function
intro_screen()

# Game Loop
clock = pygame.time.Clock() # Setting up framerate
run = True
while run :
    # load music's battle

    # Gestion des événements
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :  # Press ESC key
                game_paused = True  # Toggle pause state

    if game_paused:
        # Enter pause menu loop
        pause_action = display_pause_menu()
        if pause_action == "resume":
            game_paused = False
        elif pause_action == "restart":
            reset_game()
            game_paused = False
        elif pause_action == "exit":
            intro_screen()
            game_paused = False

    else :
        # Limit frame rate
        clock.tick(60)

        # Draw background Image
        screen.blit(background_image, (0, 0))

        # Displaying the players stats
        draw_health_bar(fighter_1, 20, 20)
        draw_health_bar(fighter_2, 780, 20)
        draw_text(" Player 1 : " + str(score[0]), score_font, BLACK, 10, 60)
        draw_text(" Player 2 : " + str(score[1]), score_font, BLACK, 770, 60)


        # update countdown
        if countdown <= 0 :
            # fighters can move
            fighter_1.move(round_over, SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
            fighter_2.move(round_over, SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1)
        else :
            # Ensure fighters face each other during countdown
            if fighter_2.rect.centerx > fighter_1.rect.centerx :
                fighter_2.flip = True
            else :
                fighter_2.flip = False
            # display the countdown timer
            if countdown == 1 :
                draw_text(str(countdown), countdown_font_2, BLACK, SCREEN_WIDTH / 2 - 20, SCREEN_HEIGHT / 3)
                draw_text(str(countdown), countdown_font_1, RED, SCREEN_WIDTH / 2 - 20, SCREEN_HEIGHT / 3)
            else :
                draw_text(str(countdown), countdown_font_2, BLACK, SCREEN_WIDTH / 2 - 40, SCREEN_HEIGHT / 3)
                draw_text(str(countdown), countdown_font_1, RED, SCREEN_WIDTH / 2 - 40, SCREEN_HEIGHT / 3)
            # update countdown
            if (pygame.time.get_ticks() - last_count_update) >= 1000 :
                countdown -= 1
                last_count_update = pygame.time.get_ticks()

        # update fighters
        fighter_2.update(fighter_1)
        fighter_1.update(fighter_2)

        smooth_attack_animation(fighter_1, fighter_2)

        # check if player was defeated
        if round_over == False :
            if fighter_1.alive == False :
                score[1] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
            elif fighter_2.alive == False :
                score[0] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
        else :
            # display the victory image
            screen.blit(victory_image, (400, 50))
            if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN :
                round_over = False
                countdown = 3
                # Creation of instances for fighters
                fighter_1 = Fighter(1, 200, 400, 581, True, True, fantasy_warrior_data, fantasy_warrior_sprite_sheet, fantasy_warrior_animation_steps)
                fighter_2 = Fighter(2, 925, 400, 581, False, True, martial_hero_data, martial_hero_sprite_sheets, martial_hero_animation_steps)

    # Update display
    pygame.display.update()

# Quitter le jeu et désinitialiser tous les modules pygame
pygame.mixer.music.stop()
pygame.quit()
sys.exit()
