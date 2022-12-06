"""
Advent of Code - Day 6
Helper functions to reuse for puzzles - thanks Danielle Lucek!
"""
import timeit
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

def solution_part_1():
    FILENAME = "data/6-input.txt"
    file_input = input_as_string(FILENAME)
    #print(file_input)
    marker = []
    signal = []
    for i in file_input:
        #print(i)
        signal.append(i)
    #print(signal)

    markerFound = False
    iterator = 0
    steps = 0
    while markerFound != True:
        while len(marker) != 4:
            marker.append(signal[iterator])
            iterator+=1
            #print(marker)

            #check marker against
            if len(marker) == 4:
                steps += 1
                duplicates = [num for num in marker if marker.count(num) > 1]
                check_dupes = list(set(duplicates))
                #print(check_dupes)
                if check_dupes == []:
                    markerFound = True
                    #print(steps)
                else:
                    marker = []
                    iterator = 0
                    iterator += steps
                #print('--------------')

    return steps+3

def solution_part_2():
    FILENAME = "data/6-input.txt"
    file_input = input_as_string(FILENAME)
    #print(file_input)
    marker = []
    signal = []
    for i in file_input:
        #print(i)
        signal.append(i)
    #print(signal)

    markerFound = False
    iterator = 0
    steps = 0
    while markerFound != True:
        while len(marker) != 14:
            marker.append(signal[iterator])
            iterator+=1
            #print(marker)

            #check marker against
            if len(marker) == 14:
                steps += 1
                duplicates = [num for num in marker if marker.count(num) > 1]
                check_dupes = list(set(duplicates))
                #print(check_dupes)
                if check_dupes == []:
                    markerFound = True
                    #print(steps)
                else:
                    marker = []
                    iterator = 0
                    iterator += steps
                #print('--------------')

    return steps+13

print(f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10}s'
    )
print(f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=10)/10}s'
    )