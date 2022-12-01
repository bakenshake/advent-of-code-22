"""
Advent of Code - Day 1: ???
Helper functions to reuse for puzzles - thanks Danielle Lucek!
"""
import timeit
from collections import Counter
from typing import List

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

def part_one(file_input):
    singleElfRations = []
    currElf = 0
    for i in file_input:
        #print(i)
        if i != '':
            currElf += int(i)
        if i == '':
            #print("Elf with ration amount: " + str(currElf))
            singleElfRations.append(currElf)
            currElf = 0

    #print("Largest ration is:", max(singleElfRations))
    return singleElfRations

def part_two(elfRations):
    elfRations.sort()
    topThree = elfRations[-1] + elfRations[-2] + elfRations[-3]
    return topThree

def solution_part_1():
    FILENAME = "data/1-input.txt"
    file_input = input_as_lines(FILENAME)
    elfRations = part_one(file_input)
    return max(elfRations)

def solution_part_2():
    FILENAME = "data/1-input.txt"
    file_input = input_as_lines(FILENAME)
    elfRations = part_one(file_input)
    return part_two(elfRations)

print(f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10}s'
    )
print(f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=10)/10}s'
    )