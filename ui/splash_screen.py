import pygame
import time


def show_splash(screen):

    font_big = pygame.font.Font(None, 70)
    font_small = pygame.font.Font(None, 30)

    start_time = time.time()

    while time.time() - start_time < 2:

        screen.fill((15, 18, 25))

        title = font_big.render(
            "ORION ROBOTICS",
            True,
            (0, 200, 255)
        )

        subtitle = font_small.render(
            "Autonomous Multi-Robot Warehouse Simulator",
            True,
            (220, 220, 220)
        )

        loading = font_small.render(
            "Initializing AI Systems...",
            True,
            (180, 180, 180)
        )

        screen.blit(
            title,
            (250, 250)
        )

        screen.blit(
            subtitle,
            (220, 330)
        )

        screen.blit(
            loading,
            (330, 400)
        )

        pygame.display.update()