import numpy as np

with open(r'./d6_input.txt', 'r') as f:
    lines = f.read().strip().splitlines()
   
lights = np.zeros((1000, 1000))
lights[:, :] = -1

def toggle(start, stop):
    lights[int(start[0]): int(stop[0]) + 1, int(start[1]): int(stop[1]) + 1] *= -1
    
    
def on(start, stop):
    lights[int(start[0]): int(stop[0]) + 1, int(start[1]): int(stop[1]) + 1] = 1
    
    
def off(start, stop):
    lights[int(start[0]): int(stop[0]) + 1, int(start[1]): int(stop[1]) + 1] = -1
   

def parse_command(cmd):
    if "turn off" in cmd:
        instruction = off
    elif "turn on" in cmd:
        instruction = on
    else:
        instruction = toggle
    first_digit = lambda i, x: i if x[i].isdigit() else first_digit(i+1, x)
    first = first_digit(0, cmd)
    cmd = cmd[first:].split('through')
    return (instruction,
            tuple(cmd[0].strip().split(',')),
            tuple(cmd[1].strip().split(','))
            )
    
for line in lines:
    function, start, stop = parse_command(line)
    function(start, stop)
    
print(f"There are {lights[lights == 1].sum()} lights on.")
    
