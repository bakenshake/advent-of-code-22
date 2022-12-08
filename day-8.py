"""
Advent of Code - Day 8: Treetop Tree House
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
    FILENAME = "data/8-sample.txt"
    file_input = input_as_lines(FILENAME)
    row = []
    grid = []
    gridLength = 0
    rowCount = 0
    for i in file_input:
        iterator = 0
        gridLength = len(i)
        for ch in i:
            row.append(ch)
            iterator +=1
            if iterator == gridLength:
                grid.append(row)
                row = []
        rowCount+=1

    print(rowCount)
    #print(grid)
    #print("grid length is: "+str(gridLength))
    
    check_visibility(grid, gridLength, rowCount)

def check_visibility(grid, gridLength, rowCount):

    #print grid
    for index, tree in enumerate(grid):
        print(index, tree)
        gridLength = len(tree)

    trees = 0
    for row in range(0, len(grid)):
        for col in range(0,len(grid)):
            if parse_trees(grid, gridLength, row, col) == 1:
                trees += 1
            #print("Trees visible: "+str(trees))
    
    gridLength = gridLength*2
    rowCount = rowCount*2
    edgeTrees = (gridLength + rowCount)-4
    print("Interior trees: " +str(trees))
    print("Edge trees: "+str(edgeTrees))
    print("Grid length: " +str(gridLength))
    print("Row count: " +str(rowCount))
    trees += edgeTrees
    print("Total Trees: "+str(trees))

def parse_trees(grid, gridLength, row, col):
    directions = {'left': 0, 'right': 0, 'above': 0, 'below': 0} #0 means not visible, 1 means visible
    print("Current tree: "+grid[row][col]+ " at row: " +str(row)+" col: "+str(col))
    #add a bounds check
    if (row != 0 and col != 0) and (row != gridLength-1 and col != gridLength-1):
        if grid[row][col] > grid[row][col+1]: #to the right
            print("front is smaller")
            if row != 0 or row != gridLength-1:
                col +=1
                return parse_trees(grid, gridLength, row, col)
        elif grid[row][col] > grid[row][col-1]: #looking behind
            print("back is smaller")
            if row != 0 or row != gridLength-1:
                col -=1
                return parse_trees(grid, gridLength, row, col)
        elif grid[row][col] > grid[row+1][col]: #below
            print("below is smaller")
            if col != 0 or col != gridLength-1:
                row += 1
                parse_trees(grid, gridLength, row, col)
        elif grid[row][col] > grid[row-1][col]: #above
            print("above is smaller")
            if col != 0 or col != gridLength-1:
                row -= 1
                parse_trees(grid, gridLength, row, col)
        else: #must be viable from that path
            print("tree visible")
            return 1
    
        
        

def solution_part_2():
    FILENAME = "data/1-input.txt"
    file_input = input_as_lines(FILENAME)

solution_part_1()

""" print(f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10}s'
    )
print(f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=10)/10}s'
    ) """