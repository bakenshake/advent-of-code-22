"""
Advent of Code - Day 3
Helper functions to reuse for puzzles - thanks Danielle Lucek!
"""
import timeit
from tokenize import group
from typing import List
import re

priorityList = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8,
    'i' : 9,
    'j' : 10,
    'k' : 11,
    'l' : 12,
    'm' : 13,
    'n' : 14,
    'o' : 15,
    'p' : 16,
    'q' : 17,
    'r' : 18,
    's' : 19,
    't' : 20,
    'u' : 21,
    'v' : 22,
    'w' : 23,
    'x' : 24,
    'y' : 25,
    'z' : 26,
    'A' : 27,
    'B' : 28,
    'C' : 29,
    'D' : 30,
    'E' : 31,
    'F' : 32,
    'G' : 33,
    'H' : 34,
    'I' : 35,
    'J' : 36,
    'K' : 37,
    'L' : 38,
    'M' : 39,
    'N' : 40,
    'O' : 41,
    'P' : 42,
    'Q' : 43,
    'R' : 44,
    'S' : 45,
    'T' : 46,
    'U' : 47,
    'V' : 48,
    'W' : 49,
    'X' : 50,
    'Y' : 51,
    'Z' : 52
}

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
    FILENAME = "data/3-input.txt"
    file_input = input_as_lines(FILENAME)
    prioritySum = 0
    for i in file_input:
        #print("Rucksack: " + i)
        compartmentOne = i[0:len(i)//2]
        compartmentTwo = i[len(i)//2 if len(i)%2 == 0 else ((len(i)//2)+1):]
        compartmentOne = list(compartmentOne)
        compartmentTwo = list(compartmentTwo)
        #print(compartmentOne)
        #print(compartmentTwo)
        k = 0
        itemFound = False
        while k != len(compartmentTwo):
            for j in compartmentOne:
                if j == compartmentTwo[k]:
                    item = j
                    #print("Item type found: " + item)
                    if item in priorityList:
                        prioritySum += priorityList.get(item)
                    itemFound = True
                    break
            if itemFound == True:
                break
            k += 1

    return prioritySum
        
def solution_part_2():
    FILENAME = "data/3-input.txt"
    file_input = input_as_lines(FILENAME)
    prioritySum = 0
    elfGroup = []
    groupCount = 0
    for i in file_input:
        groupCount +=1
        #print("Rucksack: " + i)
        elfGroup.append(i)
        
        if groupCount % 3 == 0:
            #print(groupCount)
            badge = intersection(elfGroup)
            #print(badge)
            prioritySum += priorityList.get(badge[0])
            if intersection(elfGroup) != []:
                elfGroup = []

    return prioritySum

def intersection(lists):
    allElements = lists[0]
    for i in range(1,len(lists)):
        allElements = [x for x in allElements if x in lists[i]]
    return allElements

print(f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10}s'
    )
print(f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=10)/10}s'
    )