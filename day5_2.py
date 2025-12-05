with open("input5.txt") as f:
    content = f.read().strip()

parts = content.split("\n\n")
ranges_section = parts[0]

fresh_ranges = []
for line in ranges_section.strip().split("\n"):
    start, end = map(int, line.split("-"))
    fresh_ranges.append((start, end))

fresh_ranges.sort()

merged = []
for start, end in fresh_ranges:
    if merged and start <= merged[-1][1] + 1:
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        merged.append((start, end))

total_fresh = sum(end - start + 1 for start, end in merged)

print(total_fresh)
