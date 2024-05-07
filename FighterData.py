import pygame

def load_spritesheets():
    # function that downloads the fighters spritesheets for each action
    idle_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Idle.png")
    run_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Run.png")
    jump_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Jump.png")
    fall_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Fall.png")
    attack1_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Attack1.png")
    attack2_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Attack2.png")
    hit_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Take Hit.png")
    death_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Death.png")
    attack3_fantasy_warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Fantasy Warrior/Sprites/Attack3.png")

    idle_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Idle.png")
    run_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Run.png")
    jump_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Jump.png")
    fall_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Fall.png")
    attack1_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Attack1.png")
    attack2_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Attack2.png")
    hit_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Take Hit.png")
    death_wizard_sprite_sheet = pygame.image.load("Assets/Fighters/Evil Wizard/Sprites/Death.png")

    idle_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/Idle.png")
    run_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/Run.png")
    jump_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/Going Up.png")
    fall_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/Going Down.png")
    attack1_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/Attack1.png")
    attack2_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/Attack2.png")
    hit_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/Take Hit.png")
    death_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/Death.png")
    attack3_martial_hero_sprite_sheet = pygame.image.load("Assets/Fighters/Martial Hero/Sprites/Attack3.png")

    idle_oni_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Oni Samurai/Sprites/Idle.png")
    run_oni_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Oni Samurai/Sprites/Run.png")
    jump_oni_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Oni Samurai/Sprites/Jump.png")
    fall_oni_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Oni Samurai/Sprites/Fall.png")
    attack1_oni_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Oni Samurai/Sprites/Attack1.png")
    attack2_oni_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Oni Samurai/Sprites/Attack2.png")
    hit_oni_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Oni Samurai/Sprites/Take Hit.png")
    death_oni_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Oni Samurai/Sprites/Death.png")

    idle_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Samurai/Sprites/Idle.png")
    run_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Samurai/Sprites/Run.png")
    jump_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Samurai/Sprites/Jump.png")
    fall_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Samurai/Sprites/Fall.png")
    attack1_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Samurai/Sprites/Attack1.png")
    attack2_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Samurai/Sprites/Attack2.png")
    hit_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Samurai/Sprites/Take Hit 2.png")
    death_samurai_sprite_sheet = pygame.image.load("Assets/Fighters/Samurai/Sprites/Death.png")

    idle_Female_Warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Female Warrior/Idle.png")
    run_Female_Warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Female Warrior/Run.png")
    jump_Female_Warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Female Warrior/Jump.png")
    fall_Female_Warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Female Warrior/Fall.png")
    attack1_Female_Warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Female Warrior/Attack1.png")
    attack2_Female_Warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Female Warrior/DashAttack.png")
    hit_Female_Warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Female Warrior/HitEffect.png")
    death_Female_Warrior_sprite_sheet = pygame.image.load("Assets/Fighters/Female Warrior/DeathEffect.png")


    return {
        "fantasy_warrior": [idle_fantasy_warrior_sprite_sheet, run_fantasy_warrior_sprite_sheet, jump_fantasy_warrior_sprite_sheet, fall_fantasy_warrior_sprite_sheet, attack1_fantasy_warrior_sprite_sheet, attack2_fantasy_warrior_sprite_sheet, hit_fantasy_warrior_sprite_sheet, death_fantasy_warrior_sprite_sheet, attack3_fantasy_warrior_sprite_sheet],
        "wizard": [idle_wizard_sprite_sheet, run_wizard_sprite_sheet, jump_wizard_sprite_sheet, fall_wizard_sprite_sheet, attack1_wizard_sprite_sheet, attack2_wizard_sprite_sheet, hit_wizard_sprite_sheet, death_wizard_sprite_sheet],
        "martial_hero": [idle_martial_hero_sprite_sheet, run_martial_hero_sprite_sheet, jump_martial_hero_sprite_sheet, fall_martial_hero_sprite_sheet,  attack1_martial_hero_sprite_sheet, attack2_martial_hero_sprite_sheet, hit_martial_hero_sprite_sheet, death_martial_hero_sprite_sheet, attack3_martial_hero_sprite_sheet],
        "oni_samurai": [idle_oni_samurai_sprite_sheet, run_oni_samurai_sprite_sheet, jump_oni_samurai_sprite_sheet, fall_oni_samurai_sprite_sheet,  attack1_oni_samurai_sprite_sheet, attack2_oni_samurai_sprite_sheet, hit_oni_samurai_sprite_sheet, death_oni_samurai_sprite_sheet],
        "samurai": [idle_samurai_sprite_sheet, run_samurai_sprite_sheet, jump_samurai_sprite_sheet, fall_samurai_sprite_sheet, attack1_samurai_sprite_sheet, attack2_samurai_sprite_sheet, hit_samurai_sprite_sheet, death_samurai_sprite_sheet],
        "Female Warrior": [idle_Female_Warrior_sprite_sheet, run_Female_Warrior_sprite_sheet, jump_Female_Warrior_sprite_sheet, fall_Female_Warrior_sprite_sheet, attack1_Female_Warrior_sprite_sheet, attack2_Female_Warrior_sprite_sheet, hit_Female_Warrior_sprite_sheet, death_Female_Warrior_sprite_sheet]
    }

