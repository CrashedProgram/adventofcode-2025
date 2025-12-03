def solve_dial_puzzle(filename):
    with open(filename, 'r') as f:
        rotations = [line.strip() for line in f if line.strip()]
    
    position = 50
    zero_count = 0
    
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        
        if direction == 'L':
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100
        
        if position == 0:
            zero_count += 1
    
    return zero_count

if __name__ == "__main__":
    password = solve_dial_puzzle('input.txt')
    print(f"The password is: {password}")
