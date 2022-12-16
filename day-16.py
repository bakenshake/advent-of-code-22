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
    FILENAME = "data/16-sample.txt"
    file_input = input_as_lines(FILENAME)
    
    #parse valves and flow rates
    valve_and_flow = {}
    tunnels = []
    for i in file_input:
        flow = re.findall("\d+", i)
        flow_rate = int(flow[0]) #remove as list and convert to int
        #print(flow)
        valve = i[6] + i[7]
        #print(valve)
        valve_and_flow.update({valve : flow_rate}) #put in a set
        valve_tunnel = re.findall("[A-Z][A-Z]+", i)
        tunnels.append(valve_tunnel)
    
    print(valve_and_flow)
    print(tunnels)

solution_part_1()