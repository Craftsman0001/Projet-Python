import pygame
import sys
from fighter import Fighter

# Initialize all imported pygame modules
pygame.init()

# Creation of the Game Window
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Its my game !")

# Load background image and scale it to fit the screen
original_background_image = pygame.image.load("Assets/BackGrounds/trees.jpg")
background_image = pygame.transform.scale(original_background_image, (screen_width, screen_height))

# load the victory image
original_victory_image = pygame.image.load("Assets/Images/victory_3.png")
victory_image = pygame.transform.scale(original_victory_image, (400,150))


def display_intro_video():
    clip = VideoFileClip("Assets/intro/intro.mp4")
    clip = clip.without_audio()  # Disable audio track
    clip = clip.set_fps(60) 
    clip.preview(screen_width, screen_height)



# Display the intro video
#display_intro_video()

# Loop until the player presses a key to start the game
#in_progress = False
#while not in_progress:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            in_progress = False
#        if event.type == pygame.KEYDOWN:
#            in_progress = True


# Load Spritesheets
idle_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Idle.png")
run_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Run.png")
jump_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Jump.png")
attack1_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Attack1.png")
attack2_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Attack2.png")
hit_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Take Hit.png")
death_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Death.png")
attack3_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Attack3.png")

idle_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Idle.png")
run_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Run.png")
jump_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Jump.png")
attack1_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Attack1.png")
attack2_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Attack2.png")
hit_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Take Hit.png")
death_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Death.png")

idle_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/Idle.png")
run_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/Run.png")
jump_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/Going Up.png")
attack1_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/Attack1.png")
attack2_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/Attack2.png")
hit_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/Take Hit.png")
death_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/Death.png")
attack3_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/Attack3.png")

martial_hero_sprite_sheets = [idle_martial_hero_sprite_sheet, run_martial_hero_sprite_sheet, jump_martial_hero_sprite_sheet, attack1_martial_hero_sprite_sheet, attack2_martial_hero_sprite_sheet, hit_martial_hero_sprite_sheet, death_martial_hero_sprite_sheet, attack3_martial_hero_sprite_sheet]

fantasy_warrior_sprite_sheet = [idle_fantasy_warrior_sprite_sheet, run_fantasy_warrior_sprite_sheet, jump_fantasy_warrior_sprite_sheet, attack1_fantasy_warrior_sprite_sheet, attack2_fantasy_warrior_sprite_sheet, hit_fantasy_warrior_sprite_sheet, death_fantasy_warrior_sprite_sheet, attack3_fantasy_warrior_sprite_sheet]

wizard_sprite_sheet = [idle_wizard_sprite_sheet, run_wizard_sprite_sheet, jump_wizard_sprite_sheet, attack1_wizard_sprite_sheet, attack2_wizard_sprite_sheet, hit_wizard_sprite_sheet, death_wizard_sprite_sheet] 

# Defining the numbers of steps relevant to the number of frames
idle_fantasy_warrior_animation_steps = [10]
run_fantasy_warrior_animation_steps = [8]
jump_fantasy_warrior_animation_steps = [3]
attack1_fantasy_warrior_animation_steps = [7]
attack2_fantasy_warrior_animation_steps = [7]
hit_fantasy_warrior_animation_steps = [3]
death_fantasy_warrior_animation_steps = [7]
attack3_fantasy_warrior_animation_steps = [8]

idle_wizard_animation_steps = [8]
run_wizard_animation_steps = [8]
jump_wizard_animation_steps = [2]
attack1_wizard_animation_steps = [8]
attack2_wizard_animation_steps = [8]
hit_wizard_animation_steps = [3]
death_wizard_animation_steps = [7]

idle_martial_hero_animation_steps = [10]
run_martial_hero_animation_steps = [8]
jump_martial_hero_animation_steps = [3]
attack1_martial_hero_animation_steps = [7]
attack2_martial_hero_animation_steps = [6]
hit_martial_hero_animation_steps = [3]
death_martial_hero_animation_steps = [11]
attack3_martial_hero_animation_steps = [9]

