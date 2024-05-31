import pygame

class RangedFighter(Fighter):
    def __init__(self, player, x, y, ground_level, flip, third_attack, data, sprite_sheets, animation_steps):
        super().__init__(player, x, y, ground_level, flip, third_attack, data, sprite_sheets, animation_steps)
        self.projectiles = []
        self.projectile_speed = 10  # Speed of the projectile
        self.projectile_cooldown = 0  # Cooldown for firing projectiles
        self.projectile_image = None  # Placeholder for projectile image, should be set later

    def load_projectile_image(self, projectile_image):
        self.projectile_image = pygame.transform.scale(projectile_image, (self.x_size // 2, self.y_size // 2))

    def shoot(self):
        if self.projectile_cooldown == 0 and self.projectile_image:
            direction = -1 if self.flip else 1
            projectile_x = self.rect.centerx + direction * self.rect.width // 2
            projectile_y = self.rect.centery
            projectile = pygame.Rect(projectile_x, projectile_y, self.x_size // 2, self.y_size // 2)
            self.projectiles.append({"rect": projectile, "direction": direction})
            self.projectile_cooldown = 30  # Set cooldown period for shooting

    def update_projectiles(self, screen_width):
        for projectile in self.projectiles:
            projectile["rect"].x += projectile["direction"] * self.projectile_speed
        # Remove projectiles that are out of the screen
        self.projectiles = [p for p in self.projectiles if 0 < p["rect"].x < screen_width]

    def draw_projectiles(self, surface):
        for projectile in self.projectiles:
            surface.blit(self.projectile_image, projectile["rect"].topleft)

    def move(self, round_over, screen_width, screen_height, surface, enemy):
        super().move(round_over, screen_width, screen_height, surface, enemy)
        if self.player == 1:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_f] and self.projectile_cooldown == 0:
                self.shoot()
        elif self.player == 2:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_k] and self.projectile_cooldown == 0:
                self.shoot()
        self.update_projectiles(screen_width)

    def update(self, enemy):
        super().update(enemy)
        if self.projectile_cooldown > 0:
            self.projectile_cooldown -= 1

    def draw(self, surface):
        super().draw(surface)
        self.draw_projectiles(surface)
