"""
Advent of Code - Day 7
Helper functions to reuse for puzzles - thanks Danielle Lucek!
"""
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

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = [] # references to other nodes

  def add_child(self, child_node):
    # creates parent-child relationship
    print("Adding " + child_node.value)
    self.children.append(child_node) 
    
  def remove_child(self, child_node):
    # removes parent-child relationship
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children 
                     if child is not child_node]

  def traverse(self):
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children

def solution_part_1():
    FILENAME = "data/7-sample.txt"
    file_input = input_as_lines(FILENAME)
    #print(file_input)
    all_directories = []
    dir_value_pairs = {}
    dir = "root"
    for i in file_input:
        commands = re.findall('^\$', i) #matching commands
        directories = re.findall('^dir', i)
        print(i)
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
                    print("--prev dir: " + prevDir)
                    dir = cd
                    print("--dir changed to: " + dir)
                    if dir not in all_directories:
                        all_directories.append(dir)
                elif cd != '/':
                    #dir change out
                    print("--dir change out")
                    print(all_directories)
                    dir = all_directories[len(all_directories)-1]
                    print("--dir changed to: " + dir)
                elif cd == '/':
                    dir = "root"
                    print("--root")                 
            else:
                print("--list")
        elif len(directories) > 0:
            #this dir is a child of a dir
            if dir != "root":
                dirChild = i[len(i)-1]
                print("--dir child: "+dirChild)
            if dir == "root":
                all_directories.append(dir)
            #print(dir)
            print("--curr dir: " + dir)
        else:
            #add the file size to the current directory
            print("--file listed in directory: " + dir)
            directory_size = re.findall("\d+", i)
            join = ""
            directory_size = join.join(directory_size)
            print("--dir file size is: " + directory_size)
            dir_value_pairs[directory_size] = dir
    
    #calculate_file_size(all_directories, dir_value_pairs)
    print(all_directories)
    print(dir_value_pairs)

def calculate_file_size(dirs, dir_pairs):
    dir_totals = {}
    total = 0
    iterator = 0
    for key in dir_pairs:
        print("Key: "+key+" ----- Value: "+dir_pairs[key])
        if dir_pairs[key] == dirs[iterator]:
            print(dir_pairs[key])
            print(dirs[iterator])
            total += int(key)
            dir_totals[dir_pairs[key]] = total
            print(total)
        else:
            total = 0
            iterator +=1

    print(dir_totals)
            
solution_part_1()

""" print(f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10}s'
    )
print(f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=10)/10}s'
    ) """