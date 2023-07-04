
with open("./d3_input.txt", "r") as f:
    inp = f.read()

# Use a set and add visited houses. We don't care how many times they're visited.
# Set will ensure we only add unique houses.   
visited = set()

# Initiate starting location and add it to the visited list.
x, y = 0, 0
visited.add((0, 0))

# For every token in the puzzle input, move x, y coords and add location to set
for token in list(inp):
    match token:
        case "^":
            y -= 1
        case "v":
            y += 1
        case "<":
            x -= 1
        case ">":
            x += 1
    
    visited.add((x, y))
    
print(f"Santa has visited {len(visited)} houses.")
