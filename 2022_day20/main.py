# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def CalcMoveToIndex(steps, index, listlength):
    if steps == 0:
        return index
    else:
        direction = int(steps/abs(steps))
        if direction > 0:
            finalindex = (steps+index) % (listlength-1)
        else:
            finalindex = (steps+index) % (listlength - 1)
    return finalindex

def NextIndex(steps, index, listlength):
    if steps == 0:
        return index
    else:
        direction = int(steps/abs(steps))

        wrapping = ((index+steps) < 0) or ((index+steps) >= listlength)
        if not wrapping:
            finalindex = index + steps
        else:
            #wrapping
            finalindex = index+steps
            while wrapping:
                finalindex -= int(direction * (listlength))
                wrapping = (finalindex < 0) or (finalindex >= listlength)
    return finalindex

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Rows = open("../../../Advent/2022_day20.txt", 'r').read().strip().split("\n")
    Numbers = []
    Numbers= list(map(int, Rows))
    OriginalNumbers = list(map(int, Rows)) #assignment OriginalNumbers = Numbers, will reference to same list which i move
    LengthList = len(Numbers)
    sum = 0
    for j in range(LengthList):
        #print("i",i)
        NumberToMove = OriginalNumbers[j]
        #print("numbermove",NumberToMove)
        IndexOfNumberToMove = Numbers.index(NumberToMove)

        moveto = CalcMoveToIndex(NumberToMove, IndexOfNumberToMove, LengthList)
        IndexOfNumberToMove = Numbers.index(NumberToMove)

        i = Numbers.index(NumberToMove)
        new_i = (i + NumberToMove) % (len(Numbers) - 1)

        Numbers.insert(new_i, Numbers.pop(i))
    ##not working since it has duplicate numbers!
    zero_index = Numbers.index(0)
    for i in [1000, 2000, 3000]:
        index = zero_index + i % (len(Numbers))
        index = index % (len(Numbers))
        sum += Numbers[index]
        print("SUM", Numbers[index])


    print(Numbers)
    print(Numbers[NextIndex(1, Numbers.index(0),LengthList)])
    print(sum)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
