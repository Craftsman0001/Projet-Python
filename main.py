import pygame
import sys
from fighter import Fighter
from spritesheets import *
from moviepy.editor import VideoFileClip


# Fonction pour afficher la vidéo d'introduction et attendre que le joueur appuie sur Espace pour continuer
def display_intro_video():
    clip = VideoFileClip("Assets/intro/intro.mp4")
    clip = clip.without_audio()  # Désactiver la piste audio
    clip = clip.set_fps(60)

    # Loop pour afficher chaque trame de la vidéo
    for frame in clip.iter_frames():
        frame_surface = pygame.image.frombuffer(frame, clip.size, "RGB")
        screen.blit(frame_surface, (0, 0))
        pygame.display.update()

        # Vérifier si la touche "Espace" est pressée pour passer l'intro
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

    # Attendre un certain temps après la fin de la vidéo
    pygame.time.wait(100)


# Initialiser pygame
pygame.init()

# Création de la fenêtre du jeu
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mon jeu !")

# Charger l'image de fond et la redimensionner pour s'adapter à l'écran
original_background_image = pygame.image.load("Assets/BackGrounds/trees.jpg")
background_image = pygame.transform.scale(original_background_image, (screen_width, screen_height))

# Charger l'image de victoire
original_victory_image = pygame.image.load("Assets/Images/victory_3.png")
victory_image = pygame.transform.scale(original_victory_image, (400, 150))

# Charger les feuilles de sprite et les étapes d'animation
sprite_sheets = load_spritesheets()
animation_steps = load_animation_steps()

# Extraire les feuilles de sprite pour chaque combattant
fantasy_warrior_sprite_sheet = sprite_sheets["fantasy_warrior"]
wizard_sprite_sheet = sprite_sheets["wizard"]
martial_hero_sprite_sheets = sprite_sheets["martial_hero"]

# Extraire les étapes d'animation pour chaque combattant
fantasy_warrior_animation_steps = animation_steps["fantasy_warrior"]
wizard_animation_steps = animation_steps["wizard"]
martial_hero_animation_steps = animation_steps["martial_hero"]

# Définir les variables des combattants
fighter_data = fighter_variables()
fantasy_warrior_data = fighter_data["fantasy_warrior"]
wizard_data = fighter_data["wizard"]
martial_hero_data = fighter_data["martial_hero"]

# Définir les couleurs
Blue = (0, 0, 255)
Red = (255, 0, 0)
Yellow = (255, 255, 0)
White = (255, 255, 255)
Black = (0, 0, 0)
Green = (0, 255, 0)

# Définir les variables du jeu
countdown = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]  # Scores des joueurs : [joueur1, joueur2]
round_over = False
round_over_cooldown = 3000

# Définir les polices de caractères
countdown_font_1 = pygame.font.Font("Assets/Fonts/Turok.ttf", 200)
countdown_font_2 = pygame.font.Font("Assets/Fonts/Turok.ttf", 220)
score_font = pygame.font.Font("Assets/Fonts/Turok.ttf", 30)

# Créer les instances des combattants
fighter_1 = Fighter(1, 200, 400, 581, True, True, fantasy_warrior_data, fantasy_warrior_sprite_sheet,
                    fantasy_warrior_animation_steps)
fighter_2 = Fighter(2, 925, 400, 581, False, True, martial_hero_data, martial_hero_sprite_sheets,
                    martial_hero_animation_steps)


# Fonction pour dessiner les barres de vie des combattants
def draw_health_bar(fighter, x, y):
    ratio = fighter.health / 100
    pygame.draw.rect(screen, Black, (x - 5, y - 5, 410, 40))
    pygame.draw.rect(screen, Blue, (x, y, 400, 30))
    pygame.draw.rect(screen, Green, (x, y, 400 * ratio, 30))


# Fonction pour dessiner du texte
def draw_text(text, font, text_color, x, y):
    image = font.render(text, True, text_color)
    screen.blit(image, (x, y))


# Afficher l'intro et attendre que le joueur appuie sur Espace
display_intro_video()

# Boucle du jeu
clock = pygame.time.Clock()  # Réglage du framerate
run = True
while run:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Limiter le framerate
    clock.tick(60)

    # Dessiner l'image de fond
    screen.blit(background_image, (0, 0))

    # Afficher les statistiques des joueurs
    draw_health_bar(fighter_1, 20, 20)
    draw_health_bar(fighter_2, 780, 20)
    draw_text("Joueur 1 : " + str(score[0]), score_font, Black, 10, 60)
    draw_text("Joueur 2 : " + str(score[1]), score_font, Black, 770, 60)

    # Mettre à jour le compte à rebours
    if countdown <= 0:
        # Les combattants peuvent se déplacer
        fighter_1.move(round_over, screen_width, screen_height, screen, fighter_2)
        fighter_2.move(round_over, screen_width, screen_height, screen, fighter_1)
    else:
        # Assurer que les combattants se font face pendant le compte à rebours
        if fighter_2.rect.centerx > fighter_1.rect.centerx:
            fighter_2.flip = True
        else:
            fighter_2.flip = False
        # Afficher le compte à rebours
        if countdown == 1:
            draw_text(str(countdown), countdown_font_2, Black, screen_width / 2 - 20, screen_height / 3)
            draw_text(str(countdown), countdown_font_1, Red, screen_width / 2 - 20, screen_height / 3)
        else:
            draw_text(str(countdown), countdown_font_2, Black, screen_width / 2 - 40, screen_height / 3)
            draw_text(str(countdown), countdown_font_1, Red, screen_width / 2 - 40, screen_height / 3)
        # Mettre à jour le compte à rebours
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            countdown -= 1
            last_count_update = pygame.time.get_ticks()

    # Mettre à jour les combattants
    fighter_2.update(fighter_1)
    fighter_1.update(fighter_2)

    # Animation d'attaque fluide
    if fighter_1.attacking == True:
        fighter_2.draw(screen)
        fighter_1.draw(screen)
    elif fighter_2.attacking == True:
        fighter_1.draw(screen)
        fighter_2.draw(screen)
    else:
        fighter_2.draw(screen)
        fighter_1.draw(screen)

    # Vérifier si un joueur a été vaincu
    if not round_over:
        if not fighter_1.alive:
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif not fighter_2.alive:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
    else:
        # Afficher l'image de victoire
        screen.blit(victory_image, (400, 50))
        if pygame.time.get_ticks() - round_over_time > round_over_cooldown:
            round_over = False
            countdown = 3
            # Recréer les instances des combattants
            fighter_1 = Fighter(1, 200, 400, 581, True, True, fantasy_warrior_data, fantasy_warrior_sprite_sheet,
                                fantasy_warrior_animation_steps)
            fighter_2 = Fighter(2, 925, 400, 581, False, True, martial_hero_data, martial_hero_sprite_sheets,
                                martial_hero_animation_steps)

    # Mettre à jour l'affichage
    pygame.display.update()

# Quitter le jeu et désinitialiser tous les modules pygame
pygame.quit()
sys.exit()
