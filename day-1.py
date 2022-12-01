"""
Advent of Code - Day 1: ???
Helper functions to reuse for puzzles - thanks Danielle Lucek!
"""
import numpy
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

def parse_input(file_input):
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

    return singleElfRations

FILENAME = "data/1-input.txt"
file_input = input_as_lines(FILENAME)
#print(file_input)
elfRations = parse_input(file_input)
print("Largest ration is:", max(elfRations))

### PART TWO ###

elfRations.sort()
print("Top 3 elves carrying most rations are: \n" + "1." + str(elfRations[-1]) + "\n" + "2." + str(elfRations[-2]) + "\n" + "3." + str(elfRations[-3]))
topThree = elfRations[-1] + elfRations[-2] + elfRations[-3]
print("Top 3 elves combined: " + str(topThree))
