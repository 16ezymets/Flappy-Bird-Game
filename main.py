from bird import *
import pipe
from pipehit import *
from pipe import *
from random import randint

pygame.init()


def run():
    k = 0
    ground_scroll = 0
    scroll_speed = pipe.pipe_speed
    pipe_frequency = scroll_speed * 500  # mls
    last_pipe = pygame.time.get_ticks() - pipe_frequency

    btm_pipe = Pipe(SCREEN_WIDTH, int(SCREEN_HEIGHT / 2))
    top_pipe = Pipe(SCREEN_WIDTH, int(SCREEN_HEIGHT / 2) - pipe_gap, 1)

    game_over = False
    running = True
    while running:
        clock.tick(FPS)

        screen.blit(bg, (0, 0))

        bird_group.draw(screen)
        pipe_group.draw(screen)

        if scroll_speed < game_speed_limit and not flappy.fallen:
            k += 1
            scroll_speed += game_a
            pipe.pipe_speed += game_a
            pipe_frequency = (scroll_speed - 1.33 * game_a * k) * 50  # mls
        screen.blit(ground_img, (ground_scroll, 655))

        # animations
        if not game_over:
            # new pipes
            time_now = pygame.time.get_ticks()
            if time_now - last_pipe > pipe_frequency:
                r = randint(-100, 100)
                btm_pipe = Pipe(SCREEN_WIDTH, int(SCREEN_HEIGHT / 2) + r)
                top_pipe = Pipe(SCREEN_WIDTH, int(SCREEN_HEIGHT / 2) - pipe_gap + r, 1)
                pipe_group.add(btm_pipe, top_pipe)
                last_pipe = time_now

            bird_group.update()
            pipe_group.update()

            ground_scroll -= scroll_speed
            if ground_scroll <= bg.get_width() - ground_img.get_width():
                ground_scroll = 12

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not flappy.flying and not game_over:
                flappy.flying = True

        # game over
        if flappy.rect.bottom > bg.get_height() + er and not game_over:
            bird_group.update()
            game_over = True
        if flappy.rect.top < 0 + er and not flappy.fallen:
            flappy.fallen = True
        if hit(flappy, top_pipe, btm_pipe):
            scroll_speed = 0
            flappy.fallen = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not flappy.flying and not game_over:
                flappy.flying = True
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    run()
