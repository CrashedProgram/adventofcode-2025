with open("input4.txt") as f:
    grid = [list(line.strip()) for line in f.readlines()]

rows = len(grid)
cols = len(grid[0])

directions = [(delta_row, delta_column) for delta_row in [-1, 0, 1] for delta_column in [-1, 0, 1] if not (delta_row == 0 and delta_column == 0)]

def count_adjacent_rolls(grid, r, c):
    count = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
            count += 1
    return count

def find_accessible_rolls(grid):
    accessible = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                if count_adjacent_rolls(grid, r, c) < 4:
                    accessible.append((r, c))
    return accessible

total_removed = 0

while True:
    accessible = find_accessible_rolls(grid)
    if not accessible:
        break
    
    for r, c in accessible:
        grid[r][c] = '.'
    
    total_removed += len(accessible)

print(total_removed)
