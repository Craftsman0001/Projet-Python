import pygame

class Fighter() :
    def __init__(self, player, x, y, ground_level, flip, third_attack, data, sprite_sheets, animation_steps) :
        self.player = player
        self.sprite_sheets = sprite_sheets
        self.animation_steps = animation_steps
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.timer_attack_1 = data[3]
        self.timer_attack_2 = data[4]
        self.timer_attack_3 = data[5]
        self.flip = False
        self.action = 0 # 0: idle, 1: run, 2: jump, 3: attack1, 4: attack2, 5: hit, 6: death
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
        self.health = 100
        self.alive = True
        self.animation = self.load_images()
        self.ground_level = ground_level
        self.attack_start_time = 0
        self.attack_duration = 0
        self.apply_attack_damage = False


    def load_images(self) :
        # Extraction of the images from the spritesheet
        animation_list = []
        for sheet, steps in zip(self.sprite_sheets, self.animation_steps) :
            temporary_image_list = []
            for step in steps :
                for x in range(step) :
                    temporary_image = sheet.subsurface(x * self.size, 0, self.size, self.size)
                    temporary_image_list.append( pygame.transform.scale(temporary_image, (self.size * self.image_scale, self.size * self.image_scale)))
            animation_list.append(temporary_image_list)
        return animation_list


    def move(self, round_over, screen_width, screen_height, surface, enemy) :
        SPEED = 8 # constant
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
                if keys[pygame.K_r] and self.third_attack == True:
                    self.attack_type = 7
                    self.attack_duration = self.timer_attack_3 
                    self.attack(enemy) 
                elif keys[pygame.K_e] :
                    self.attack_type = 1
                    self.attack_duration = self.timer_attack_1 
                    self.attack(enemy) 
                elif keys[pygame.K_a] :
                    self.attack_type = 2
                    self.attack_duration = self.timer_attack_2 
                    self.attack(enemy) 
                
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
                if keys[pygame.K_p] and self.third_attack == True:
                    self.attack_type = 7
                    self.attack_duration = self.timer_attack_3
                    self.attack(enemy)
                elif keys[pygame.K_m]:
                    self.attack_type = 1
                    self.attack_duration = self.timer_attack_1
                    self.attack(enemy)
                elif keys[pygame.K_l]:
                    self.attack_type = 2
                    self.attack_duration = self.timer_attack_2
                    self.attack(enemy)

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

        if self.attacking == True and self.apply_attack_damage == True :
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - self.attack_start_time
            if elapsed_time >= self.attack_duration :
                enemy.health -= 10
                self.apply_attack_damage = False

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
                        self.attack_cooldown = 20
                        self.update_fighter_action(0) # idle
                    # check if fighter took a hit
                    elif self.action == 6 :
                        self.frame_index = 0
                        self.hit = False
                        # check that if the player is in the middle of an attack it is stoppped
                        self.attacking = False
                        self.attack_cooldown = 20
                        self.update_fighter_action(0) # idle
                    # Transition back to idle animation
                    else :
                        self.frame_index = 0  # idle
                else :
                    # If the fighter is dead, keep the last frame of the death animation
                    self.frame_index = len(self.animation[self.action]) - 1


    def draw(self, surface) :
        # Get the current animation frame
        current_frame = self.animation[self.action][self.frame_index]
    
        # Flip the current frame if necessary
        if self.flip == True :
            current_frame = pygame.transform.flip(current_frame, self.flip, False)

        # Draw the flipped frame onto the surface
        ### pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(current_frame, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))


    def attack(self, enemy) : ### def attack(self, surface, enemy) :

        if self.attack_cooldown == 0 :
            
            self.attacking = True
            self.attack_start_time = pygame.time.get_ticks()

            if self.flip :
                # If the fighter is flipped, the attacking rectangle starts from the left side of the fighter
                attacking_rect_left = self.rect.left - 1.5 * self.rect.width
            else :
                # If the fighter is not flipped, the attacking rectangle starts from the right side of the fighter
                attacking_rect_left = self.rect.right

            # Create the attacking rectangle
            attacking_rect = pygame.Rect(attacking_rect_left, self.rect.y, 1.5 * self.rect.width, self.rect.height)
        
            if attacking_rect.colliderect(enemy.rect) :
                enemy.hit = True
                self.apply_attack_damage = True

            ### pygame.draw.rect(surface, (0, 255, 0), attacking_rect)


    def update_fighter_action(self, new_action) :
        # check if the new action is different than the previous one
        if new_action != self.action :
            self.action = new_action

            # update de animation settings
            self.frame_index = 0
            self.last_update = pygame.time.get_ticks() 

    # Inside the Fighter class definition
    def reset(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y
        self.health = 100
