import pygame

def load_spritesheets():
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

    return {
        "fantasy_warrior": [idle_fantasy_warrior_sprite_sheet, run_fantasy_warrior_sprite_sheet, jump_fantasy_warrior_sprite_sheet, attack1_fantasy_warrior_sprite_sheet, attack2_fantasy_warrior_sprite_sheet, hit_fantasy_warrior_sprite_sheet, death_fantasy_warrior_sprite_sheet, attack3_fantasy_warrior_sprite_sheet],
        "wizard": [idle_wizard_sprite_sheet, run_wizard_sprite_sheet, jump_wizard_sprite_sheet, attack1_wizard_sprite_sheet, attack2_wizard_sprite_sheet, hit_wizard_sprite_sheet, death_wizard_sprite_sheet],
        "martial_hero": [idle_martial_hero_sprite_sheet, run_martial_hero_sprite_sheet, jump_martial_hero_sprite_sheet, attack1_martial_hero_sprite_sheet, attack2_martial_hero_sprite_sheet, hit_martial_hero_sprite_sheet, death_martial_hero_sprite_sheet, attack3_martial_hero_sprite_sheet]
    }

def load_animation_steps():
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

    return {
        "fantasy_warrior": [idle_fantasy_warrior_animation_steps, run_fantasy_warrior_animation_steps, jump_fantasy_warrior_animation_steps, attack1_fantasy_warrior_animation_steps, attack2_fantasy_warrior_animation_steps, hit_fantasy_warrior_animation_steps, death_fantasy_warrior_animation_steps, attack3_fantasy_warrior_animation_steps],
        "wizard": [idle_wizard_animation_steps, run_wizard_animation_steps, jump_wizard_animation_steps, attack1_wizard_animation_steps, attack2_wizard_animation_steps, hit_wizard_animation_steps, death_wizard_animation_steps],
        "martial_hero": [idle_martial_hero_animation_steps, run_martial_hero_animation_steps, jump_martial_hero_animation_steps, attack1_martial_hero_animation_steps, attack2_martial_hero_animation_steps, hit_martial_hero_animation_steps, death_fantasy_warrior_animation_steps, attack3_martial_hero_animation_steps]
    }
