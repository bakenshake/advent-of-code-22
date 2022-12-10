"""
Advent of Code - Day 10
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
    FILENAME = "data/10-input.txt"
    file_input = input_as_lines(FILENAME)

    #create the grid
    crt_screen = create_grid(40, 6)
    #print_grid(crt_screen)
    print("---------------------------------")
    #flatten into one big line
    #crt_screen = [ele for crt_screen in crt_screen for ele in crt_screen]
    
    cycle = 0
    register_x = 1
    row = 0
    signal_strength = 0
    all_signals = []
    sprite = '#' #draw what X equals to and +1 and -1 to draw the full sprite
    for i in file_input:
        if i == "noop":
            cycle += 1
            draw_pixel(cycle, crt_screen, register_x, sprite, row)
            if check_signal(cycle) == 1:
                row += 1
        else:
            if re.search('-', i):
                add_cycle = re.findall("-\d+", i)
                cycle += 1
                draw_pixel(cycle, crt_screen, register_x, sprite, row)
                if check_signal(cycle) == 1:
                    #signal_strength = register_x * cycle
                    #all_signals.append(signal_strength)
                    row += 1
                cycle += 1
                draw_pixel(cycle, crt_screen, register_x, sprite, row)
                #draw pixel
                if check_signal(cycle) == 1:
                    #signal_strength = register_x * cycle
                    #all_signals.append(signal_strength)
                    row += 1
            else:
                add_cycle = re.findall("\d+", i)
                cycle += 1
                draw_pixel(cycle, crt_screen, register_x, sprite, row)
                #draw pixel
                if check_signal(cycle) == 1:
                    #signal_strength = register_x * cycle
                    #all_signals.append(signal_strength)
                    row += 1
                cycle += 1
                draw_pixel(cycle, crt_screen, register_x, sprite, row)
                #draw pixel
                if check_signal(cycle) == 1:
                    #signal_strength = register_x * cycle
                    #all_signals.append(signal_strength)
                    row += 1
            
            register_x += int(add_cycle[0])

    #print(crt_screen)
    print_screen(crt_screen)
    #print(all_signals)
    #total = 0
    #for k in range(0,len(all_signals)):
    #    total += all_signals[k]

    #print(total)

def print_screen(crt_screen):
    row = []
    readout = []
    for j in range(0, len(crt_screen)):
        for k in range(0,len(crt_screen)):
            row = ''.join(crt_screen[j])
        print(row)
        row = []

    
def check_signal(cycle):
    if (cycle == 40) or (cycle == 80) or (cycle == 120) or (cycle == 160) or (cycle == 200) or (cycle == 240):
        return 1
    else:
        return -1

def draw_pixel(cycle, crt_screen, register_x, sprite, row):
    cycle_adjuster = cycle
    if row == 1:
        cycle_adjuster -= 40
    elif row == 2:
        cycle_adjuster -= 80
    elif row == 3:
        cycle_adjuster -= 120
    elif row == 4:
        cycle_adjuster -= 160
    elif row == 5:
        cycle_adjuster -= 200
    elif row == 6:
        cycle_adjuster -= 240

    if ((cycle_adjuster-1) == (register_x-1)) or ((cycle_adjuster-1) == register_x) or ((cycle_adjuster-1) == (register_x+1)):
        crt_screen[row][cycle_adjuster-1] = sprite        

def create_grid(horizontal, vertical):
    grid = [[i for i in range(horizontal)] for n in range(vertical)]

    for idx_x in range(0,vertical):
        for idx_y in range(0, horizontal):
            grid[idx_x][idx_y] = '.'

    return grid

def print_grid(grid):
    #print grid
    for idx_x, idx_y in enumerate(grid):
        print(idx_x, idx_y)

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