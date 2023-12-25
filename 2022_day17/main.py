# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
import copy
#from tqdm import tqdm
class Rock:
    rocks = []

    def __init__(self, rocks):
        self.rocks = rocks

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    direction = open("../../../Advent/2022_day17.txt",'r').read()
    print(direction)
    lengthDirections = len(direction)
    Rocklist = []

    #lower left corner is 0,0 of rocks
    MinRock = [[0,0],[1,0],[2,0],[3,0]]
    PlusRock =[[1,0],[0,1],[1,1],[2,1],[1,2]]
    RightRock =[[0,0],[1,0],[2,0],[2,1],[2,2]]
    VertRock = [[0,0],[0,1],[0,2],[0,3]]
    SquareRock = [[0,0],[1,0],[0,1],[1,1]]
    Rocklist.append(MinRock)
    Rocklist.append(PlusRock)
    Rocklist.append(RightRock)
    Rocklist.append(VertRock)
    Rocklist.append(SquareRock)

    Cave = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0]]

    Yoffset = 3
    Xoffset = 2
    i = 0
    maxrocks = 1

    #bar = tqdm(range(2022))
    for j in range(2022):
        #bar.update(1)
        tmplist = copy.deepcopy(Rocklist[j%5])
        breakcond = 0
        for el in tmplist:
            el[0] += Xoffset
            el[1] += Yoffset+maxrocks

        while 1:
            moveright = 1
            moveleft = 1
            for el in tmplist:
                if el[0] == 6 or [el[0]+1,el[1]] in Cave:
                    moveright = 0
                if el[0] == 0 or [el[0]-1,el[1]] in Cave:
                    moveleft = 0

            movevalue = 1 if direction[i%lengthDirections] == ">" and moveright else 0
            movevalue = -1 if direction[i%lengthDirections] == "<" and moveleft else movevalue

            for el in tmplist:
                el[0] += movevalue
                if ([el[0],el[1]-1] in Cave):
                    breakcond = 1

            for el in tmplist:
                if not breakcond: #only move with wind at lowest point
                    el[1] -= 1

            i += 1
            if breakcond:
                break;

        for el in tmplist:
            Cave.append(el)

        for el in tmplist:
            maxrocks = max(maxrocks,el[1]+1)


    print("max",maxrocks-1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
