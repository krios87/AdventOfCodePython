# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def calcStonesCoord(x1, y1, x2, y2):
    returncoord = []
    if x1 == x2:
        for y in range(min(y1,y2),max(y1,y2)+1):
            returncoord.append([x1, y])
    elif y1 == y2:
        for x in range(min(x1,x2),max(x1,x2)+1):
            returncoord.append([x, y1])

    return returncoord


def checkStoneOrSand(x,y,xMin,xMax,yMax,Map):
    retval = 0
    if (x < xMin) | (x > xMax) | (y> yMax):
        retval = 2  #full!!
    elif (Map[y][x]=="#") | (Map[y][x]=="O"):
        #check left down
        if (Map[y][x-1]=="#") | (Map[y][x-1]=="O"):
            #check right down
            if (Map[y][x + 1] == "#") | (Map[y][x + 1] == "O"):
                Map[y-1][x] = "O"
                retval = 1 #place sand
            else:
                retval = checkStoneOrSand(x+1, y + 1, xMin, xMax,yMax, Map)
                ##move down right
        else:
            retval = checkStoneOrSand(x-1, y +1, xMin, xMax,yMax, Map)
            #move down left
    else:
         retval = checkStoneOrSand(x, y+1, xMin, xMax,yMax, Map)
            #move down

    return retval

def checkStoneOrSand2(x,y,xMin,xMax,yMax,Stones,floorY):
    retval = 0
    part1 = 1
    print(x,y,xMin,xMax,yMax)
    if [x, y + 1] not in Stones and (y < (yMax + 3)): #down?
        retval = checkStoneOrSand2(x, y + 1, xMin, xMax, yMax, Stones,floorY)
    elif [x - 1, y + 1] not in Stones and y < (yMax + 3):  # left-down?
        retval = checkStoneOrSand2(x - 1, y + 1, xMin, xMax, yMax, Stones,floorY)
    elif [x + 1, y + 1] not in Stones and y < (yMax + 3):  # right-down?
        retval = checkStoneOrSand2(x + 1, y + 1, xMin, xMax, yMax, Stones,floorY)
    else:  # create new sand
        Stones.append([x, y])
        retval = 1
        if (x ==500) and (y== 0):
            retval = 2  #full!!
    return retval

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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Rows = open("../../../Advent/2022_day14.txt", 'r').read().strip().split("\n")
    data = open("../../../Advent/2022_day14.txt.txt").read().strip()

    line = []
    for Row in Rows:
        line.append(Row.split("->"))

    coord = []
    drawCoord = []
    xMin = xMax = 500
    yMin = 0
    yMax = 0
    for oneLine in line:
        coordIndex = 0
        intCoord2 = []
        for oneCoord in oneLine:
            intCoord2.append(list(map(int, oneCoord.split(",")))) #int is a list of int list ([X][Y])
            if intCoord2[coordIndex][0] < xMin:
                xMin = intCoord2[coordIndex][0]
            elif intCoord2[coordIndex][0] > xMax:
                xMax = intCoord2[coordIndex][0]
            elif intCoord2[coordIndex][1] < yMin:
                yMin = intCoord2[coordIndex][1]
            elif intCoord2[coordIndex][1] > yMax:
                yMax = intCoord2[coordIndex][1]

            if coordIndex > 0:

                stonesRow =calcStonesCoord(intCoord2[coordIndex-1][0], intCoord2[coordIndex-1][1], intCoord2[coordIndex][0], intCoord2[coordIndex][1])
                for stone in stonesRow:
                    if stone not in drawCoord: #better to use set to have unique items instead of drawing a map as below
                        drawCoord.append(stone)
            coordIndex += 1

    #part2 add floor:
    for x in range(-100000,100000):
        drawCoord.append([x,yMax+2])


    nbrOfLoops = 30000
    iterationLoop = nbrOfLoops
    while iterationLoop > 0:
        retVal= checkStoneOrSand2(500,0, xMin, xMax, yMax, drawCoord,yMax+1)
        if (retVal == 2):
            break
        iterationLoop -= 1

    #print(nbrOfLoops-iterationLoop+1)#+1 for second part

    Map = []
    for y in range(yMin, yMax + 3):
        Xcoord = []
        for x in range(-400 + xMin, xMax + 1 + 400):
            drawStone = 0

            for coord in drawCoord:
                if (x == coord[0]) & (y == coord[1]):
                    drawStone = 1
                elif (x == 500) & (y == 0):  # start
                    drawStone = 2
            if drawStone == 1:
                Xcoord.append("#")
            elif drawStone == 2:
                Xcoord.append("O")
            else:
                Xcoord.append(".")
        Map.append(Xcoord)

    for Xcoord in Map:
        print(Xcoord)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
