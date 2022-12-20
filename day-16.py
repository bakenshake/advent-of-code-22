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

    total_pressure = 0
    open_valves = []
    minutes = 1
    start = tunnels[0][0]
    curr_pos = start
    prev_valve_loc = start
    while minutes <= 30:
        #move to the next valve
        print("----- "+str(minutes)+" ------")
        prev_valve_loc = curr_pos #to make sure we don't visit the same one we were JUST at
        curr_pos = determine_movement(valve_and_flow, tunnels, curr_pos, prev_valve_loc)
        print("Moving to valve: "+curr_pos)
        minutes += 1 #one minute to move to a valve
        print("----- "+str(minutes)+" ------")
        #calculate pressure based on currently opened valves
        total_pressure += calculate_pressure(valve_and_flow, open_valves)
        #check if we open the valve we're visiting
        valve_to_open = to_open_or_not()
        #if we do open the valve, add to open_valves
        if valve_to_open:
            open_valves.append(curr_pos)
        minutes += 1 #one minute to open a valve
        #calculate pressure
        total_pressure += calculate_pressure(valve_and_flow, open_valves)

def calculate_pressure(valve_and_flow, open_valves):

    pressure = 0
    for i in open_valves:
        flow_rate = valve_and_flow.get(i)
        pressure += flow_rate

    return pressure

def to_open_or_not():
    print("ayo")

def determine_movement(valve_flow_pairs, valve_tunnels, curr_pos, prev_valve_loc):

    #find the tunnels connected to the valve we're currently at
    for i in range(0, len(valve_tunnels)):
        if curr_pos == valve_tunnels[i][0]:
            rates_to_check = valve_tunnels[i]
            break

    #print(rates_to_check)

    valve_to_move = find_highest_rate(valve_flow_pairs, rates_to_check, prev_valve_loc)

    return valve_to_move

def find_highest_rate(valve_flow_pairs, rates_to_check, prev_valve_loc):

    rates = []
    for i in range(0, len(rates_to_check)):
        if i == 0: 
            continue
        elif i > 0 and rates_to_check[i] != prev_valve_loc:
            curr_rate = valve_flow_pairs.get(rates_to_check[i])
            rates.append(curr_rate)
    
    #print(max(rates))

    valve_to_move = [i for i in valve_flow_pairs if valve_flow_pairs[i]==max(rates)]
    #print(valve_to_move)
    
    return valve_to_move[0]

solution_part_1()