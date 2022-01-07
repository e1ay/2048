import numpy as np
import settings
import random


class Logic2048:
    def __init__(self):
        self.grid = np.zeros(settings.matrix_size1)

    def __str__(self):
        return str(self.grid)

    def generate_number(self, k=1):
        free_poss = list(zip(*np.where(self.grid == 0)))

        for pos in random.sample(free_poss, k=k):
            if random.random() < .1:
                self.grid[pos] = 4
            else:
                self.grid[pos] = 2


if __name__ == '__main__':
    game = Logic2048()
    game.generate_number(k=2)
    print(game)
