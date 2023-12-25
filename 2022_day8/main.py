# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
import sys


def map_forest(x, y, forest, visibility_map, scenic_score):
    if visibility_map[y][x]:
        return scenic_score #for edges visibility is 0
    dx = -1 if x <= len(forest[y]) // 2 else 1 #if x is in the left part of the middle then -1 otherwise 1
    dy = -1 if y <= len(forest) // 2 else 1
    horizontal = len(forest[y]) >= len(forest)
    score = 0
    print(dx)
    print(dy)
    for direction in range(4):
        cx = x + dx * (horizontal)
        cy = y + dy * (not horizontal)
        visible = True
        count = 0
        while cx >= 0 and cx < len(forest[y]) and cy >= 0 and cy < len(forest):
            count += 1
            if forest[cy][cx] >= forest[y][x]:
                visible = False
                break
            cx += dx * (horizontal)
            cy += dy * (not horizontal)
        score = count if score == 0 else score * count #first check score is 0 and count is added, for next directions multiply with previous
        if visible:
            visibility_map[y][x] = True
        horizontal = not horizontal
        if direction == 1:
            dx = dx * -1
            dy = dy * -1
    return scenic_score if scenic_score[2] >= score else (x, y, score)


if __name__ == '__main__':
    with open("../../../Advent/2022_day8.txt.txt", 'rt') as f:
        forest = [line.strip() for line in f.readlines()]

    visibility_map = [[True] * len(forest[0])] #create matrix [[]] of trues of length len(forest[0])=99 for first line

    for y in range(1, len(forest)-1):
        visibility_map.append(
            [True] + ([False] * (len(forest[y]) - 2)) + [True]) #True for first and last row rest false
    visibility_map.append([True] * len(forest[-1])) #-1 is last element, last column all are visible

    scenic_score = (0, 0, 0)
    for y in range(1, len(forest)-1):
        row = forest[y]
        for x in range(1, len(row)-1):
            scenic_score = map_forest(
                x, y, forest, visibility_map, scenic_score)
    print(sum([v for t in visibility_map for v in t]))
    print(scenic_score)