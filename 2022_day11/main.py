import sys


class StupidMonkey:

    items = []
    divider = 1
    NextMonkeyDivTrue = 0
    NextMonkeyDivFalse = 0
    MonkeyOperand = ""
    OperandValue = 0
    inspectingItems = 0

    def __init__(self, items, divider, NextMonkeyDivTrue, NextMonkeyDivFalse, MonkeyOperand, OperandValue):
        self.items = items
        self.divider = divider
        self.NextMonkeyDivTrue = NextMonkeyDivTrue
        self.NextMonkeyDivFalse = NextMonkeyDivFalse
        self.MonkeyOperand = MonkeyOperand
        self.OperandValue = OperandValue


def CalcOperation(operator, oldVal, val):
    if operator == "power":
        return oldVal*oldVal
    elif operator == "mult":
        return oldVal*val
    elif operator == "add":
        return oldVal+val


if __name__ == '__main__':
    Lines = open(sys.argv[1], 'r').read().strip().split("\n")
    monkeyList = []
    for line in Lines:

        FindItems = line.split("items:")

        if len(FindItems) > 1:
            Items = list(map(int, FindItems[1].split(",")))  #get second part after "items:" split with ",", convert to int at once with map
        elif line.find("* old") != -1:
            monkeyOperand = "power"
            operandValue = 0
        elif line.find("old * ") != -1:
            monkeyOperand = "mult"
            operandValue = int(line.split("old * ")[1])
        elif line.find("old + ") != -1:
            monkeyOperand = "add"
            operandValue = int(line.split("old + ")[1])
        elif line.find("divisible") != -1:
            divider = int(line.split("Test: divisible by ")[1])
        elif line.find("If true:") != -1:
            NextMonkeyDivTrue = int(line.split("monkey ")[1])
        elif line.find("If false:") != -1:
            NextMonkeyDivFalse = int(line.split("monkey ")[1])
            ##this will come last so create the stupid monkey
            monkeyList.append(StupidMonkey(Items, divider, NextMonkeyDivTrue, NextMonkeyDivFalse, monkeyOperand, operandValue))

    NbrOfRounds = 10000

    moduloDivider = 1 #for part2, see https://en.wikipedia.org/wiki/Chinese_remainder_theorem

    for i in range(len(monkeyList)):
        moduloDivider *= monkeyList[i].divider

    for i in range(NbrOfRounds):
        for mIndex in range(0, len(monkeyList)):
            cMonkey = monkeyList[mIndex]

            while cMonkey.items:
                currentItem = cMonkey.items.pop(0)
                cMonkey.inspectingItems += 1
                #newWorry = int(CalcOperation(cMonkey.MonkeyOperand, currentItem, cMonkey.OperandValue)/3) #part1
                newWorry = int(CalcOperation(cMonkey.MonkeyOperand, currentItem, cMonkey.OperandValue)) % moduloDivider
                if newWorry % cMonkey.divider == 0:
                    monkeyList[cMonkey.NextMonkeyDivTrue].items.append(newWorry)
                else:
                    monkeyList[cMonkey.NextMonkeyDivFalse].items.append(newWorry)

    for mIndex in range(len(monkeyList)):
        print("monkey",mIndex, "inspect: ", monkeyList[mIndex].inspectingItems)

