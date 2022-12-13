"""
Advent of Code - Day 13
Helper functions to reuse for puzzles - thanks Danielle Lucek!
"""
import timeit
from typing import List
import re
import math
from queue import PriorityQueue

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
    FILENAME = "data/13-sample.txt"
    file_input = input_as_lines(FILENAME)
    print(file_input)
    pair = []
    left = ''
    right = ''
    all_pairs = []
    possible_ints = [0,1,2,3,4,5,6,7,8,9,10]
    for i in file_input:
        #print(i)
        if i != '':
            pair.append(i)
        if len(pair) == 2:
            #print("examine pair")
            left = pair[0]
            right = pair[1]
            pair = []
            all_pairs.append(eval(left))
            all_pairs.append(eval(right))
            #pair_one = []
            #pair_two = []
            #temp_list = []
            #for j in range(0, len(left)):
                #if left[j] == '[':
                    #start a new list
                    #if j != len(left):
                        #temp_list = []
                #elif left[j] == ']':
                    #end a list
                    #pair_one.append(temp_list)
                    #print(pair_one)
                    #print("list")
                    #if j != len(left):
                        #temp_list = []
                #elif left[j] == ',':
                    #new number or list or bracket - look ahead
                    #continue
                #elif int(left[j]) in possible_ints:
                    #print("it's a number")
                    #temp_list.append(int(left[j]))
                    #print(temp_list)
                    #if int(left[j]) < int(right[j]):
                    #    print("left is smaller")
                    #    index += j 
                    #    index += clean_idx
                    #    print("index for right ordered pair: " +str(index))
    print(all_pairs)

solution_part_1()