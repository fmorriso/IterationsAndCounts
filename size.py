# Project 3.2.3 - Combo Menu Iteration with Loops
# Author: Fred Morrison
# Date written: 2023-03-16
# Description: An enum that controls the valid drink and french fry sizes
# NOTES:
# 1. The string value can be access via the built-in .value property, such as:
#    Size.SMALL.value which will yield 'small', which eliminates the need to use
#    "magic strings" in assignment and equality statements..
from enum import Enum, unique


@unique
class Size(Enum):
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
