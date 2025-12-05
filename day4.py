with open("input4.txt") as f:
    grid = [line.strip() for line in f.readlines()]

rows = len(grid)
cols = len(grid[0])

directions = [(delta_row, delta_column) for delta_row in [-1, 0, 1] for delta_column in [-1, 0, 1] if not (delta_row == 0 and delta_column == 0)]

accessible_count = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '@':
            adjacent_rolls = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                    adjacent_rolls += 1
            
            if adjacent_rolls < 4:
                accessible_count += 1

print(accessible_count)
