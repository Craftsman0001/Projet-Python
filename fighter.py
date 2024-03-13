import pygame

class Fighter() :
    def __init__(self, x, y) :
        self.rect = pygame.Rect((x, y, 80, 180))

    def draw(self, surface) :
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def move(self, keys) :
        speed = 8
        dx = 0
        dy = 0

        if keys[pygame.K_q]:
            dx -= 1
        if keys[pygame.K_d]:
            dx += 1
        if keys[pygame.K_z]:
            dy -= 1
        if keys[pygame.K_s]:
            dy += 1

        #Updating the position of the fighter
        self.rect.x += dx * speed
        self.rect.x += dy * speed

