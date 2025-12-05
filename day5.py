with open("input5.txt") as f:
    content = f.read().strip()

parts = content.split("\n\n")
ranges_section = parts[0]
ingredients_section = parts[1]

fresh_ranges = []
for line in ranges_section.strip().split("\n"):
    start, end = map(int, line.split("-"))
    fresh_ranges.append((start, end))

available_ids = [int(line) for line in ingredients_section.strip().split("\n")]

fresh_count = 0
for ingredient_id in available_ids:
    for start, end in fresh_ranges:
        if start <= ingredient_id <= end:
            fresh_count += 1
            break

print(fresh_count)
