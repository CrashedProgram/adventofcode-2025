def is_invalid_id(n):
    s = str(n)
    length = len(s)
    
    if length % 2 != 0:
        return False
    
    half = length // 2
    return s[:half] == s[half:]


def find_invalid_ids_in_range(start, end):
    invalid_ids = []
    
    for num_digits in range(2, 20, 2):
        half_digits = num_digits // 2
        
        min_half = 10 ** (half_digits - 1) if half_digits > 1 else 1
        max_half = 10 ** half_digits - 1
        
        for half in range(min_half, max_half + 1):
            repeated = int(str(half) * 2)
            
            if start <= repeated <= end:
                invalid_ids.append(repeated)
            elif repeated > end:
                break
    
    return invalid_ids


def solve(input_text):
    ranges = []
    parts = input_text.strip().split(',')
    
    for part in parts:
        part = part.strip()
        if not part:
            continue
        start, end = map(int, part.split('-'))
        ranges.append((start, end))
    
    total = 0
    for start, end in ranges:
        invalid_ids = find_invalid_ids_in_range(start, end)
        total += sum(invalid_ids)
    
    return total


with open('input2.txt', 'r') as f:
    input_text = f.read()

result = solve(input_text)
print(f"Sum of all invalid IDs: {result}")
