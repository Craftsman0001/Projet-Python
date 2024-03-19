import pygame

class Fighter() :
    def __init__(self, x, y, ground_level, flip, data, sprite_sheets, animation_steps) :
        self.sprite_sheets = sprite_sheets
        self.animation_steps = animation_steps
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
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
        self.attack_type = 0
        self.attack_cooldown = 0
        self.health = 100
        self.alive = True
        self.animation = self.load_images()
        self.ground_level = ground_level

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

    def move(self, keys, screen_width, screen_height, surface, enemy) :
        speed = 8
        gravity = 2
        dx = 0
        dy = 0

        # Reset animation state
        self.running = False
        self.attack_type = 0

        # Performing actions if not attacking
        if self.attacking == False and self.alive == True :
            if keys[pygame.K_q]:
                dx -= speed
                self.running = True
            if keys[pygame.K_d]:
                dx += speed
                self.running = True
                
            # Jumping 
            if keys[pygame.K_z] and self.jump == False:
                if self.rect.bottom == self.ground_level :  # Only jump if the fighter is on the ground
                    self.velocity_y = -30
                    self.jump = True
                    
            # Attack
            if keys[pygame.K_e] or keys[pygame.K_a] :
                self.attack(surface, enemy)
                # Determining which attack was used
                if keys[pygame.K_e] :
                    self.attack_type = 1
                if keys[pygame.K_a] :
                    self.attack_type = 2

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
        if self.rect.right + dx > screen_width :
            dx = screen_width - self.rect.right

        # Updating the position of the fighter (moving the rect by dx and dy)
        self.rect.move_ip(dx, dy) 

        # Update velocity for gravity
        self.velocity_y += gravity

        # Fighter stays on the ground
        if self.rect.bottom > self.ground_level :
            self.rect.bottom = self.ground_level
            self.velocity_y = 0
            self.jump = False

    def update(self) :
        # check what action the fighter is doing
        if self.health <= 0 :
            self.health = 0
            self.alive = False
            self.update_fighter_action(6) # death
        elif self.hit == True :
            self.update_fighter_action(5) # hit
            self.hit = False
        elif self.attacking == True :
            if self.attack_type == 1 :
                self.update_fighter_action(3) # attack1
            elif self.attack_type == 2 :
                self.update_fighter_action(4) # attack2
        elif self.jump == True :
            self.update_fighter_action(2) # jump
        elif self.running == True :
            self.update_fighter_action(1)  # run
        else : 
            self.update_fighter_action(0) # idle

  
        animation_cooldown = 100 # Default to 50 milliseconds if action not found
        current_time = pygame.time.get_ticks()
        # update image
        self.image = self.animation[self.action][self.frame_index]
        # Check if enough time has passed since the last update
        if current_time - self.last_update > animation_cooldown :
            self.frame_index += 1
            self.last_update = current_time
            # check if the animation has finished
        if self.frame_index >= len(self.animation[self.action]) -1 :
            # check if the fighter is dead and end the animation
            if self.alive == False :
                self.frame_index = len(self.animation[self.action]) -1
            else :
                self.frame_index = 0
                # check if an attack was done
                if self.action == 3 or self.action == 4 :
                    self.attacking = False
                    self.attack_cooldown = 20
                # check if fighter took damage
                if self.action == 5 :
                    self.hit = False
                    # check that if the player is in the middle of an attack it is stoppped
                    self.attacking = False
                    self.attack_cooldown = 20

    def draw(self, surface) :
        # Get the current animation frame
        image = self.animation[self.action][self.frame_index]
    
        # Flip the current frame if necessary
        #if self.flip == True :
            #current_frame = pygame.transform.flip(current_frame, self.flip, False)
        #image = pygame.transform.flip(self.image, self.flip, False)
        # Draw the flipped frame onto the surface
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(image, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))

    def attack(self, surface, enemy) :

        if self.attack_cooldown == 0 :
            
            self.attacking = True

            if self.flip :
                # If the fighter is flipped, the attacking rectangle starts from the left side of the fighter
                attacking_rect_left = self.rect.left - 1.5 * self.rect.width
            else :
                # If the fighter is not flipped, the attacking rectangle starts from the right side of the fighter
                attacking_rect_left = self.rect.right

            # Create the attacking rectangle
            attacking_rect = pygame.Rect(attacking_rect_left, self.rect.y, 1.5 * self.rect.width, self.rect.height)
        
            if attacking_rect.colliderect(enemy.rect) :
                enemy.health -= 10
                enemy.hit = True

            pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def update_fighter_action(self, new_action) :
        # check if the new action is different than the previous one
        if new_action != self.action :
            self.action = new_action

        # update de animation settings
            self.frame_index = 0
            self.last_update = pygame.time.get_ticks() 