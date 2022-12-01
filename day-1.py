"""
Advent of Code - Day 1: ???
Helper functions to reuse for puzzles - thanks Danielle Lucek!
"""
import re
from collections import Counter
from typing import List

def input_as_string(filename:str) -> str:
    """returns the content of the input file as a string"""
    with open(filename) as file_to_open:
        return file_to_open.read().rstrip("\n")

def input_as_lines(filename:str) -> List[str]:
    """Return a list where each line in the input file is an element of the list"""
    return input_as_string(filename).split("\n")

def input_as_ints(filename:str) -> List[int]:
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    lines = input_as_lines(filename)
    line_as_int = lambda l: int(l.rstrip('\n'))
    return list(map(line_as_int, lines))

FILENAME = "data/AoC-1.txt"
file_input = input_as_lines(FILENAME)
print(file_input)