from bird import flappy
from settings import *


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position=-1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pipe.png')
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = (x, y)
        if position == -1:
            self.rect.topleft = (x, y)

    def update(self, *args, **kwargs):
        if flappy.flying:
            self.rect.x -= pipe_speed


pipe_group = pygame.sprite.Group()
