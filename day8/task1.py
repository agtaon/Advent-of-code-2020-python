import os

    

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    instructions = f.readlines()
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
        
    
    print('current_value: ', current_value)