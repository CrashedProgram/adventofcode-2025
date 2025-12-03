def is_invalid_id(n):
    s = str(n)
    length = len(s)
    
    for base_len in range(1, length // 2 + 1):
        if length % base_len == 0:
            repetitions = length // base_len
            if repetitions >= 2:
                base = s[:base_len]
                if base * repetitions == s:
                    return True
    return False


def find_invalid_ids_in_range(start, end):
    invalid_ids = set()
    
    min_digits = len(str(start))
    max_digits = len(str(end))
    
    for num_digits in range(min_digits, max_digits + 1):
        for base_len in range(1, num_digits // 2 + 1):
            if num_digits % base_len != 0:
                continue
            
            repetitions = num_digits // base_len
            if repetitions < 2:
                continue
            
            min_base = 10 ** (base_len - 1) if base_len > 1 else 1
            max_base = 10 ** base_len - 1
            
            for base in range(min_base, max_base + 1):
                repeated = int(str(base) * repetitions)
                if start <= repeated <= end:
                    invalid_ids.add(repeated)
                elif repeated > end and base_len > 1:
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
