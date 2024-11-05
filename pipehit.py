from bird import Bird
from pipe import Pipe
from settings import *


def hit(bird: Bird, top_pipe: Pipe, btm_pipe: Pipe) -> bool:
    """ Checks if bird hit one of the pipe """
    if (top_pipe.rect.x <= bird.rect.x <= top_pipe.rect.x + PIPE_WIDTH and
            top_pipe.rect.y <= bird.rect.y <= top_pipe.rect.y + PIPE_HEIGHT):
        return True
    if (btm_pipe.rect.x <= bird.rect.x <= btm_pipe.rect.x + PIPE_WIDTH and
            btm_pipe.rect.y <= bird.rect.y <= btm_pipe.rect.y + PIPE_HEIGHT):
        return True
    return False
