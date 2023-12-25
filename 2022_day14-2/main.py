# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#borrowed solution (unknown source!)
def place_rocks(data):
    rocks = set()
    for line in data.split("\n"):
        points = [tuple(map(int, p.split(","))) for p in line.split(" -> ")]
        for i in range(len(points)-1):
            p1, p2 = points[i], points[i+1]
            xr = range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1)
            yr = range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1)
            rocks.update({(x, y) for x in xr for y in yr})
    return rocks

data = open("../../../Advent/2022_day14.txt.txt").read().strip()
rocks = place_rocks(data)
print(len(rocks))
max_y = max((y for _, y in rocks))
x, y = (500, 0)
ct = p1 = p2 = 0
while True:
    if (x, y) in rocks:  # restart sand at origin
        (x, y) = (500, 0)
    if y > max_y and p1 == 0:  # abyss part 1
        p1 = ct
    if (x, y + 1) not in rocks and y < max_y + 1:  # drop down?
        y += 1
    elif (x - 1, y + 1) not in rocks and y < max_y + 1:  # drop left-down?
        x -= 1
        y += 1
    elif (x + 1, y + 1) not in rocks and y < max_y + 1:  # drop right-down?
        x += 1
        y += 1
    else:  # hit somoething
        ct += 1
        rocks.add((x, y))
    if (x, y) == (500, 0):  # filled
        p2 = ct
        break
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
