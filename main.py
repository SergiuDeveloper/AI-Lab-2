#!/usr/bin/python3.8

import numpy as np
import warnings

from Maze import Maze


if __name__ == '__main__':
    warnings.simplefilter('ignore', DeprecationWarning)

    file = open('Generator/maze-generator/maze.txt', mode='r')

    file_content = file.read().split()
    file.close()

    maze_x_size = int(file_content[0])
    maze_y_size = int(file_content[1])
    maze_matrix = np.fromstring(file_content[2], dtype=bool, sep=',')
    maze_matrix = maze_matrix.reshape((maze_x_size, maze_y_size))

    print(maze_matrix)

    maze = Maze(maze_matrix, (13, 15), (14, 25), maze_x_size, maze_y_size)
