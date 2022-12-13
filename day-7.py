"""
Advent of Code - Day 7
Helper functions to reuse for puzzles - thanks Danielle Lucek!
"""
from calendar import prweek
from logging import root
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

def solution_part_2():
    FILENAME = "data/1-input.txt"
    file_input = input_as_lines(FILENAME)

def solution_part_1():
    FILENAME = "data/7-input.txt"
    file_input = input_as_lines(FILENAME)
    #print(file_input)
    all_directories = []
    dir_value_pairs = {}
    dir = "root"
    parentDir = ''
    for i in file_input:
        commands = re.findall('^\$', i) #matching commands
        directories = re.findall('^dir \w+', i)
        #print(i)
        if len(commands) > 0:
            #do the action
            #print(i)
            comm = i.find('cd')
            if comm > 0:
                cd = i[len(i)-1]
                #print(cd)
                if cd != '.' and cd != '/':
                    #dir change in
                    prevDir = dir
                    parentDir = dir
                    #print("--prev dir: " + prevDir)
                    dir = i.replace("$ cd ", "")
                    #print("--dir changed to: " + dir)
                    if dir not in all_directories:
                        newDir = []
                        newDir.append(dir)
                        all_directories.append(newDir)
                        multiple_children = False
                elif cd != '/':
                    #dir change out
                    #print("--dir change out")
                    dir = all_directories[len(all_directories)-1]
                    #print("--dir changed to: " + dir)
                    multiple_children = False
                elif cd == '/':
                    dir = "root"
                    #print("--root")                 
        elif len(directories) > 0:
            #this dir is a child of a dir
            if dir != "root":
                dirChild = i.replace("dir ", "")
                if multiple_children == False:
                    dir_idx = all_directories.index([dir])
                all_directories[dir_idx].append(dirChild)
                multiple_children = True
            if dir == "root" and dir not in all_directories: #for the first dir only
                newDir = []
                newDir.append(dir)
                all_directories.append(newDir)
                multiple_children = False
            #print(dir)
            #print("--curr dir: " + dir)
        else:
            #add the file size to the current directory
            #print("--file listed in directory: " + dir)
            directory_size = re.findall("\d+", i)
            join = ""
            directory_size = join.join(directory_size)
            #print("--dir file size is: " + directory_size)
            dir_value_pairs[directory_size] = dir
    
    print("-----------------------")
    print(all_directories)
    dir_totals = total_directories(dir_value_pairs)
    print("-----------------------")
    print(dir_totals)
    for i in range(0, len(all_directories)):
        if all_directories[i][0] == "root":
            all_directories[i].pop(0)
        else:
            for j in range(0, len(all_directories[i])):
                dir_to_pull = all_directories[i][j]
                all_directories[i][j] = dir_totals.get(dir_to_pull)
                if all_directories[i][j] == None:
                    all_directories[i][j] = 0
            
    dir_sum = [sum(x) for x in all_directories]
    print(all_directories)
    print(dir_sum)

    total = 0
    for j in range(0, len(dir_sum)):
        if dir_sum[j] < 100000:
            total += dir_sum[j]

    print(total)

def total_directories(dir_value_pairs):
    
    #remove all root entries
    dir_value_pairs = {key:val for key, val in dir_value_pairs.items() if val != "root"}
    #print(dir_value_pairs)
    
    dir_totals = {}

    for key, value in dir_value_pairs.items():
        dir_totals.update({value : 0})


    #print(dir_totals)    

    #convert to nested list
    dir_value_pairs_list = list(dir_value_pairs.items())
    #print(dir_value_pairs_list)
    total = 0

    for i in range(0, len(dir_value_pairs_list)):
        #print(dir_value_pairs_list[i][0])
        if i == 0:
            start_dir = dir_value_pairs_list[i][1]
        
        if start_dir == dir_value_pairs_list[i][1]:
            total += int(dir_value_pairs_list[i][0])
            #print(start_dir, total)
            if i < len(dir_value_pairs_list)-1 and dir_value_pairs_list[i+1][1] != start_dir:
                #add total to dir_totals
                dir_totals.update({start_dir:total})
            if i == len(dir_value_pairs_list)-1:
                dir_totals.update({start_dir:total})
        else:
            start_dir = dir_value_pairs_list[i][1]
            total = 0
            total += int(dir_value_pairs_list[i][0])
            #print(start_dir, total)
            dir_totals.update({start_dir:total})
            start_dir = dir_value_pairs_list[i+1][1]
            total = 0 
    
    #print(dir_totals)

    return dir_totals
            
solution_part_1()

""" print(f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10}s'
    )
print(f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=10)/10}s'
    ) """