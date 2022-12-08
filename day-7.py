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
    FILENAME = "data/7-input.txt"
    file_input = input_as_lines(FILENAME)
    #print(file_input)
    all_directories = []
    dir_value_pairs = {}
    dir = "root"
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
                    #print("--prev dir: " + prevDir)
                    dir = i.replace("$ cd ", "")
                    #print("--dir changed to: " + dir)
                    if dir not in all_directories:
                        all_directories.append(dir)
                elif cd != '/':
                    #dir change out
                    #print("--dir change out")
                    dir = all_directories[len(all_directories)-1]
                    #print("--dir changed to: " + dir)
                elif cd == '/':
                    dir = "root"
                    #print("--root")                 
        elif len(directories) > 0:
            #this dir is a child of a dir
            if dir != "root":
                dirChild = i.replace("dir ", "")
                #print("--dir child: "+dirChild)
            if dir == "root" and dir not in all_directories: #for the first dir only
                all_directories.append(dir)
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
    #print(all_directories)
    #print(dir_value_pairs)
    calculate_file_size(all_directories, dir_value_pairs)
    #print(all_directories)
    #print(dir_value_pairs)

def calculate_file_size(directory_list, dir_value_pairs):
            
    #remove all root entries
    dir_value_pairs = {key:val for key, val in dir_value_pairs.items() if val != "root"}

    dir_totals = {}
    total = 0
    iterator = 0
    step = 1
    window = directory_list[iterator]
    for file_size in dir_value_pairs:
        directory = dir_value_pairs[file_size]
        print("Key: "+file_size+" ----- Value: "+directory)
        #print("iterating on: "+directory_list[iterator])
        #print(iterator)
        #print(len(directory_list))
        if directory == "root" or directory == "ls": #skip root entries for now
            continue

        window = directory_list[step]
        if directory == window:
            total += int(file_size)
            print("Looking at directory: " +directory)
            print("Current total is: " + str(total))
            dir_totals[directory] = total
            if iterator != len(dir_value_pairs)-1:
                peekOne = next( v for i, v in enumerate(dir_value_pairs.items()) if i == iterator+1)
                #peekTwo = next( v for i, v in enumerate(dir_value_pairs.items()) if i == iterator+2)
                #print(peek[0])
                #print(peek[1])
                if window != peekOne[1]:
                    #iterator +=1
                    print("---- NEXT DIRECTORY ----")
                    step += 1
                    total = 0 
                iterator += 1

    print(dir_totals)
            
solution_part_1()

""" print(f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=10)/10}s'
    )
print(f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=10)/10}s'
    ) """