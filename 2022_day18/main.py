# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from operator import itemgetter

def countNotOccupied(point,space):
    NbrNotOcc = 6
    for dir in [-1,1]:
        for coord in ['x','y','z']:
            if coord == 'x':
                yi = zi = 0
                xi = dir
            if coord == 'y':
                xi = zi = 0
                yi = dir
            if coord == 'z':
                xi = yi = 0
                zi = dir
            if space[point[0]+xi][point[1]+yi][point[2]+zi] == 1:
                NbrNotOcc -= 1

    return NbrNotOcc

##copied code since recursion does not work! use
def countflood(points, Space):
    max_x = max(points, key=itemgetter(0))[0] + 2
    min_x = min(points, key=itemgetter(0))[0] - 1
    max_y = max(points, key=itemgetter(1))[1] + 2
    min_y = min(points, key=itemgetter(1))[1] - 1
    max_z = max(points, key=itemgetter(2))[2] + 2
    min_z = min(points, key=itemgetter(2))[2] - 1
    water = [(min_x, min_y, min_z)]  # just as we'd start a recursive flood fill
    water_sides = 0
    visited = []  # dfs cache

    # do an iterative flood fill - python max recusion
    while water:
        x, y, z = water.pop()
        if (x, y, z) not in visited:
            visited.append((x, y, z))

            # stole this efficient loop of flood points from u/alykzandr
            for nx, ny, nz in [(x + 1, y, z), (x - 1, y, z),
                               (x, y + 1, z), (x, y - 1, z),
                               (x, y, z + 1), (x, y, z - 1)]:
                if (min_x <= nx <= max_x and
                        min_y <= ny <= max_y and
                        min_z <= nz <= max_z):
                    if [nx, ny, nz] in points:
                        water_sides += 1 #reached the point/cube
                    else:
                        water.append((nx, ny, nz)) #add some water since it is not the cube
    return water_sides

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Rows = open("../../../Advent/2022_day18.txt",'r').read().strip().split("\n")
    space = []
    j = 0
    spaceSize = 23

    space = [[[0]*spaceSize for i in range(spaceSize)] for j in range(spaceSize)]

    Points = []

    for r in Rows:
        point = list(map(int,r.split(",")))
        Points.append(point)
        space[point[0]][point[1]][point[2]] = 1

    print(sum([countNotOccupied(Point,space) for Point in Points]))
    #print(space)
    #sys.setrecursionlimit(2461)
    #new_recursion_limit = sys.getrecursionlimit()

    #flood(space, 0, 0, 0) #does not work with python

    print(countflood(Points,space))
    #print(sum([countflood(Point, space) for Point in Points]))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
