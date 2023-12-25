# This is a sample Python script.

# Press Skift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("../../../Advent/2020_day5.txt", 'rt') as f:
        line = [line.strip() for line in f.readlines()]

    ID = []
    for li in line:
        IDnew = 0
        for i in range(10):
            IDnew += pow(2,7-i+2) if li[i] == 'B' or li[i] == 'R' else 0

        ID.append(IDnew)

    ID.sort()
    #part 1: \
    print("part1: ",ID.pop())

    #part 2:
    for i in range(len(ID)-1):
        if ID[i+1] != ID[i]+1:
            print("part2: ",ID[i]+1)
            break


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
