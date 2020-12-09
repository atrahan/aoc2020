# Task 8: Game Code

from utilities import read_input
from typing import List

def process_command(command:str):
    action, val = [s.strip() for s in command.split()]
    val = int(val)
    if action == "nop":
        pos_increment = 1
        acc_increment = 0
    elif action == "acc":
        pos_increment = 1
        acc_increment = val
    elif action == "jmp":
        pos_increment = val
        acc_increment = 0
    else:
        raise ValueError(f"Command action '{action}' in command '{command}' not recognized.")
    return pos_increment, acc_increment

def run_command_list(commands:List[str]):
    # Initialize
    pos_list = [0]
    accumulator = 0
    exit_code = 0
    
    # Run commands
    while True:
        cur_pos = pos_list[-1]
        if cur_pos in pos_list[:-1]:
            exit_code = 1
            break
        elif cur_pos == len(commands):
            exit_code = 0
            break
        elif (cur_pos > len(commands)) or (cur_pos < 0):
            print(f"executing {cur_pos}, out of {len(commands)}")
            raise IndexError()
        else:
            pos_increment, acc_increment = process_command(command=commands[pos_list[-1]])
            pos_list.append(pos_list[-1]+pos_increment)
            accumulator += acc_increment
    
    return pos_list, accumulator, exit_code

if __name__=="__main__":
    
    # commands = read_input("08_test_input.txt")
    commands = read_input("08_input.txt")
    
    # Accumulator on exit, no modifications
    pos_list, accumulator, exit_code = run_command_list(commands)
    print(f"Accumulator before loop: {accumulator}")
    
    # Test jmp/nop conversion
    for ix in range(len(commands)):
        action = commands[ix].split()[0].strip()
        if action == "acc":
            continue
        elif action == "jmp":
            modified_commands = commands.copy()
            modified_commands[ix] = modified_commands[ix].replace("jmp", "nop")
            pos_list, accumulator, exit_code = run_command_list(modified_commands)
        elif action == "nop":
            modified_commands = commands.copy()
            modified_commands[ix] = modified_commands[ix].replace("nop", "jmp")
            pos_list, accumulator, exit_code = run_command_list(modified_commands)
        else:
            raise ValueError(f"Command action '{action}' in command '{commands[ix]}' not recognized.")
        
        if exit_code == 0:
            print(f"Successful execution on changing line {ix}.")
            print(f"Accumulator at completion: {accumulator}")
            break
        
    
    
    # # Testing
    # print("-"*10)
    # for p in pos_list:
    #     print(f"{p}: {commands[p]}")
    
    