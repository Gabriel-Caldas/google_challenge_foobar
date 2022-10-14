from sys import path
import numpy as np


map =  np.array([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
map = np.array([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])

h = map.shape[0]
w = map.shape[1]

min_legth = (h-1)+(w-1)

directions = 2