def load_animation_steps():
    # function that has the number of frames for each spritesheet
    idle_fantasy_warrior_animation_steps = [10]
    run_fantasy_warrior_animation_steps = [8]
    jump_fantasy_warrior_animation_steps = [3]
    fall_fantasy_warrior_animation_steps = [3]
    attack1_fantasy_warrior_animation_steps = [7]
    attack2_fantasy_warrior_animation_steps = [7]
    hit_fantasy_warrior_animation_steps = [3]
    death_fantasy_warrior_animation_steps = [7]
    attack3_fantasy_warrior_animation_steps = [8]

    idle_wizard_animation_steps = [8]
    run_wizard_animation_steps = [8]
    jump_wizard_animation_steps = [2]
    fall_wizard_animation_steps = [2]
    attack1_wizard_animation_steps = [8]
    attack2_wizard_animation_steps = [8]
    hit_wizard_animation_steps = [3]
    death_wizard_animation_steps = [7]

    idle_martial_hero_animation_steps = [10]
    run_martial_hero_animation_steps = [8]
    jump_martial_hero_animation_steps = [3]
    fall_martial_hero_animation_steps = [3]
    attack1_martial_hero_animation_steps = [7]
    attack2_martial_hero_animation_steps = [6]
    hit_martial_hero_animation_steps = [3]
    death_martial_hero_animation_steps = [11]
    attack3_martial_hero_animation_steps = [9]

    idle_oni_samurai_animation_steps = [4]
    run_oni_samurai_animation_steps = [8]
    jump_oni_samurai_animation_steps = [2]
    fall_oni_samurai_animation_steps = [2]
    attack1_oni_samurai_animation_steps = [4]
    attack2_oni_samurai_animation_steps = [4]
    hit_oni_samurai_animation_steps = [3]
    death_oni_samurai_animation_steps = [7]

    idle_samurai_animation_steps = [8]
    run_samurai_animation_steps = [8]
    jump_samurai_animation_steps = [2]
    fall_samurai_animation_steps = [2]
    attack1_samurai_animation_steps = [6]
    attack2_samurai_animation_steps = [6]
    hit_samurai_animation_steps = [4]
    death_samurai_animation_steps = [6]

    idle_Female_Warrior_animation_steps = [6]
    run_Female_Warrior_animation_steps = [8]
    jump_Female_Warrior_animation_steps = [3]
    fall_Female_Warrior_animation_steps = [3]
    attack1_Female_Warrior_animation_steps = [12]
    attack2_Female_Warrior_animation_steps = [10]
    hit_Female_Warrior_animation_steps = [4]
    death_Female_Warrior_animation_steps = [11]


    return {
        "fantasy_warrior": [idle_fantasy_warrior_animation_steps, run_fantasy_warrior_animation_steps, jump_fantasy_warrior_animation_steps, fall_fantasy_warrior_animation_steps,  attack1_fantasy_warrior_animation_steps, attack2_fantasy_warrior_animation_steps, hit_fantasy_warrior_animation_steps, death_fantasy_warrior_animation_steps, attack3_fantasy_warrior_animation_steps],
        "wizard": [idle_wizard_animation_steps, run_wizard_animation_steps, jump_wizard_animation_steps, fall_wizard_animation_steps, attack1_wizard_animation_steps, attack2_wizard_animation_steps, hit_wizard_animation_steps, death_wizard_animation_steps],
        "martial_hero": [idle_martial_hero_animation_steps, run_martial_hero_animation_steps, jump_martial_hero_animation_steps, fall_martial_hero_animation_steps, attack1_martial_hero_animation_steps, attack2_martial_hero_animation_steps, hit_martial_hero_animation_steps, death_fantasy_warrior_animation_steps, attack3_martial_hero_animation_steps],
        "oni_samurai": [idle_oni_samurai_animation_steps, run_oni_samurai_animation_steps, jump_oni_samurai_animation_steps, fall_oni_samurai_animation_steps, attack1_oni_samurai_animation_steps, attack2_oni_samurai_animation_steps, hit_oni_samurai_animation_steps, death_oni_samurai_animation_steps],
        "samurai": [idle_samurai_animation_steps, run_samurai_animation_steps, jump_samurai_animation_steps, fall_samurai_animation_steps, attack1_samurai_animation_steps, attack2_samurai_animation_steps, hit_samurai_animation_steps, death_samurai_animation_steps],
        "Female Warrior": [idle_Female_Warrior_animation_steps, run_Female_Warrior_animation_steps, jump_Female_Warrior_animation_steps, fall_Female_Warrior_animation_steps, attack1_Female_Warrior_animation_steps, attack2_Female_Warrior_animation_steps, hit_Female_Warrior_animation_steps, death_Female_Warrior_animation_steps]
    }

