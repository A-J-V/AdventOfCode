with open(r'./d1_input.txt', 'r') as f:
    input = f.read()

floor = 0
pos = 1
for i, token in enumerate(input):
    if token == '(':
        floor += 1
    elif token == ')':
        floor -= 1

    if floor == -1:
        break

    pos += 1

print(f"Mr. Claus first entered the basement at position {pos}.")
