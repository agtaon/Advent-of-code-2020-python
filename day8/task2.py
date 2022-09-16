"""
This code changes the first jmp/npos instruction it encounters and 
then repeats the previous code. If it encounters a 'used' index it restarts but 
changes the second jmp/nop this time. Even if npos is +0 since that 
instruction will be replaced by 'used' hindering an infinite loop.
"""

import os

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    instructions = f.readlines()
    for i in range (len(instructions)):
        current_index = 0
        current_value = 0
        iterator = 0
        instruction = 0
        status = 0

        instructions_copy = instructions.copy()
        if 'jmp' in instructions_copy[i]:
            status = 1
            instructions_copy[i] = instructions_copy[i].replace('jmp', 'nop')
        
        elif 'nop' in instructions_copy[i] and status == 0:
            instructions_copy[i] = instructions_copy[i].replace('nop', 'jmp')
        else:
            continue
        
        while instructions_copy[current_index] != 'used':
            iterator += 1
            if iterator > 10000:
                print('loop reached limit')
                break
            instruction = instructions_copy[current_index].rstrip()
            instructions_copy[current_index] = 'used'
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
            if instructions_copy[-1] == 'used':
                print('current_value: ', current_value)
                break

        
