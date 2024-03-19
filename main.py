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
original_background = pygame.image.load("Assets/BackGrounds/trees.jpg")
background_image = pygame.transform.scale(original_background, (screen_width, screen_height))

# Load Spritesheets
idle_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Idle.png")
run_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Run.png")
jump_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Jump.png")
attack1_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Attack1.png")
attack2_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Attack2.png")
hit_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Take Hit.png")
death_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Death.png")

idle_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Idle.png")
run_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Run.png")
jump_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Jump.png")
attack1_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Attack1.png")
attack2_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Attack2.png")
hit_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Take Hit.png")
death_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Death.png")

fantasy_warrior_sprite_sheet = [idle_fantasy_warrior_sprite_sheet, run_fantasy_warrior_sprite_sheet, jump_fantasy_warrior_sprite_sheet, attack1_fantasy_warrior_sprite_sheet, attack2_fantasy_warrior_sprite_sheet, hit_fantasy_warrior_sprite_sheet, death_fantasy_warrior_sprite_sheet]

wizard_sprite_sheet = [idle_wizard_sprite_sheet, run_wizard_sprite_sheet, jump_wizard_sprite_sheet, attack1_wizard_sprite_sheet, attack2_wizard_sprite_sheet, hit_wizard_sprite_sheet, death_wizard_sprite_sheet] 

# Defining the numbers of steps relevant to the number of frames
idle_fantasy_warrior_animation_steps = [10]
run_fantasy_warrior_animation_steps = [8]
jump_fantasy_warrior_animation_steps = [3]
attack1_fantasy_warrior_animation_steps = [7]
attack2_fantasy_warrior_animation_steps = [7]
hit_fantasy_warrior_animation_steps = [3]
death_fantasy_warrior_animation_steps = [7]

idle_wizard_animation_steps = [8]
run_wizard_animation_steps = [8]
jump_wizard_animation_steps = [2]
attack1_wizard_animation_steps = [8]
attack2_wizard_animation_steps = [8]
hit_wizard_animation_steps = [3]
death_wizard_animation_steps = [7]

fantasy_warrior_animation_steps = [idle_fantasy_warrior_animation_steps, run_fantasy_warrior_animation_steps, jump_fantasy_warrior_animation_steps, attack1_fantasy_warrior_animation_steps, attack2_fantasy_warrior_animation_steps, hit_fantasy_warrior_animation_steps, death_fantasy_warrior_animation_steps]
wizard_animation_steps = [idle_wizard_animation_steps, run_wizard_animation_steps, jump_wizard_animation_steps, attack1_wizard_animation_steps, attack2_wizard_animation_steps, hit_wizard_animation_steps, death_wizard_animation_steps]

# Defining fighter variables
fantasy_warrior_size = 162
fantasy_warrior_scale = 4
fantasy_warrior_offset = [72, 56]
fantasy_warrior_data = [fantasy_warrior_size, fantasy_warrior_scale, fantasy_warrior_offset]
wizard_size = 250
wizard_scale = 3
wizard_offset = [112, 107]
wizard_data = [wizard_size, wizard_scale, wizard_offset]

# Colors
Blue = (0, 0, 255)
Red = (255, 0, 0)
Yellow = (255, 255, 0)
White = (255, 255, 255)

# Creation of instances for fighters
fighter_1 = Fighter(200, 400, 581, True, fantasy_warrior_data, fantasy_warrior_sprite_sheet, fantasy_warrior_animation_steps)
fighter_2 = Fighter(925, 400, 581, False, wizard_data, wizard_sprite_sheet, wizard_animation_steps)

# Function to draw fighter health bars
def draw_health_bar (fighter, x, y) :
    ratio = fighter.health / 100
    pygame.draw.rect(screen, White, (x - 5, y -5, 410, 40) )
    pygame.draw.rect(screen, Red, (x, y, 400, 30) )
    pygame.draw.rect(screen, Yellow, (x, y, 400 * ratio, 30) )

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

    # Get Pressed Keys
    keys = pygame.key.get_pressed()
    
    # Draw background Image
    screen.blit(background_image, (0, 0))

    # Displaying the players stats
    draw_health_bar(fighter_1, 20, 20)
    draw_health_bar(fighter_2, 780, 20)

    # Move Fighters
    fighter_1.move(keys, screen_width, screen_height, screen, fighter_2)

    # update fighters
    fighter_2.update()
    fighter_1.update()
    

    # Draw fighter
    fighter_2.draw(screen)
    fighter_1.draw(screen)
    

    # Update display
    pygame.display.update()


# Exiting the Game and uninitializing all pygame modules
pygame.quit()
sys.exit()