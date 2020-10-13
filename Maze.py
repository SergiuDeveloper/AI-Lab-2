#!/usr/bin/python3.8

import numpy as np

from enum import Enum
from typing import Tuple


class Maze(object):
    class __TransitionDirection(Enum):
        UP = 1,
        DOWN = 2,
        LEFT = 3,
        RIGHT = 4

    def __init__(self,
                 maze_matrix: np.ndarray,
                 starting_position: Tuple[int, int],
                 destination_position: Tuple[int, int]
                 ):
        self.__maze_matrix = maze_matrix

        self.__starting_position = starting_position
        if not self.__is_valid_state(self.__starting_position):
            raise Exception("Invalid starting position")

        self.__destination_position = destination_position
        if not self.__is_valid_state(self.__destination_position):
            raise Exception("Invalid destination position")

        self.__current_position = starting_position

    def __perform_transition(self, current_position: Tuple[int, int], transition_direction: __TransitionDirection):
        desired_position = current_position

        if transition_direction == Maze.__TransitionDirection.UP:
            desired_position[0] += 1
        elif transition_direction == Maze.__TransitionDirection.DOWN:
            desired_position[0] -= 1
        elif transition_direction == Maze.__TransitionDirection.LEFT:
            desired_position[1] -= 1
        elif transition_direction == Maze.__TransitionDirection.RIGHT:
            desired_position[1] += 1
        else:
            return None

        if not self.__is_valid_state(desired_position):
            return None

        return desired_position

    def __is_valid_state(self, desired_position: Tuple[int, int]):
        x = desired_position[0]
        y = desired_position[1]

        if not 0 <= x < self.__maze_matrix.shape[0]:
            return False
        if not 0 <= y < self.__maze_matrix.shape[1]:
            return False

        if not self.__maze_matrix[x, y]:
            return False

        return True

    def __is_final_state(self):
        return self.__current_position == self.__destination_position
