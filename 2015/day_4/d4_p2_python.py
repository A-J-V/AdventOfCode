import hashlib

def decrypt(key):
    """Given an input, use brute force to find the solution."""
    for i in range(1, 1000000000):
        result = hashlib.md5((key + str(i)).encode()).hexdigest()
        if result[:6] == "000000":
            print(f"The solution is {i}")
            return i

with open(r'./d4_input.txt', 'r') as f:            
    key = f.read().strip()
decrypt(key)
