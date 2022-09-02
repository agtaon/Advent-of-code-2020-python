"""
This code changes the first jmp/npos instruction it encounters and 
then repeats the previous code. If it encounters a 'used' index it restarts but 
changes the second jmp/nop this time. Even if npos is +0 since that 
instruction will be replaced by 'used' hindering an infinite loop.
"""

import os

def instruction_reader_and_changer():
    current_index = 0
    current_value = 0
    iterator = 0
    instruction = 0
    while instructions[current_index] != 'used':
        iterator += 1
        if iterator > 10000:
            print('loop reached limit')
            break
        instruction = instructions[current_index].rstrip()
        instructions[current_index] = 'used'
        if instruction[0:3] == 'jmp':
            if instruction[4] == '+':
                current_index += int(instruction[5:])
            else:
                current_index -= int(instruction[5:])

        elif instruction[0:3] == 'acc':
            current_index += 1
            if instruction[4] == '+':
                current_value += int(instruction[5:])
            else:
                current_value -= int(instruction[5:])

        else:
            current_index += 1
        if current_index > len(instructions)-1:
            break
    return instruction, current_index, current_value


with open(os.path.join(os.getcwd(), "input.txt")) as f:
    instructions = f.readlines()
    current_index = 0
    current_value = 0
    iterator = 0
    instruction = 0
    while current_index != len(instructions)-1:
        instruction, current_index, current_value = instruction_reader_and_changer()
        if instructions[current_index][0:3] == "jmp":
            instructions[current_index].replace("jmp", "nop")
        else:
            instructions[current_index].replace("nop", "jmp")
    
    print('current_value: ', current_value)