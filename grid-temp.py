"""
Advent of Code - Day 9: Rope Bridge
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
    FILENAME = "data/9-sample.txt"
    file_input = input_as_lines(FILENAME)
    high_num = 0

    #find length of the grid
    for i in file_input:
        num = re.findall("\d+",i)
        if high_num == 0:
            high_num = num
        elif num > high_num:
            high_num = num

    #create the grid
    grid_length = int(high_num[0])
    grid = create_grid(grid_length)
    print_grid(grid)

    #init starting positions
    head = {}
    tail = {}
    start = {}
    head, tail, start = init_rope(grid, grid_length)

def init_rope(grid, grid_length):
    head = {(0,grid_length)}
    tail = {(0,grid_length)}
    start = tail

    return head, tail, start

def create_grid(high_num):
    grid = [[i for i in range(high_num)] for n in range(high_num)]

    for idx_x in range(0,len(grid)):
        for idx_y in range(0, len(grid)):
            grid[idx_x][idx_y] = '.'

    return grid

def print_grid(grid):
    #print grid
    for idx_x, idx_y in enumerate(grid):
        print(idx_x, idx_y)

def solution_part_2():
    FILENAME = "data/9-sample.txt"
    file_input = input_as_lines(FILENAME)

solution_part_1()

""" print(f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10}s'
    )
print(f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=10)/10}s'
    ) """