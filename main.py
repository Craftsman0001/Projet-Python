import pygame
import sys
from moviepy.editor import VideoFileClip
from fighter import Fighter
from FighterData import *
from button import Button

# Initialize all imported pygame modules
pygame.init()

# Creation of the Game Window
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mon jeu !")

# Load background image and scale it to fit the screen
original_background_image = pygame.image.load("Assets/BackGrounds/trees.jpg")
background_image = pygame.transform.scale(original_background_image, (screen_width, screen_height))

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
GREEN = (0, 255, 0)
AZURE = (0, 100, 255)
AZURE_2 = (20, 150, 255)
AQUAMARINE = (0, 255, 100)
GREY = (128, 128, 128)
GREY_2 = (93, 93, 93)
GREY_3 = (58, 58, 58)
BLACK_2 = (16, 16, 16)

# defining game variables
countdown = 3
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
fighter_1 = Fighter(1, 200, 400, 581, True, False, fantasy_warrior_data, fantasy_warrior_sprite_sheet,
                    fantasy_warrior_animation_steps)
fighter_2 = Fighter(2, 925, 400, 581, False, True, martial_hero_data, martial_hero_sprite_sheets,
                    martial_hero_animation_steps)


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
def draw_text(num, text, font, text_color, x, y) :
    if num == 1 :
        image = font.render(text, True, text_color)
        screen.blit(image, (x, y))
    if num == 2 :
        text_surface = font.render(text, True, text_color)
        screen.blit(text_surface, (x, y))


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
    game_paused = True

    text_font = pygame.font.Font(None, 40)

    # create rectangles for the window and buttons
    window_rect = pygame.Rect(screen_width // 4, screen_height // 4, screen_width // 2, screen_height // 2 + 80)
    resume_button_rect = pygame.Rect(screen_width // 3, screen_height // 2 -100, screen_width // 3, screen_height // 8)
    restart_button_rect = pygame.Rect(screen_width // 3, screen_height // 2 , screen_width // 3, screen_height // 8)
    exit_button_rect = pygame.Rect(screen_width // 3, screen_height // 2 + 100, screen_width // 3, screen_height // 8)

    while game_paused == True :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :  # Resume game on ESC key press
                    game_paused = False
            elif event.type == pygame.MOUSEBUTTONDOWN :
                mouse_position = pygame.mouse.get_pos()
                if resume_button_rect.collidepoint(mouse_position) :
                    game_paused = False
                elif restart_button_rect.collidepoint(mouse_position) :
                    # Restart the game
                    reset_game()
                    game_paused = False
                elif exit_button_rect.collidepoint(mouse_position) :
                    # Close the game window
                    pygame.quit()
                    sys.exit()

        # Draw a pause window/rectangle
        pygame.draw.rect(screen, BLACK_2, window_rect)

        # Draw button rectangle
        pygame.draw.rect(screen, GREY_3, resume_button_rect)
        pygame.draw.rect(screen, GREY_3, restart_button_rect)
        pygame.draw.rect(screen, GREY_3, exit_button_rect)

        # Draw text
        draw_text(2, "Resume", text_font, BLACK, 550, 230)
        draw_text(2, "Restart", text_font, BLACK, 555, 330)
        draw_text(2, "Exit Game", text_font, BLACK, 533, 430)

        # Highlight buttons if mouse hovers over them
        mouse_position = pygame.mouse.get_pos()
        if resume_button_rect.collidepoint(mouse_position) :
            pygame.draw.rect(screen, AZURE, resume_button_rect)
            draw_text(2, "Resume", text_font, BLACK, 550, 230)
        elif restart_button_rect.collidepoint(mouse_position) :
            pygame.draw.rect(screen, AZURE, restart_button_rect)
            draw_text(2, "Restart", text_font, BLACK, 555, 330)
        elif exit_button_rect.collidepoint(mouse_position) :
            pygame.draw.rect(screen, AZURE, exit_button_rect)
            draw_text(2, "Exit Game", text_font, BLACK, 533, 430)

        pygame.display.update()

        return game_paused





# Define the intro_screen function
def intro_screen(startresume):
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    play_button = Button(screen_width // 2 - 100, 200, 200, 50, (50, 50, 50), AZURE_2, f"{startresume} Game", 32)
    exit_button = Button(screen_width // 2 - 100, 300, 200, 50, (50, 50, 50), AZURE_2, "Exit Game", 32)

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        title_font = pygame.font.Font(None, 64)
        title = title_font.render("Main Menu", True, (255, 255, 255))
        title_rect = title.get_rect(center=(screen_width // 2, 100))
        screen.blit(title, title_rect)

        play_button.update_color(pygame.mouse.get_pos())
        play_button.draw(screen)

        exit_button.update_color(pygame.mouse.get_pos())
        exit_button.draw(screen)

        mouse_pressed = pygame.mouse.get_pressed()
        if play_button.is_pressed(pygame.mouse.get_pos(), mouse_pressed):
            intro = False
        elif exit_button.is_pressed(pygame.mouse.get_pos(), mouse_pressed):
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        clock.tick(60)

# call intro function
display_intro_video()

# Call the intro_screen function
intro_screen("Start")

# Game Loop
clock = pygame.time.Clock() # Setting up framerate
run = True
while run :
    # Gestion des événements
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :  # Press ESC key
                game_paused = True  # Toggle pause state

    if game_paused == True :
        # Enter pause menu loop
        while game_paused :
            game_paused = display_pause_menu()  # Keep displaying pause menu until game is unpaused

    else :
        # Limit frame rate
        clock.tick(60)

        # Draw background Image
        screen.blit(background_image, (0, 0))

        # Displaying the players stats
        draw_health_bar(fighter_1, 20, 20)
        draw_health_bar(fighter_2, 780, 20)
        draw_text(1, " Player 1 : " + str(score[0]), score_font, BLACK, 10, 60)
        draw_text(1, " Player 2 : " + str(score[1]), score_font, BLACK, 770, 60)

        # update countdown
        if countdown <= 0 :
            # fighters can move
            fighter_1.move(round_over, screen_width, screen_height, screen, fighter_2)
            fighter_2.move(round_over, screen_width, screen_height, screen, fighter_1)
        else :
            # Ensure fighters face each other during countdown
            if fighter_2.rect.centerx > fighter_1.rect.centerx :
                fighter_2.flip = True
            else :
                fighter_2.flip = False
            # display the countdown timer
            if countdown == 1 :
                draw_text(1, str(countdown), countdown_font_2, BLACK, screen_width / 2 - 20, screen_height / 3)
                draw_text(1, str(countdown), countdown_font_1, RED, screen_width / 2 - 20, screen_height / 3)
            else :
                draw_text(1, str(countdown), countdown_font_2, BLACK, screen_width / 2 - 40, screen_height / 3)
                draw_text(1, str(countdown), countdown_font_1, RED, screen_width / 2 - 40, screen_height / 3)
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
pygame.quit()
sys.exit()
