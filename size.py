# Project 3.2.3 - Combo Menu Iteration with Loops
# Author: Fred Morrison
# Date written: 2023-03-16
# Description: An enum that controls the valid drink and french fry sizes
from enum import Enum, unique


@unique
class Size(Enum):
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
