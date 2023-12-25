# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#borrowed solution, unknown source
def s2i(sval):
    ival = 0
    power5 = 5 ** len(sval)
    for c in sval:
        power5 //= 5
        if c == '1' or c == '2':
            ival += power5 * int(c)
        elif c == '=':
            ival -= power5 * 2
        elif c == '-':
            ival -= power5
    return ival


def i2s(ival):
    if ival == 0:
        return ''

    matchval = ival % 5
    print(ival)

    if matchval == 0 or matchval == 1 or matchval == 2:

        return i2s(ival // 5) + str(ival % 5)
    elif matchval == 3:

        return i2s(1 + ival // 5) + '='
    elif matchval == 4:

        return i2s(1 + ival // 5) + '-'


reqts = open("../../../Advent/2022_day25.txt").read().split()

print("PART 1: SNAFU sum:", i2s(sum([s2i(r) for r in reqts])))

# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
