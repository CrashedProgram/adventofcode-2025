def solve_dial_puzzle_part2(filename):
    with open(filename, 'r') as f:
        rotations = [line.strip() for line in f if line.strip()]
    
    position = 50
    zero_count = 0
    
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        
        if direction == 'L':    
            if position == 0:
                crossings = distance // 100
            else:
                if distance >= position:
                    crossings = 1 + (distance - position) // 100
                else:
                    crossings = 0
            
            zero_count += crossings
            position = (position - distance) % 100
            
        else:            
            if position == 0:
                crossings = distance // 100
            else:
                first_cross = 100 - position
                if distance >= first_cross:
                    crossings = 1 + (distance - first_cross) // 100
                else:
                    crossings = 0
            
            zero_count += crossings
            position = (position + distance) % 100
    
    return zero_count


if __name__ == "__main__":
    password = solve_dial_puzzle_part2('input1.txt')
    print(f"The password is: {password}")
