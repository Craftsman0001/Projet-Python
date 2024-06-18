import pygame
from fighter import Fighter

class RangedFighter(Fighter):
    def __init__(self, player, x, y, ground_level, flip, third_attack, data, player_sprite_sheets, player_animation_steps, projectile_sprite_sheets, projectile_animation_steps):
        super().__init__(player, x, y, ground_level, flip, third_attack, data, player_sprite_sheets, player_animation_steps)
        self.projectile_x_size = data[4]
        self.projectile_y_size = data[5]
        self.projectile_image_scale = data[6]
        self.projectile_y_offset = data[7]
        self.projectile_width = data[8]
        self.projectile_height = data[9]
        self.projectiles = []
        self.projectile_speed = 20  # Speed of the projectile
        # self.projectile_cooldown = 60  # Cooldown for firing projectiles
        self.player_sprite_sheets = player_sprite_sheets
        self.player_animation_steps = player_animation_steps
        self.projectile_sprite_sheets = [projectile_sprite_sheets]
        self.projectile_animation_steps = [projectile_animation_steps]
        self.projectile_images = self.load_projectile_images()  # Load the projectile images
        self.projectile_damage = 5
        self.bonus_damage = 0
        self.last_shot_time = 0 # Add a new attribute to keep track of the last shot time
        self.projectile_cooldown_period = 500  # Define the cooldown period for firing projectiles in milliseconds


    def load_projectile_images(self):
        # Extraction of the images from the projectile spritesheet
        projectile_animation_list = []
        for sheet, steps in zip(self.projectile_sprite_sheets, self.projectile_animation_steps):
            temporary_image_list = []
            for step in steps:
                for x in range(step):
                    temporary_image = sheet.subsurface(x * self.projectile_x_size, 0, self.projectile_x_size, self.projectile_y_size)
                    scaled_image = pygame.transform.scale(temporary_image, (self.projectile_width, self.projectile_height))
                    temporary_image_list.append(scaled_image)
            projectile_animation_list.append(temporary_image_list)
        return projectile_animation_list

    def shoot(self):
        # Check if enough time has passed since the last shot
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.projectile_cooldown_period:
            if self.frame_index == len(self.animation[self.action])-2 and self.action in (4, 5):
                if self.flip:
                    direction = -1
                else:
                    direction = +1
                self.projectile_y_offset = self.projectile_y_offset + (self.bonus_damage //2)
                projectile_x = self.rect.centerx + direction * self.rect.width // 2 + (self.bonus_damage //2)
                projectile_y = self.rect.centery + self.projectile_y_offset + (self.bonus_damage //2)

                # Apply bonus damage if "T" key is pressed and mana is sufficient
                damage = self.projectile_damage + self.bonus_damage 
                projectile = {
                    "rect": pygame.Rect(projectile_x, projectile_y, self.projectile_width, self.projectile_height),
                    "direction": direction,
                    "animation_index": 0,
                    "damage": damage
                }
                self.projectiles.append(projectile)
                self.last_shot_time = current_time  # Update the last shot time
                self.bonus_damage = 0
                self.projectile_x_size = self.projectile_x_size/3
                self.projectile_y_size = self.projectile_y_size/3
                self.projectile_y_offset = self.projectile_y_offset/2
                # self.projectile_cooldown = 60

    def update_projectiles(self, screen_width, enemy):
        for projectile in self.projectiles:
            projectile["rect"].x += projectile["direction"] * self.projectile_speed
            # Check for collision with the enemy
            if projectile["rect"].colliderect(enemy.rect):
                # Reduce enemy's health (assuming there's a method `reduce_health` in the Enemy class)
                enemy.health -= projectile["damage"] 
                self.add_mana(10)
                # Remove the projectile
                self.projectiles.remove(projectile)
        # Remove projectiles that are out of the screen
        self.projectiles = [p for p in self.projectiles if 0 < p["rect"].x < screen_width]

    def draw_projectiles(self, surface):
        for projectile in self.projectiles:
            # Get the current animation frame for the projectile
            current_frame = self.projectile_images[0][projectile["animation_index"]]
            if projectile["direction"] == -1:
                current_frame = pygame.transform.flip(current_frame, True, False)  # Flip image for left direction
            surface.blit(current_frame, projectile["rect"].topleft)
            # Update the animation index
            projectile["animation_index"] = (projectile["animation_index"] + 1) % len(self.projectile_images[0])

    def move(self, round_over, screen_width, screen_height, surface, enemy):
        super().move(round_over, screen_width, screen_height, surface, enemy)

        keys = pygame.key.get_pressed()

        if self.player == 1:
            if keys[pygame.K_e] : #and self.projectile_cooldown == 0:
                self.shoot()
            if keys[pygame.K_t] and self.mana >= 50:
                self.bonus_damage = 10
                self.mana -= 50  # Deduct mana
                self.projectile_x_size = self.projectile_x_size*3
                self.projectile_y_size = self.projectile_y_size*3
                self.projectile_y_offset = self.projectile_y_offset*2
            #else:
            #    self.bonus_damage = 0

        elif self.player == 2:
            if keys[pygame.K_m] : #and self.projectile_cooldown == 0:
                self.shoot()
            if keys[pygame.K_o] and self.mana >= 50:
                self.bonus_damage = 10
                self.mana -= 50  # Deduct mana
                self.projectile_x_size = self.projectile_x_size*3
                self.projectile_y_size = self.projectile_y_size*3
                self.projectile_y_offset = self.projectile_y_offset*2
            #else:
            #    self.bonus_damage = 0

        self.update_projectiles(screen_width, enemy)

    #def update(self, enemy):
    #    super().update(enemy)
        #if self.projectile_cooldown > 0:
        #    self.projectile_cooldown -= 1

    def draw(self, surface):
        super().draw(surface)
        self.draw_projectiles(surface)