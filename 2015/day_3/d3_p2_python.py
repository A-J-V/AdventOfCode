
with open("./d3_input.txt", "r") as f:
    inp = f.read()

# Use a set and add visited houses. We don't care how many times they're visited.
# Set will ensure we only add unique houses.   
visited = set()

# Initiate starting location and add it to the visited list.
# This time there are two coordinates, santa and robo-santa.
# Use lists to exploit Python's pass-by-reference.
s = [0, 0]
r = [0, 0]
visited.add((0, 0))

def update_x(coord, change):
    coord[0] += change

def update_y(coord, change):
    coord[1] += change

# Define a variable that will be used to switch back and forth between santas
i = 0

# For every token in the puzzle input, move a coordinate and add location to set
for token in list(inp):
    if i % 2 == 0:
        coord = s
    else:
        coord = r
        
    match token:
        case "^":
            update_y(coord, -1)
        case "v":
            update_y(coord, 1)
        case "<":
            update_x(coord, -1)
        case ">":
            update_x(coord, 1)
    
    visited.add((coord[0], coord[1]))
    i += 1
    
print(f"Santa has visited {len(visited)} houses.")
