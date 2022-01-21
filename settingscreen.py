import sys

import pygame
from PyQt5.QtWidgets import QApplication

from main import Game2048
import settings
import leaderboard
click_img = pygame.image.load('img/clk.png')
app = QApplication(sys.argv)


class SettingScreen:
    def __init__(self, xx, yy, image, scale):
        pygame.init()
        self.mainscreen = pygame.display.set_mode((600, 600))
        self.option_button = []
        self._victory_point = 2048
        self.screen_width = 600
        self.screen_height = 600
        self.x = 10
        self.y = 10
        pygame.display.set_caption('2048')
        logo = pygame.image.load('img/logo2.jpeg')
        pygame.display.set_icon(logo)
    #     ----------------------------
        self.image = pygame.transform.scale(image, (int(600 * scale), int(600 * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (xx, yy)
        self.clicked = False


    def show_screen(self):
        while True:
            stop = self.check_events()
            self.update_screen()
            if self.clicked:

                ex = leaderboard.Example()
                ex.show()
            if stop:
                q = Game2048()
                q.play()





    def update_screen(self):
        self.mainscreen.fill(settings.colors['background2'])
        self.show_option()
        self.mouse_pointing_show()
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_pressed = pygame.mouse.get_pressed()
                if button_pressed[0]:
                    cursor_pos = pygame.mouse.get_pos()
                    if self.option_button[6][0].collidepoint(cursor_pos):
                        return True
                    elif self.option_button[0][0].collidepoint(cursor_pos):
                        settings.victory_point = 16
                        self.draw_button_reaction(self.option_button[0][0],
                                                  color=(105, 103, 110))
                    elif self.option_button[1][0].collidepoint(cursor_pos):
                        settings.victory_point = 2048
                        self.draw_button_reaction(self.option_button[1][0], color=(20, 20, 20))
                    elif self.option_button[2][0].collidepoint(cursor_pos):
                        settings.victory_point = 4096
                        self.draw_button_reaction(self.option_button[2][0], color=(20, 20, 20))
                    elif self.option_button[3][0].collidepoint(cursor_pos):
                        settings.n = 2
                        self.draw_button_reaction(self.option_button[3][0], color=(20, 20, 20))
                    elif self.option_button[4][0].collidepoint(cursor_pos):
                        settings.n = 4
                        self.draw_button_reaction(self.option_button[4][0], color=(20, 20, 20))
                    elif self.option_button[5][0].collidepoint(cursor_pos):
                        settings.n = 8
                        self.draw_button_reaction(self.option_button[5][0], color=(20, 20, 20))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()

    def mouse_pointing_show(self):
        cursor_pos = pygame.mouse.get_pos()
        if self.option_button[0][0].collidepoint(cursor_pos):
            self.draw_button_reaction(self.option_button[0][0], self.option_button[0][1])
        elif self.option_button[1][0].collidepoint(cursor_pos):
            self.draw_button_reaction(self.option_button[1][0], self.option_button[1][1])
        elif self.option_button[2][0].collidepoint(cursor_pos):
            self.draw_button_reaction(self.option_button[2][0], self.option_button[2][1])
        elif self.option_button[3][0].collidepoint(cursor_pos):
            self.draw_button_reaction(self.option_button[3][0], self.option_button[3][1])
        elif self.option_button[4][0].collidepoint(cursor_pos):
            self.draw_button_reaction(self.option_button[4][0], self.option_button[4][1])
        elif self.option_button[5][0].collidepoint(cursor_pos):
            self.draw_button_reaction(self.option_button[5][0], self.option_button[5][1])
        elif self.option_button[6][0].collidepoint(cursor_pos):
            self.draw_button_reaction(self.option_button[6][0], self.option_button[6][1])

    def draw(self, x, y, box_width, box_height):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        self.mainscreen.blit(self.image, (self.rect.x, self.rect.y))
        return action

    def show_option(self):
        self.draw_whatever("CHOOSE GOAL:", self.screen_width // 2 - 120 // 2, self.y + 10, 120, 60)
        self.draw_whatever("TIPS:", 10, 10, 60, 60)
        self.draw_whatever("Use the arrows", 40, 40, 120, 60)

        self.draw_whatever("Press 'Q' to exit", self.screen_width // 10, self.y + 500, 120, 60)

        self.draw(300, 300, 100, 100)

        self.draw_option_box(self.screen_width // 2 - 120 // 2, self.y + 90, 120, 60, "16", 1)
        self.draw_option_box(self.screen_width // 2 - 120 // 2, self.y + 160, 120, 60, "2048", 1)
        self.draw_option_box(self.screen_width // 2 - 120 // 2, self.y + 230, 120, 60, "4096", 1)

        self.draw_whatever("CHOOSE SIZE:", self.screen_width // 2 - 120 // 2, self.y + 300, 120, 60)
        self.draw_option_box(self.screen_width // 2 - 120 // 2, self.y + 380, 120, 60, "2", 3)
        self.draw_option_box(self.screen_width // 2 - 120 // 2, self.y + 450, 120, 60, "4", 3)
        self.draw_option_box(self.screen_width // 2 - 120 // 2, self.y + 520, 120, 60, "8", 3)

        self.draw_option_box(self.screen_width - self.x - 110,
                             self.screen_height - self.y - 110, 60, 60, "PLAY", 2)

    def draw_option_box(self, x, y, box_width, box_height, number, color_num):
        option_box_color = {1: (139,	109,	92),
                            2: (255, 0, 47),
                            3: (72, 100, 171)}
        box = pygame.Rect(x, y, box_width, box_height)
        self.option_button.append([box, number])
        pygame.draw.rect(self.mainscreen, option_box_color[color_num],
                         box, False, 15)
        self.draw_whatever(number, x, y, box_width, box_height)

    def draw_whatever(self, message, x, y, rect_width, rect_height, size=30):
        temp_font = pygame.font.SysFont('clear sans', size, bold=True)
        number = temp_font.render(str(message), True, (10, 10, 10))
        number_rect = number.get_rect()
        number_rect.center = (x + rect_width // 2, y + rect_height // 2)
        self.mainscreen.blit(number, number_rect)

    def draw_button_reaction(self, button, number='clicked', color=(105, 105, 105)):
        pygame.draw.rect(self.mainscreen, color, button, False, 15)
        self.draw_whatever(number, button.x, button.y, button.width, button.height)
        pygame.display.flip()




