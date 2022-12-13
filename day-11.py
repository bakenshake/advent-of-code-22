"""
Advent of Code - Day 11: Monkey in the Middle
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

"""
Constraints:
1. After each OPERATION but before a TEST, calculate relief (worry level divided by three and rounded down)
2. 
"""
def solution_part_1():
    FILENAME = "data/11-sample.txt"
    file_input = input_as_lines(FILENAME)
    monkey_group = []
    item_count = 0
    for i in file_input:
        monkey_data = re.split(r'\n{2,}', i)
        print(monkey_data)
        #monkey_name = re.findall("^Monkey \d+:",i)
        #starting_items = re.findall("Starting items: [\d+].*$", i)
        #print(starting_items)
        #operation = re.findall("Operation: new = old [\] [\w+\d+]+.", i)
        #print(operation)
        #test = re.findall("Test: divisible by [\d+]+.$", i)
        #print(test)
        #if_true = re.findall("If true: ",i)
        #if_false = re.findall("If false: ", i)
        #print(if_true)
        #print(if_false)
        #monkey_group.append(Monkey(monkey_name, starting_items, 0, operation, 0,  test, 0, if_true, if_false, item_count))
    
    #for j in monkey_group:
    #    print(j.monkey_name)
    #    print(j.starting_items)
    #    print(j.worry_level)

class Monkey:
    def __init__(self, monkey_name, starting_items, worry_level, operation, relief, test, new_items, if_true, if_false, item_count):
        self.monkey_name = monkey_name
        self.starting_items = starting_items 
        self.worry_level = worry_level
        self.operation = operation
        self.relief = relief
        self.test = test
        self.new_items = new_items
        self.if_true = if_true
        self.if_false = if_false
        self.item_count = item_count

    #def throw_items(self, items, relief):
    #    if

solution_part_1()

""" print(f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10}s'
    ) """