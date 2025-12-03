def max_joltage(bank):
    max_val = 0
    n = len(bank)
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            val = int(bank[i] + bank[j])
            max_val = max(max_val, val)
    
    return max_val


def solve(input_text):
    total = 0
    
    for line in input_text.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        joltage = max_joltage(line)
        total += joltage
    
    return total


with open('input3.txt', 'r') as f:
    input_text = f.read()

result = solve(input_text)
print(f"Total output joltage: {result}")
