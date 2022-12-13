"""
Advent of Code - Day 12
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
}

def solution_part_1():
    FILENAME = "data/12-sample.txt"
    file_input = input_as_lines(FILENAME)
    print(file_input)
    row = 0
    start = [0,0]
    end = [0,0]
    grid = []
    for i in file_input:
        for j in (range(0, len(i))):
            #print(i[j])
            if i[j] == 'S':
                #print("found starting point")
                start[0] = row
                start[1] = j
            if i[j] == 'E':
                #print("found end")
                end[0] = row
                end[1] = j
        row += 1
    
    #distance_to_end = abs(abs(end[0] - start[0]) - abs(end[1] - start[1]))
    print(start)
    print(end)
    #print(distance_to_end)

def bfs(grid, start, end):
    #queue to track BFS 
    queue = []
    queue.append(start)

    #mark all nodes as unvisited
    visited = [False] * (max(grid) + 1)
    #start has been visited
    visited[start] = True

    while queue:
        node = queue.pop(len(queue)-1)
        if node == end:
            return node

        adjacent = [(-1, 0), (0, 1), (0, -1), (1, 0)]
        for i in grid[node]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True


solution_part_1()