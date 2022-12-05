"""
Advent of Code - Day 4: Camp Cleanup
Helper functions to reuse for puzzles - thanks Danielle Lucek!
"""
from operator import indexOf
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
    FILENAME = "data/4-sample.txt"
    file_input = input_as_lines(FILENAME)
    print(file_input)
    elfPair = []
    elfOneRange = 0
    elfTwoRange = 0
    sectionOneWork = []
    sectionTwoWork = []
    rangeCovered = 0
    noneDuplicated = 0
    for i in file_input:
        assignments = i.split(',')
        #print(assignments)
        for j in assignments:
            range = j.split('-')
            #print(range)
            elfPair.append(range)
            if assignments.index(j) % 2 != 0:
                print(elfPair)
                elfOneRange = int(elfPair[0][0])
                while elfOneRange <= int(elfPair[0][1]):
                    sectionOneWork.append(elfOneRange)
                    elfOneRange += 1
                print(sectionOneWork)

                elfTwoRange = int(elfPair[1][0])
                while elfTwoRange <= int(elfPair[1][1]):
                    sectionTwoWork.append(elfTwoRange)
                    elfTwoRange += 1
                print(sectionTwoWork)
                
                overlap = list(set(sectionOneWork).intersection(set(sectionTwoWork)))
                print(overlap)
                intersect = [x for x in sectionOneWork if x in sectionTwoWork]
                print(intersect)

                if len(overlap) == len(sectionOneWork):
                    print("elf one work duped")
                    rangeCovered += 1
                    print("Ranges overlapped: " + str(rangeCovered))
                elif len(overlap) == len(sectionTwoWork):
                    print("elf two work duped")
                    rangeCovered +=1     
                    print("Ranges overlapped: " + str(rangeCovered))
                else:
                    print("")
                    noneDuplicated +=1
                
                #reset it all
                elfOneRange = 0
                sectionOneWork = []
                elfTwoRange = 0
                sectionTwoWork = []
                elfPair = []
    
    print("No dupes: " + str(noneDuplicated))
    print("Ranges duped: " + str(rangeCovered))
    print("Number of pairs: " + str(len(file_input)))
    return rangeCovered

def solution_part_2():
    FILENAME = "data/4-sample.txt"
    file_input = input_as_lines(FILENAME)

print(solution_part_1())

""" print(f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10}s'
    )
print(f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=10)/10}s'
    ) """