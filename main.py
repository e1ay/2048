import sqlite3

import numpy as np
import settings
import random
from pygame.locals import *
import pygame
import time


class Game2048:

    def __init__(self):
        self.grid = np.zeros((settings.n, settings.n), dtype=int)

        # self.W = 400
        # self.H = self.W
        self.c = 0
        pygame.init()
        # logo = pygame.image.load('logo32x32.png')
        # pygame.display.set_icon(logo)
        pygame.display.set_caption('2048')
        self.screen = pygame.display.set_mode(settings.window_size)
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.player_name = settings.player_name

    def __str__(self):
        return str(self.grid)

    def generate_number(self, k=1):
        free_poss = list(zip(*np.where(self.grid == 0)))

        for pos in random.sample(free_poss, k=k):
            if random.random() < .1:
                self.grid[pos] = 4
            else:
                self.grid[pos] = 2

    def make_move(self, move):
        for i in range(settings.n):
            if move in 'lr':
                tek = self.grid[i, :]
            else:
                tek = self.grid[:, i]

            revers = False
            if move in 'rd':
                revers = True
                tek = tek[::-1]

            tek_number = self.sum_numbers(tek)

            new_tek = np.zeros_like(tek)
            new_tek[:len(tek_number)] = tek_number

            if revers:
                new_tek = new_tek[::-1]

            if move in 'lr':
                self.grid[i, :] = new_tek
            else:
                self.grid[:, i] = new_tek

    @staticmethod
    def sum_numbers(tek):
        tek_number = tek[tek != 0]
        tek_number_sum = []
        flag = False

        for j in range(len(tek_number)):
            if flag:
                flag = False
                continue
            if j != len(tek_number) - 1 and tek_number[j] == tek_number[j + 1]:
                new_number = tek_number[j] * 2
                flag = True
            else:
                new_number = tek_number[j]

            tek_number_sum.append(new_number)

        return np.array(tek_number_sum)

    def draw_game(self):
        self.screen.fill((settings.colors['background']))
        for i in range(settings.n):
            for j in range(settings.n):
                a = self.grid[i][j]

                rect_x = j * settings.w // settings.n + settings.margin
                rect_y = i * settings.w // settings.n + settings.margin
                rect_w = settings.w // settings.n - 2 * settings.margin
                rect_h = settings.w // settings.n - 2 * settings.margin

                pygame.draw.rect(self.screen, settings.colors[a], pygame.Rect(rect_x, rect_y, rect_w, rect_h),
                                 border_radius=10)
                if a == 0:
                    continue
                text_surface = self.font.render(f'{a}', True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=(rect_x + rect_w / 2,
                                                          rect_y + rect_h / 2))
                self.screen.blit(text_surface, text_rect)

    @staticmethod
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

    def game_over(self):
        grid_copy = self.grid.copy()
        for move in 'lrud':
            self.make_move(move)
            if not all((self.grid == grid_copy).flatten()):
                self.grid = grid_copy
                return False
        return True

    def win(self):
        if self.grid.__contains__(settings.victory_point):
            return True
        return False

    def play(self):
        self.generate_number(k=2)
        while True:
            self.c += 1
            self.draw_game()
            pygame.display.flip()
            s = self.wait_for_k()

            if s == 'q':
                break
            old_grid = self.grid.copy()
            self.make_move(s)

            if self.game_over():
                self.end_lose()
                pygame.display.flip()
                time.sleep(2)
                break
            if self.win():
                self.end_win()
                pygame.display.flip()
                time.sleep(2)
                break

            pygame.display.update()

            if not all((self.grid == old_grid).flatten()):
                self.generate_number()

    def end_win(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 50)
        text = font.render("Win!", True, (100, 255, 100))
        text_x = 600 // 2 - text.get_width() // 2
        text_y = 600 // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        self.screen.blit(text, (text_x, text_y))
        pygame.draw.rect(self.screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                                    text_w + 20, text_h + 20), 1)
        self.add_to_db()

    def end_lose(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 50)
        text = font.render("Lose! Try again", True, (255, 0, 0))
        text_x = 600 // 2 - text.get_width() // 2
        text_y = 600 // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        self.screen.blit(text, (text_x, text_y))
        pygame.draw.rect(self.screen, (255, 0, 0), (text_x - 10, text_y - 10,
                                                    text_w + 20, text_h + 20), 1)

    def add_to_db(self):
        con = sqlite3.connect('database.sqlite')
        cur = con.cursor()
        cur.execute("""INSERT into RECORDS(name, score, size, steps) VALUES(?, ?, ?, ?)""",
                    (settings.player_name, settings.victory_point, settings.n, self.c))
        con.commit()
        con.close()