fantasy_warrior_animation_steps = [idle_fantasy_warrior_animation_steps, run_fantasy_warrior_animation_steps, jump_fantasy_warrior_animation_steps, attack1_fantasy_warrior_animation_steps, attack2_fantasy_warrior_animation_steps, hit_fantasy_warrior_animation_steps, death_fantasy_warrior_animation_steps, attack3_fantasy_warrior_animation_steps]
wizard_animation_steps = [idle_wizard_animation_steps, run_wizard_animation_steps, jump_wizard_animation_steps, attack1_wizard_animation_steps, attack2_wizard_animation_steps, hit_wizard_animation_steps, death_wizard_animation_steps]
martial_hero_animation_steps = [idle_martial_hero_animation_steps, run_martial_hero_animation_steps, jump_martial_hero_animation_steps, attack1_martial_hero_animation_steps, attack2_martial_hero_animation_steps, hit_martial_hero_animation_steps, death_fantasy_warrior_animation_steps, attack3_martial_hero_animation_steps]

# Defining fighter variables
fantasy_warrior_size = 162
fantasy_warrior_scale = 4
fantasy_warrior_offset = [72, 56]   
fantasy_warrior_data = [fantasy_warrior_size, fantasy_warrior_scale, fantasy_warrior_offset]
wizard_size = 250
wizard_scale = 3
wizard_offset = [112, 107]
wizard_data = [wizard_size, wizard_scale, wizard_offset]
martial_hero_size = 126
martial_hero_scale = 3.5
martial_hero_offset = [50, 30.5]
martial_hero_data = [martial_hero_size, martial_hero_scale, martial_hero_offset]

# Colors
Blue = (0, 0, 255)
Red = (255, 0, 0)
Yellow = (255, 255, 0)
White = (255, 255, 255)
Black = (0, 0, 0)
Green = (0, 255, 0)

# defining game variables
countdown = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0] # player scores : [player1, player2]
round_over = False
round_over_cooldown = 3000

# defining the font
countdown_font_1 = pygame.font.Font("Assets/Fonts/Turok.ttf", 200)
countdown_font_2 = pygame.font.Font("Assets/Fonts/Turok.ttf", 220)
score_font = pygame.font.Font("Assets/Fonts/Turok.ttf", 30)

# Creation of instances for fighters
fighter_1 = Fighter(1, 200, 400, 581, True, True, fantasy_warrior_data, fantasy_warrior_sprite_sheet, fantasy_warrior_animation_steps)
#fighter_2 = Fighter(2, 925, 400, 581, False, False, wizard_data, wizard_sprite_sheet, wizard_animation_steps)
fighter_2 = Fighter(2, 925, 400, 581, False, True, martial_hero_data, martial_hero_sprite_sheets, martial_hero_animation_steps)


# Function to draw fighter health bars
def draw_health_bar (fighter, x, y) :
    ratio = fighter.health / 100
    pygame.draw.rect(screen, Black, (x - 5, y -5, 410, 40) )
    pygame.draw.rect(screen, Blue, (x, y, 400, 30) )
    pygame.draw.rect(screen, Green, (x, y, 400 * ratio, 30) )
    

# function to draw text
def draw_text(text, font, text_color, x, y) :
    image = font.render(text, True, text_color)
    screen.blit(image, (x, y))


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



# Game Loop
clock = pygame.time.Clock() # Setting up framerate
run = True
while run :

    # Event Handler
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False

    # Limit frame rate
    clock.tick(60)
    
    # Draw background Image
    screen.blit(background_image, (0, 0))

    # Displaying the players stats
    draw_health_bar(fighter_1, 20, 20)
    draw_health_bar(fighter_2, 780, 20)
    draw_text(" Player 1 : " + str(score[0]), score_font, Black, 10, 60)
    draw_text(" Player 2 : " + str(score[1]), score_font, Black, 770, 60)

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
            draw_text(str(countdown), countdown_font_2, Black, screen_width / 2 - 20, screen_height / 3)
            draw_text(str(countdown), countdown_font_1, Red, screen_width / 2 - 20, screen_height / 3)
        else : 
            draw_text(str(countdown), countdown_font_2, Black, screen_width / 2 - 40, screen_height / 3)
            draw_text(str(countdown), countdown_font_1, Red, screen_width / 2 - 40, screen_height / 3)
        # update countdown
        if (pygame.time.get_ticks() - last_count_update) >= 1000 :
            countdown -=1
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
        if pygame.time.get_ticks() - round_over_time > round_over_cooldown :
            round_over = False
            countdown = 3
            # Creation of instances for fighters
            fighter_1 = Fighter(1, 200, 400, 581, True, True, fantasy_warrior_data, fantasy_warrior_sprite_sheet, fantasy_warrior_animation_steps)
            fighter_2 = Fighter(2, 925, 400, 581, False, False, wizard_data, wizard_sprite_sheet, wizard_animation_steps)

        
    # Update display
    pygame.display.update()


# Exiting the Game and uninitializing all pygame modules
pygame.quit()
sys.exit()