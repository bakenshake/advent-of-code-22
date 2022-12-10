"""
Advent of Code - Day 9: Rope Bridge
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

1. If the H is ever 2 steps up, down, left, or right from the T, the T must move one step in THAT direction to be close enough
    - Check through each move and update T, not after each row of moves
    - If the H is diagonally away, it could still be touching
2. If the H and T are not touching AND are not in the same row, the T moves one step closer diagonally
    - Moves to match the row that H is in, column stays the same AND if it's 2 away
3. H can cover T
4. Mark all positions T touched AT LEAST ONCE, including the starting position
"""


def solution_part_1():
    FILENAME = "data/9-sample.txt"
    file_input = input_as_lines(FILENAME)
    print(file_input)

    #init starting positions
    head = [0,0]
    tail = [0,0]
    start = [0,0]
    tail_positions = set()
    tails = []
    print(head, tail, start)

    for j in range(0, 9, 1):
        new_tail = [0,0]
        tails.append(new_tail)
    
    print(tails)

    for i in file_input:
        move = re.findall("^\w", i)
        num = re.findall("\d+",i)
        iterator = int(num[0])
        print("-------------------")
        while iterator != 0:
            prev_head = head
            if move[0] == 'R':
                #step
                head[1] += 1
                #check T distance
                if check_tail(head, tail, prev_head, move[0], tails) == 1:
                    print("move tail")
                iterator -= 1
            elif move[0] == 'L':
                head[1] -= 1
                if check_tail(head, tail, prev_head, move[0], tails) == 1:
                    print("move tail")
                iterator -= 1
            elif move[0] == 'U':
                head[0] += 1
                if check_tail(head, tail, prev_head, move[0], tails) == 1:
                    print("move tail")
                iterator -= 1
            elif move[0] == 'D':
                head[0] -= 1
                if check_tail(head, tail, prev_head, move[0], tails) == 1:
                    print("move tail")
                iterator -= 1

            tail_positions.add((tail[0], tail[1]))
            #print(tail_positions)
            print(head, tail)
    
    unique_positions = []
    [unique_positions.append(x) for x in tail_positions if x not in unique_positions]
    print(unique_positions)
    print(len(unique_positions))

def check_tail(head, tail, prev_head, move, tails):
    print(move)

    iter_head = tail #set current tail to be the next head
    next_tail = tails[j] #set the tail to be the tail after the current one
    if ((abs(head[0] - tail[0])) >= 2) and move == 'U': #moving up
        print("x value needs adjusted")
        tail[0] += 1
        tail[1] = head[1]
        return 1
    elif ((abs(head[1] - tail[1])) >= 2) and move == 'R': #moving right
        print("y needs adjusted")
        tail[1] += 1
        tail[0] = head[0]
        return 1
    elif ((abs(head[0] - tail[0])) >= 2) and move == 'D': #moving down 
        print("x value needs adjusted")
        tail[0] -= 1
        tail[1] = head[1]
        return 1
    elif ((abs(head[1] - tail[1])) >= 2) and move == 'L': #moving left
        print("y needs adjusted")
        tail[1] -= 1
        tail[0] = head[0]
        return 1
    elif (head[0] == tail[1]) and (head[1] == tail[0]):
        print("diagonally apart")
        tail = prev_head
        return 0
    else:
        return -1 #head and tail are close enough

def solution_part_2():
    FILENAME = "data/9-sample.txt"
    file_input = input_as_lines(FILENAME)

solution_part_1()

""" print(f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10}s'
    )
print(f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=10)/10}s'
    ) """