import pygame
from pg_utils import *


# This function executes at the start of the program
def start():
    global get_ticks_last_frame
    get_ticks_last_frame = 0.0


# This function executes every frame
def update() -> bool:
    global get_ticks_last_frame, delta_time

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False

    pygame.display.flip()

    get_ticks_last_frame, delta_time = manage_frame_rate(clock, get_ticks_last_frame)

    return True


# Run the program
if __name__ == "__main__":
    run(start, update)
    pygame.quit()
