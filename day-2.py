"""
Advent of Code - Day 1: ???
Helper functions to reuse for puzzles - thanks Danielle Lucek!
"""
import timeit
from typing import List
import re

def input_as_string(filename:str) -> str:
    """returns the content of the input file as a string"""
    with open(filename) as f:
        return f.read().rstrip("\n")

def input_as_lines(filename:str) -> List[str]:
    """Return a list where each line in the input file is an element of the list"""
    return input_as_string(filename).split("\n")

def input_as_ints(filename:str) -> List[int]:
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    lines = input_as_lines(filename)
    line_as_int = lambda l: int(l.rstrip('\n'))
    return list(map(line_as_int, lines))

def solution_part_1():
    FILENAME = "data/2-input.txt"
    file_input = input_as_lines(FILENAME)
    score = 0
    for i in file_input:
        if i == 'A X':
            score += 4
        elif i == 'A Y':
            score += 8
        elif i == 'A Z':
            score += 3
        elif i == 'B X':
            score += 1
        elif i == 'B Y':
            score += 5
        elif i == 'B Z':
            score += 9
        elif i == 'C X':
            score += 7
        elif i == 'C Y':
            score += 2
        elif i == 'C Z':
            score += 6
    return score

def solution_part_2():
    FILENAME = "data/2-input.txt"
    file_input = input_as_lines(FILENAME)
    # X means lose, Y means draw, Z means win
    score = 0
    for i in file_input:
        #print(i)
        rounds = re.split(' ', i)
        if rounds[1] == 'X':
            #print("lose")
            if rounds[0] == 'A':
                score += 3
            elif rounds[0] == 'B':
                score += 1
            elif rounds[0] == 'C':
                score += 2
        elif rounds[1] == 'Y':
            #print("draw")
            if rounds[0] == 'A':
                score += 4
            elif rounds[0] == 'B':
                score += 5
            elif rounds[0] == 'C':
                score += 6
        elif rounds[1] == 'Z':
            #print("win")
            if rounds[0] == 'A':
                score += 8
            elif rounds[0] == 'B':
                score += 9
            elif rounds[0] == 'C':
                score += 7
        #print("Current score: " + str(score))
    return score

print(f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10}s'
    )
print(f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=10)/10}s'
    )