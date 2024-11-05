from settings import *


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        self.fall_speed = 0

        for num in range(1, 4):
            img = pygame.image.load(f'bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.clicked = False
        self.fallen = False
        self.flying = False

    def update(self, *args, **kwargs):
        if self.flying:
            # gravity
            self.fall_speed += fall_a
            if self.fall_speed > fall_speed_limit:
                self.fall_speed = fall_speed_limit
            if self.rect.bottom <= bg.get_height() + er:
                self.rect.y += self.fall_speed
            else:
                self.fallen = True

        if not self.fallen:
            # jump
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                self.fall_speed = -jump_pow
            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False

            # animation
            self.counter += 1
            limit = 5
            if self.counter > limit:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

            # rotate
            self.image = pygame.transform.rotate(self.image, -self.fall_speed * k_rotate)
        else:
            self.image = pygame.transform.rotate(self.image, -90)


flappy = Bird(100, int(SCREEN_HEIGHT / 2))
bird_group = pygame.sprite.Group()
bird_group.add(flappy)
