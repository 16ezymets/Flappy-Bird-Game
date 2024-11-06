import pygame

SCREEN_WIDTH = 925
SCREEN_HEIGHT = 712
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FPS = 30
clock = pygame.time.Clock()

bg = pygame.image.load('background.png')
ground_img = pygame.image.load('ground.png')

pygame.display.set_caption('Flappy Bird')

er = 0.01

jump_pow = 10
k_rotate = 1.5

PIPE_HEIGHT = pygame.image.load('pipe.png').get_height()
PIPE_WIDTH = pygame.image.load('pipe.png').get_width()
pipe_gap = 100
pipe_speed = 13

difficulty = 0
if difficulty == 1:
    fall_a = 2
    jump_pow = 15
    fall_speed_limit = 32
    game_a = 0.01
    game_speed_limit = 17
else:
    jump_pow = 10
    fall_a = 1
    fall_speed_limit = 16
    game_a = 0.005
    game_speed_limit = 15
