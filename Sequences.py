import math
import numpy as np


class Sequences:
    def __init__(self, members):
        self.members = members

    def combinations(self):
        combos = np.empty((0, 2), int)
        for i in range(len(self.members)):
            for j in self.members:
                if i != j:
                    combos = np.append(combos, np.array([[i, j]]), axis=0)

        return combos
