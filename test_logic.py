import numpy as np
import settings
import random


class Logic2048:
    def __init__(self):
        self.grid = np.zeros(settings.matrix_size1, dtype=int)

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

    def play(self):
        self.generate_number(k=2)
        while True:
            print(self.grid)
            s = input()
            if s == 'q':
                break
            self.make_move(s)

if __name__ == '__main__':
    game = Logic2048()
    game.play()
