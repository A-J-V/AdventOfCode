import hashlib

def decrypt(key):
    """Given an input, use brute force to find the solution."""
    for i in range(1, 10000000):
        result = hashlib.md5((key + str(i)).encode()).hexdigest()
        if result[:5] == "00000":
            print(f"The solution is {i}")
            return i

with open(r'./d4_input.txt', 'r') as f:            
    key = f.read().strip()
print(key)
decrypt(key)
