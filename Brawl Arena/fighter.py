import pygame
import math

class Fighter():
    def __init__(self, player, x, y, ground_level, flip, third_attack, data, sprite_sheets, animation_steps):
        self.player = player
        self.sprite_sheets = sprite_sheets
        self.animation_steps = animation_steps
        self.x_size = data[0]
        self.y_size = data[1]
        self.image_scale = data[2]
        self.offset = data[3]
        self.timer_attack_1 = data[4]
        self.timer_attack_2 = data[5]
        self.timer_attack_3 = data[6]
        self.flip = False
        self.action = 0  # 0: idle, 1: run, 2: jump, 3: attack1, 4: attack2, 5: hit, 6: death
        self.frame_index = 0
        self.last_update = pygame.time.get_ticks()
        self.rect = pygame.Rect((x, y, 80, 180))
        self.velocity_y = 0
        self.running = False
        self.jump = False
        self.hit = False
        self.attacking = False
        self.third_attack = third_attack
        self.attack_type = 0
        self.attack_cooldown = 0
        self.bonus_damage = 0
        self.health = 100
        self.alive = True
        self.mana = 0
        self.animation = self.load_images()
        self.ground_level = ground_level
        self.attack_start_time = 0
        self.attack_duration = 0
        self.apply_attack_damage = False
        #self.damage_taken = 0
        self.damage_duration = 5000  # milliseconds
        #self.last_update_time = pygame.time.get_ticks()
        self.border_radius = 25
        self.rectangle_edge = 5

    def load_images(self):
        # Extraction of the images from the spritesheet
        animation_list = []
        for sheet, steps in zip(self.sprite_sheets, self.animation_steps):
            temporary_image_list = []
            for step in steps:
                for x in range(step):
                    temporary_image = sheet.subsurface(x * self.x_size, 0, self.x_size, self.y_size)
                    temporary_image_list.append(pygame.transform.scale(temporary_image, (
                    self.x_size * self.image_scale, self.y_size * self.image_scale)))
            animation_list.append(temporary_image_list)
        return animation_list

    def move(self, round_over, screen_width, screen_height, surface, enemy):
        SPEED = 8  # constant
        GRAVITY = 1.5
        dx = 0
        dy = 0

        # Reset animation state
        self.running = False
        self.attack_type = 0

        # Get Pressed Keys
        keys = pygame.key.get_pressed()

        # Performing actions if not attacking
        if self.attacking == False and self.alive == True and round_over == False :
            # check the player 1 controls
            if self.player == 1 :
                if keys[pygame.K_q]:
                    dx -= SPEED
                    self.running = True
                elif keys[pygame.K_d]:
                    dx += SPEED
                    self.running = True  
                # Jumping 
                if keys[pygame.K_z] and self.jump == False:
                    if self.rect.bottom == self.ground_level :  # Only jump if the fighter is on the ground
                        self.velocity_y = -30
                        self.jump = True 
                # Attack
                if keys[pygame.K_r] and self.third_attack == True and self.attack_cooldown == 0:
                    self.attack_type = 7
                    self.attack_duration = self.timer_attack_3
                    self.attack(enemy)
                elif keys[pygame.K_e] and self.attack_cooldown == 0:
                    self.attack_type = 1
                    self.attack_duration = self.timer_attack_1
                    self.attack(enemy)
                elif keys[pygame.K_a] and self.attack_cooldown == 0:
                    self.attack_type = 2
                    self.attack_duration = self.timer_attack_2 
                    self.attack(enemy)

                # Mana
                if keys[pygame.K_t] and self.mana == 50 :
                    self.bonus_damage = 10
                    self.mana = 0

            # check the player 2 controls
            if self.player == 2 :
                if keys[pygame.K_LEFT]:
                    dx -= SPEED
                    self.running = True
                if keys[pygame.K_RIGHT]:
                    dx += SPEED
                    self.running = True
                # Jumping 
                if keys[pygame.K_UP] and self.jump == False:
                    if self.rect.bottom == self.ground_level :  # Only jump if the fighter is on the ground
                        self.velocity_y = -30
                        self.jump = True
                # Attack
                if keys[pygame.K_p] and self.third_attack == True and self.attack_cooldown == 0:
                    self.attack_type = 7
                    self.attack_duration = self.timer_attack_3
                    self.attack(enemy)
                elif keys[pygame.K_m] and self.attack_cooldown == 0:
                    self.attack_type = 1
                    self.attack_duration = self.timer_attack_1
                    self.attack(enemy)
                elif keys[pygame.K_l] and self.attack_cooldown == 0:
                    self.attack_type = 2
                    self.attack_duration = self.timer_attack_2
                    self.attack(enemy)

                # Mana
                if keys[pygame.K_o] and self.mana == 50 :
                    self.bonus_damage = 10
                    self.mana = 0

        # Ensure fighters face each other
        if enemy.rect.centerx > self.rect.centerx :
            self.flip = False
        else :
            self.flip = True

        # apply attack cooldown
        if self.attack_cooldown > 0 :
            self.attack_cooldown -= 1

        dy += self.velocity_y

        # Fighter stays on the screen (left and right)
        if self.rect.left + dx < 0 : 
            dx = -self.rect.left 
        elif self.rect.right + dx > screen_width :
            dx = screen_width - self.rect.right

        # Updating the position of the fighter (moving the rect by dx and dy)
        self.rect.move_ip(dx, dy) 

        # Update velocity for gravity
        self.velocity_y += GRAVITY

        # Fighter stays on the ground
        if self.rect.bottom > self.ground_level :
            self.rect.bottom = self.ground_level
            self.velocity_y = 0
            self.jump = False

    def update_attack(self) :
        if self.attack_type == 1 :
            self.update_fighter_action(4) # attack1
        elif self.attack_type == 2 :
            self.update_fighter_action(5) # attack2
        elif self.attack_type == 7 :
            self.update_fighter_action(8) # attack 3

    def update(self, enemy) :

        # check if the fighter is dead
        if self.health <= 0 :
            self.health = 0
            self.alive = False
            self.update_fighter_action(7) # death

        # Check if the fighter is in mid-air
        elif self.jump == True and self.rect.bottom != self.ground_level : 
            if self.attacking == True :
                # Update the fighter's action to attacking while jumping
                self.update_attack()
            # Check if the fighter is at the maximum height of the jump
            elif self.velocity_y >= 0:
                self.update_fighter_action(3)  # fall animation
            else :
                self.update_fighter_action(2)  # jump animation

        else:
        # Check other conditions and update animations accordingly
            if self.hit == True :
                self.update_fighter_action(6) # hit
                self.hit = False
            elif self.attacking == True :
                self.update_attack()
            elif self.running == True :
                self.update_fighter_action(1)  # run
            else : 
                self.update_fighter_action(0) # idle

  
        ANIMATION_COOLDOWN = 90 # Default to 100 milliseconds if action not found
        current_time = pygame.time.get_ticks()

        # update image
        self.image = self.animation[self.action][self.frame_index]

        # Check if enough time has passed since the last update
        if current_time - self.last_update > ANIMATION_COOLDOWN :
            self.frame_index += 1
            self.last_update = current_time

            if self.frame_index >= len(self.animation[self.action]) :
                if self.alive == True :
                    # check if an attack was done
                    if self.action in (4, 5, 8) :
                        self.frame_index = 0
                        # Check if it's during a attack animation
                        self.attacking = False
                        self.attack_cooldown = 30
                        self.update_fighter_action(0) # idle
                    # check if fighter took a hit
                    elif self.action == 6 :
                        self.frame_index = 0
                        self.hit = False
                        # check that if the player is in the middle of an attack it is stoppped
                        self.attacking = False
                        self.attack_cooldown = 50
                        self.update_fighter_action(0) # idle
                    # Transition back to idle animation
                    else :
                        self.frame_index = 0  # idle
                else :
                    # If the fighter is dead, keep the last frame of the death animation
                    self.frame_index = len(self.animation[self.action]) - 1
        
        if self.attack_cooldown > 0 :
            self.attack_cooldown -= 1

    def draw(self, surface) :
        # Get the current animation frame
        current_frame = self.animation[self.action][self.frame_index]
    
        # Flip the current frame if necessary
        if self.flip == True :
            current_frame = pygame.transform.flip(current_frame, self.flip, False)

        # Draw the flipped frame onto the surface
         ###pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(current_frame, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))

    def attack(self, enemy):
        if self.attack_cooldown == 0:
            self.attacking = True
            self.attack_start_time = pygame.time.get_ticks()

            # Define base damage
            base_damage = 5

            # Apply bonus damage if available
            total_damage = base_damage + self.bonus_damage

            # Determine attacking rectangle position based on fighter orientation
            if self.flip:
                attacking_rect_left = self.rect.left - 1.5 * self.rect.width
            else:
                attacking_rect_left = self.rect.right

            # Create the attacking rectangle
            attacking_rect = pygame.Rect(attacking_rect_left, self.rect.y, 1.5 * self.rect.width, self.rect.height)

            # Check for collision with the enemy
            if attacking_rect.colliderect(enemy.rect):
                enemy.hit = True
                if self.attacking == True and self.apply_attack_damage == True :
                    print("good")
                    current_time = pygame.time.get_ticks()
                    elapsed_time = current_time - self.attack_start_time
                    if elapsed_time >= self.attack_duration :
                        enemy.health = enemy.health -5 - self.bonus_damage
                        self.apply_attack_damage = False
                        self.bonus_damage = 0
                # Apply damage to the enemy
                enemy.health -= total_damage
                # Set cooldown period for the attack
                self.attack_cooldown = 30
                # Add mana when the attack hits
                self.add_mana(10)
                self.bonus_damage = 0

            # Draw the attacking rectangle for debugging
            ### pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def update_fighter_action(self, new_action):
        # check if the new action is different than the previous one
        if new_action != self.action:
            self.action = new_action

            # update de animation settings
            self.frame_index = 0
            self.last_update = pygame.time.get_ticks()

            # Inside the Fighter class definition

    def reset(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y
        self.ground_level = 581
        self.health = 100
        self.mana = 0

    def add_mana(self, add) :
        if self.mana + add < 50 :
            self.mana += add
        elif self.mana + add > 50 :
            self.mana = 50

    # Function to draw fighter health bars
    def update_health(self, enemy, x, y, screen):

        LIGHT_GREY = (160, 160, 160)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        GREEN = (20, 255, 150)
        PURPLE = (200, 0, 255)
        PINK = (255, 0, 255)

        RECTANGLE_WIDTH = 400
        RECTANGLE_HEIGHT = 30

        if self.mana < 50 :
            mana_colour = PURPLE
        if self.mana == 50 :
            mana_colour = PINK

        # Calculate ratios for health and mana
        ratio_health = self.health / 100
        ratio_mana = self.mana / 50
        
        # Draw inner health bar
        pygame.draw.rect(screen, LIGHT_GREY, (x, y, RECTANGLE_WIDTH, RECTANGLE_HEIGHT), border_radius=self.border_radius)

        # Draw health bar based on fighter
        if self.player == 1 :
            if self.health > 15 :
                pygame.draw.rect(screen, GREEN, (x, y, RECTANGLE_WIDTH * ratio_health, RECTANGLE_HEIGHT), border_radius=self.border_radius)
            else :
                pygame.draw.rect(screen, GREEN, (x, y, RECTANGLE_WIDTH * ratio_health, RECTANGLE_HEIGHT), border_radius=self.border_radius)
        if self.player == 2 :
            if self.health > 15 :
                pygame.draw.rect(screen, GREEN, (x + RECTANGLE_WIDTH - (RECTANGLE_WIDTH * ratio_health), y, RECTANGLE_WIDTH * ratio_health, RECTANGLE_HEIGHT), border_radius=self.border_radius)
            else :
                pygame.draw.rect(screen, GREEN, (x + RECTANGLE_WIDTH - (RECTANGLE_WIDTH * ratio_health), y, RECTANGLE_WIDTH * ratio_health, RECTANGLE_HEIGHT), border_radius=self.border_radius)

        # Draw outer border
        pygame.draw.rect(screen, BLACK, (x - 5, y - 5, RECTANGLE_WIDTH + 10, RECTANGLE_HEIGHT + 10), self.rectangle_edge, border_radius=self.border_radius)

        RECTANGLE_WIDTH_DIVISION = math.ceil(RECTANGLE_WIDTH / 2)

        # Draw mana bar based on fighter
        if self.player == 1 :
            pygame.draw.rect(screen, LIGHT_GREY, (x, y + 45, RECTANGLE_WIDTH_DIVISION, RECTANGLE_HEIGHT), border_radius=self.border_radius)
            pygame.draw.rect(screen, mana_colour, (x, y + 45, 200 * ratio_mana, RECTANGLE_HEIGHT), border_radius=self.border_radius)
            pygame.draw.rect(screen, BLACK, (x - 5, y + 40, RECTANGLE_WIDTH_DIVISION + 10, RECTANGLE_HEIGHT + 10), self.rectangle_edge, border_radius=self.border_radius)
        if self.player == 2 :
            pygame.draw.rect(screen, LIGHT_GREY, (x + RECTANGLE_WIDTH_DIVISION, y + 45, RECTANGLE_WIDTH_DIVISION, RECTANGLE_HEIGHT), border_radius=self.border_radius)
            if self.mana < 50 :
                pygame.draw.rect(screen, mana_colour, (x + RECTANGLE_WIDTH - (RECTANGLE_WIDTH_DIVISION * ratio_mana) + 1, y + 45, 200 * ratio_mana, RECTANGLE_HEIGHT), border_radius=self.border_radius)
            else :
                pygame.draw.rect(screen, mana_colour, (x + RECTANGLE_WIDTH - (RECTANGLE_WIDTH_DIVISION * ratio_mana), y + 45, 200 * ratio_mana, RECTANGLE_HEIGHT), border_radius=self.border_radius)
            pygame.draw.rect(screen, BLACK, (x + RECTANGLE_WIDTH_DIVISION - 5, y + 40, RECTANGLE_WIDTH_DIVISION + 10, RECTANGLE_HEIGHT + 10), self.rectangle_edge, border_radius=self.border_radius)

        # Calculate the width of the damage rectangle based on damage taken
        # damage_width = RECTANGLE_WIDTH * (self.damage_taken / 100)
            
        # Calculate the starting position of the damage rectangle based on player
        # damage_x = x + RECTANGLE_WIDTH - damage_width

        gap = 0
        if self.health < 100 :
            gap = RECTANGLE_WIDTH * (1 - ratio_health)
        
        # If damage has been taken, draw a white rectangle representing the damage
        #if self.damage_taken > 0:
        #    if self.player == 1 :
        #        pygame.draw.rect(screen, WHITE, (x + RECTANGLE_WIDTH - gap, y, damage_width, RECTANGLE_HEIGHT))

        #    if self.player == 2 :
        #        pygame.draw.rect(screen, WHITE, (damage_x - RECTANGLE_WIDTH + gap, y, damage_width, RECTANGLE_HEIGHT))
                
            # Decrease the duration for damage indicator
        #    self.damage_duration -= pygame.time.get_ticks() - self.last_update_time

        #    if self.damage_duration <= 0:
        #        self.damage_taken = 0
        #        self.damage_duration = 5000  # Reset duration
        #    if self.health == 0 :
        #        self.damage_taken = 0
        #        self.damage_duration = 0

        # Reset the last update time
        #self.last_update_time = pygame.time.get_ticks()