def fighter_variables() :
    #function that has the data for each fighter
    fantasy_warrior_size = 162
    fantasy_warrior_scale = 4
    fantasy_warrior_offset = [72, 56]  
    fantasy_warrior_timer_attack_1 = 350
    fantasy_warrior_timer_attack_2 = 200
    fantasy_warrior_timer_attack_3 = 450

    wizard_size = 250
    wizard_scale = 3
    wizard_offset = [112, 107]
    wizard_timer_attack_1 = 400
    wizard_timer_attack_2 = 400
    wizard_timer_attack_3 = 0

    martial_hero_size = 126
    martial_hero_scale = 3.5
    martial_hero_offset = [50, 30.5]
    martial_hero_timer_attack_1 = 350
    martial_hero_timer_attack_2 = 200
    martial_hero_timer_attack_3 = 550

    oni_samurai_size = 200
    oni_samurai_scale = 3.3
    oni_samurai_offset = [85, 73.5]
    oni_samurai_timer_attack_1 = 200
    oni_samurai_timer_attack_2 = 200
    oni_samurai_timer_attack_3 = 0

    samurai_size = 200
    samurai_scale = 3.3
    samurai_offset = [88, 67.5]
    samurai_timer_attack_1 = 280
    samurai_timer_attack_2 = 300
    samurai_timer_attack_3 = 0

    Female_Warrior_size = 200
    Female_Warrior_scale = 3.3
    Female_Warrior_offset = [88, 67.5]
    Female_Warrior_timer_attack_1 = 200
    Female_Warrior_timer_attack_2 = 200
    Female_Warrior_timer_attack_3 = 0

    return {
        "fantasy_warrior" : [fantasy_warrior_size, fantasy_warrior_scale, fantasy_warrior_offset, fantasy_warrior_timer_attack_1, fantasy_warrior_timer_attack_2, fantasy_warrior_timer_attack_3],
        "wizard" : [wizard_size, wizard_scale, wizard_offset, wizard_timer_attack_1, wizard_timer_attack_2, wizard_timer_attack_3],
        "martial_hero" : [martial_hero_size, martial_hero_scale, martial_hero_offset, martial_hero_timer_attack_1, martial_hero_timer_attack_2, martial_hero_timer_attack_3],
        "oni_samurai" : [oni_samurai_size, oni_samurai_scale, oni_samurai_offset, oni_samurai_timer_attack_1, oni_samurai_timer_attack_2, oni_samurai_timer_attack_3],
        "samurai": [samurai_size, samurai_scale, samurai_offset, samurai_timer_attack_1, samurai_timer_attack_2, samurai_timer_attack_3],
        "Female Warrior": [Female_Warrior_size, Female_Warrior_scale, Female_Warrior_offset, Female_Warrior_timer_attack_1, Female_Warrior_timer_attack_2, Female_Warrior_timer_attack_3]
    }