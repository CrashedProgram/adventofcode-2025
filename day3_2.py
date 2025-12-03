def max_joltage_12(bank):
    n = len(bank)
    k = 12
    
    
    result = []
    start = 0
    
    for i in range(k):
        remaining_to_pick = k - i
        end = n - remaining_to_pick
        
        best_pos = start
        best_digit = bank[start]
        
        for j in range(start, end + 1):
            if bank[j] > best_digit:
                best_digit = bank[j]
                best_pos = j
        
        result.append(best_digit)
        start = best_pos + 1
    
    return int(''.join(result))


def solve(input_text):
    total = 0
    
    for line in input_text.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        joltage = max_joltage_12(line)
        total += joltage
    
    return total


with open('input3.txt', 'r') as f:
    input_text = f.read()

result = solve(input_text)
print(f"Total output joltage: {result}")
