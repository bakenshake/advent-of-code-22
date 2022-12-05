"""
Advent of Code - Day 5: Supply Stacks
Helper functions to reuse for puzzles - thanks Danielle Lucek!
"""
import timeit
from typing import List
import re
import numpy

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

"""crate1 = ['Z', 'N']
crate2 = ['M', 'C', 'D']
crate3 = ['P']
crates = [crate1, crate2, crate3] 
"""
crate1 = ['Z', 'J', 'N', 'W', 'P', 'S']
crate2 = ['G', 'S', 'T']
crate3 = ['V', 'Q', 'R', 'L', 'H']
crate4 = ['V', 'S', 'T', 'D']
crate5 = ['Q', 'Z', 'T', 'D', 'B', 'M', 'J']
crate6 = ['M', 'W', 'T', 'J', 'D', 'C', 'Z', 'L']
crate7 = ['L', 'P', 'M', 'W', 'G', 'T', 'J']
crate8 = ['N', 'G', 'M', 'T', 'B', 'F', 'Q', 'H']
crate9 = ['R', 'D', 'G', 'C', 'P', 'B', 'Q', 'W']
crates = [crate1, crate2, crate3, crate4, crate5, crate6, crate7, crate8, crate9]

def solution_part_1():
    FILENAME = "data/5-input.txt"
    file_input = input_as_lines(FILENAME)
    print(crates)
    topOfStacks = []
    for i in file_input:
        numbers = re.findall("\d+",i)
        print(numbers)
        cratesToMove = int(numbers[0])
        fromStack = int(numbers[1])
        toStack = int(numbers[2])
        print("Moving crates: " + numbers[0])
        print("From stack #: " + numbers[1])
        print("To stack #: " + numbers[2])
        #print(crates[fromStack-1])
        #print(len(crates[fromStack-1]))

        while cratesToMove != 0:
            crates[toStack-1].append(crates[fromStack-1][len(crates[fromStack-1])-1])
            crates[fromStack-1].pop()
            cratesToMove -= 1
            
    iterator = 0
    while iterator != len(crates):
        topOfStacks.append(crates[iterator][len(crates[iterator])-1])
        iterator += 1

    print(crates)
    print("----------")
    print(topOfStacks)

def solution_part_2():
    FILENAME = "data/5-input.txt"
    file_input = input_as_lines(FILENAME)
    #print(crates)
    topOfStacks = []
    for i in file_input:
        numbers = re.findall("\d+",i)
        #print(numbers)
        cratesToMove = int(numbers[0])
        fromStack = int(numbers[1])
        toStack = int(numbers[2])
        print("Moving crates: " + numbers[0])
        print("From stack #: " + numbers[1])
        print("To stack #: " + numbers[2])
        itemsToRemove = cratesToMove
        #print(crates[fromStack-1])
        #print(crates[toStack-1])
        print(crate1)
        print(crate2)
        print(crate3)
        print(crate4)
        print(crate5)
        print(crate6)
        print(crate7)
        print(crate8)
        print(crate9)
        print("--------------------")

        #move to stack
        while cratesToMove != 0:
            crates[toStack-1].append(crates[fromStack-1][len(crates[fromStack-1])-cratesToMove])
            cratesToMove -= 1

        #remove from old stack
        while itemsToRemove != 0:
            if len(crates[fromStack-1]) != 0:
                crates[fromStack-1].pop()
                itemsToRemove -= 1
        
        #print(crates[fromStack-1])
        #print(crates[toStack-1])
        print(crate1)
        print(crate2)
        print(crate3)
        print(crate4)
        print(crate5)
        print(crate6)
        print(crate7)
        print(crate8)
        print(crate9)
            
    iterator = 0
    while iterator != len(crates):
        topOfStacks.append(crates[iterator][len(crates[iterator])-1])
        iterator += 1

    print(crates)
    print("----------")
    print(topOfStacks)

#solution_part_1()
solution_part_2()

""" print(f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10}s'
    )
print(f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=10)/10}s'
    ) """