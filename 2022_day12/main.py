# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("../../../Advent/2022_day12.txt") as file:
        Map = []
        for line in file.readlines():
            OneRow = []
            for c in range(len(line)):
                char = line[c]
                if char != "\n":
                    OneRow.append(char)
            Map.append(OneRow)

    length = len(Map[0])
    NbrOfRows = len(Map)
    startX = Map[0].index("S")
    startY = 0
    for m in Map:
        print(m)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
