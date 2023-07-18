with open(r'./d5_input.txt', 'r') as f:
    inpt = f.read()
    
lines = inpt.splitlines()

def is_vowel(c) -> bool:
    return c.lower() in 'aeiou'
    
def three_vowels(string: str) -> bool:
    vowels = 0
    for c in string:
        if is_vowel(c):
            vowels += 1
            
    if vowels >= 3:
        return True
    else:
        return False
    
def has_double(string: str) -> bool:
    for i, c in enumerate(string[:-1]):
        if c == string[i+1]:
            return True
    return False
    
def no_nasties(string: str) -> bool:
    for i, c in enumerate(string[:-1]):
        if (c + string[i+1]).lower() in ['ab', 'cd', 'pq', 'xy']:
            return False
    return True
    
def check_string(string: str) -> bool:

    has_three = three_vowels(string)
    has_doub = has_double(string)
    no_foul = no_nasties(string)
    
    if has_three and has_doub and no_foul:
        return True
    else:
        return False

nice_strings = 0
for line in lines:
    if check_string(line):
        nice_strings += 1
        
print(f"There are {nice_strings} nice strings.")
    

