import pygame

class Fighter() :
    def __init__(self, x, y) :
        self.rect = pygame.Rect((x, y, 80, 180))
        self.velocity_y = 0

    def draw(self, surface) :
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def move(self, keys, screen_width, screen_height) :
        speed = 10
        gravity = 2
        dx = 0
        dy = 0

        if keys[pygame.K_q]:
            dx -= speed
        if keys[pygame.K_d]:
            dx += speed
        
        # Jumping 
        if keys[pygame.K_z] :
            if self.rect.bottom == 581 :  # Only jump if the fighter is on the ground
                self.velocity_y = -30

        dy += self.velocity_y

        # Fighter stays on the screen (left and right)
        if self.rect.left + dx < 0 : 
            dx = -self.rect.left 
        if self.rect.right + dx > screen_width :
            dx = screen_width - self.rect.right

        # Updating the position of the fighter
        self.rect.move_ip(dx, dy) # Move the rect by dx and dy

        # Update velocity for gravity
        self.velocity_y += 2

        # Fighter stays on the ground
        if self.rect.bottom > 581 :
            self.rect.bottom = 581
            self.velocity_y = 0

