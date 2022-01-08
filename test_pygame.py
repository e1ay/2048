import sys
from pygame.locals import *
import pygame
import settings
import numpy as np


def draw_game(screen, grid, font):
    screen.fill((settings.colors['background']))
    for i in range(settings.n):
        for j in range(settings.n):
            a = grid[i][j]

            rect_x = j * settings.w // settings.n + settings.margin
            rect_y = i * settings.w // settings.n + settings.margin
            rect_w = settings.w // settings.n - 2 * settings.margin
            rect_h = settings.w // settings.n - 2 * settings.margin

            pygame.draw.rect(screen, settings.colors[a], pygame.Rect(rect_x, rect_y, rect_w, rect_h),
                             border_radius=10)
            text_surface = font.render(f'{a}', True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(rect_x + rect_w / 2,
                                                      rect_y + rect_h / 2))
            screen.blit(text_surface, text_rect)


def wait_for_k():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return 'q'
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    return 'u'
                elif event.key == K_RIGHT:
                    return 'r'
                elif event.key == K_LEFT:
                    return 'l'
                elif event.key == K_DOWN:
                    return 'd'
                elif event.key == K_q or event.key == K_ESCAPE:
                    return 'q'


def main():
    pygame.init()
    # logo = pygame.image.load('logo32x32.png')
    # pygame.display.set_icon(logo)
    pygame.display.set_caption('2048')
    screen = pygame.display.set_mode((settings.window_size))
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 30)

    running = True

    while running:
        np.random.shuffle(settings.test_grid)

        draw_game(screen, settings.test_grid, font)
        pygame.display.flip()
        key = wait_for_k()
        if key == 'q':
            running = False


if __name__ == '__main__':
    main()
