# solution only works for the first part
# need to apply compression to get full marks
# otherwise compute limit exceeded

# remove type hints for submission
# these type hints not supported on python 3.8
# but local env complains if i remove them
from typing import List

h, w, n = map(int, input().split())
canvas: List[List[None | str]] = [[None for _ in range(w)] for _ in range(h)]

for _ in range(n):
    line = input().split()
    x, y, spread = map(int, line[:3])
    color = line[3]

    x1 = max(0, x - spread)
    y1 = max(0, y - spread)
    x2 = min(w - 1, x + spread)
    y2 = min(h - 1, y + spread)

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            canvas[j][i] = color

color = input()

total = 0
for row in canvas:
    total += row.count(color)

print(total)
