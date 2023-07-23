with open(r'./d5_input.txt', 'r') as f:
    lines = f.read().splitlines()

def flanked(string: str, debug=False) -> bool:

    for i, c in enumerate(string[:-2]):
        if c == string[i+2]:
            return True
    return False

    
def has_duplicate_pair(string: str, debug=False) -> bool:
    # For every pair of two characters in the string,
    # see if that same pair is in the substring before
    # the pair or the substring after the pair. If so,
    # it is a non-overlapping duplicate.
    
    for i in range(len(string[:-1])):
        cloned_string_left = string[:i]
        cloned_string_right = string[i+2:]
        pair = string[i: i+2]
        if pair in cloned_string_left or pair in cloned_string_right:
            return True
    return False
    
def check_string(string: str, debug=False) -> bool:

    is_flanked = flanked(string, debug=debug)
    pair = has_duplicate_pair(string, debug=debug)
    
    if is_flanked and pair:
        return True
    else:
        return False

nice_strings = 0
for line in lines:
    if flanked(line) and has_duplicate_pair(line):
        nice_strings += 1
        
print(f"There are {nice_strings} nice strings.")

