import pygame
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

# Creation of instances for fighters
fighter_1 = Fighter(200, 400)
fighter_2 = Fighter(925, 400)


# Game Loop
clock = pygame.time.Clock() # Setting up framerate
run = True
while run :

    # Event Handler
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False

    # Get Pressed Keys
    keys = pygame.key.get_pressed()
    
    # Move Fighters
    fighter_1.move(keys, screen_width, screen_height)

    # Draw background Image
    screen.blit(background_image, (0, 0))

    # Draw fighter
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    # Update display
    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

    #Update display
    pygame.display.update()


# Exiting the Game and uninitializing all pygame modules
pygame.quit()