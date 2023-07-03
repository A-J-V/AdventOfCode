with open(r'./d1_input.txt', 'r') as f:
    input = f.read()

floor = 0

for token in input:
    if token == '(':
        floor += 1
    elif token == ')':
        floor -= 1

print(f"Mr. Claus must go to floor {floor}.")
