# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def calcOperation(operand,leftmonkey,rightmonkey):
    returnvalue = 0
    if operand == "*":
        returnvalue = int(leftmonkey * rightmonkey)
    elif operand =="+":
        returnvalue = leftmonkey + rightmonkey
    elif operand == "-":
        returnvalue = leftmonkey - rightmonkey
    elif operand == "/":
        returnvalue = int(leftmonkey/rightmonkey)
    return returnvalue

def FindMonkey(monkeyName,monkeylist):
    returnval = -1
    for monkey in monkeylist:
        if monkey.monkeyName == monkeyName:
            returnval = monkey

    return returnval

class Monkey:
    monkeyName = ""
    monkeyOne = ""
    monkeyTwo = ""
    MonkeyOperand = ""
    MonkeyValue = 0
    pLeftMonkey = 0
    pRightMonkey = 0

    def __init__(self, monkeyName, monkeyOne, monkeyTwo, MonkeyOperand, MonkeyValue):
        self.monkeyName = monkeyName
        self.monkeyOne = monkeyOne
        self.monkeyTwo = monkeyTwo
        self.MonkeyOperand = MonkeyOperand
        self.MonkeyValue = MonkeyValue

    def setMonkeys(self, leftMonkeyName, rightMonkeyName, monkeyList):
        self.pLeftMonkey = FindMonkey(leftMonkeyName, monkeylist)
        self.pRightMonkey = FindMonkey(leftMonkeyName, monkeylist)

    def getvaluePointer(self, monkeylist):
        if self.MonkeyValue != 0:
            return self.MonkeyValue
        else:
            returnval =calcOperation(self.MonkeyOperand, self.pLeftMonkey.getvalue(monkeylist), self.pRightMonkey.getvalue(monkeylist))

            return returnval

    def getvalue(self, monkeylist):
        if self.MonkeyValue != 0:
            return self.MonkeyValue
        else:
            returnval =calcOperation(self.MonkeyOperand,FindMonkey(self.monkeyOne,monkeylist).getvalue(monkeylist),FindMonkey(self.monkeyTwo,monkeylist).getvalue(monkeylist))
            return returnval


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Rows = open("../../../Advent/2022_day21.txt", 'r').read().strip().split("\n")

    monkeylist =[]
    for Row in Rows:
        splitname = Row.split(":")
        monkeyName = (splitname[0]) #names
        value = 0
        leftMonkey = ""
        rightMonkey = ""
        operator = ""

        #there is a library for operator. can use dictionary to link character to operator type
        if Row.find("+") != -1:
            operator = "+"
        elif Row.find("-") != -1:
            operator = "-"
        elif Row.find("*") != -1:
            operator = "*"
        elif Row.find("/") != -1:
            operator = "/"
        else:
            operator = ""
            value = int(Row.split(":")[1])

        if operator != "":
            leftMonkey = splitname[1].split(operator)[0].strip()
            rightMonkey = splitname[1].split(operator)[1].strip()
        if monkeyName == "root": #part 2
            operator = "-"

        monkeylist.append(Monkey(monkeyName,leftMonkey,rightMonkey,operator,value))

    humanMonkey = FindMonkey("humn",monkeylist)

    #link the pointers to other monkeys:
    for monk in monkeylist:
        if monk.monkeyOne != "":
            monk.pLeftMonkey = FindMonkey(monk.monkeyOne,monkeylist)
        if monk.monkeyTwo != "":
            monk.pRightMonkey = FindMonkey(monk.monkeyTwo,monkeylist)

    rootmonkey = FindMonkey("root", monkeylist)

    low = -100000000000000
    high = 100000000000000

    #do binary search
    while (low+1) < high:
        candidate = int((low + high) // 2)
        if candidate == 0: #is used if monkey value depend on others
            candidate += 1
        humanMonkey.MonkeyValue = candidate
        result = rootmonkey.getvaluePointer(monkeylist)
        if result == 0:
            print(humanMonkey.MonkeyValue, "FOUND")
            break
        if result > 0:
            low = candidate
        else:
            high = candidate

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
