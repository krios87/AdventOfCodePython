# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#borrowed solution, unknown source
class Number:
    def __init__(self, value):
        self.value = value


def mix(filename, key=1, count=1):
    with open(filename) as file:
        original = [Number(int(num) * key) for num in file]

    nums = original.copy()

    for _ in range(count):
        for num in original:
            i = nums.index(num)
            new_i = (i + num.value) % (len(nums) - 1)

            nums.insert(new_i, nums.pop(i))
        print([nums[i].value for i in range(len(nums))])
    i_0 = nums.index(list(filter(lambda n: n.value == 0, nums))[0])

    return sum([nums[(i_0 + i) % len(nums)].value for i in range(1000, 3001, 1000)])


def part_1():
    return mix("../../../Advent/2022_day20.txt")


def part_2():
    return mix("../../../Advent/2022_day20.txt", key=811589153, count=10)


print(part_1())
#print(part_2())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    x = [int(x) for x in open('../../../Advent/2022_day20.txt')]
    j = list(range(len(x)))

    for i in range(len(x)):
        c = j.index(i)
        j.pop(c)
        j.insert((c + x[i]) % len(j), i)

    print(j)
    z = j.index(x.index(0))
    #print(sum(x[j[(z + i) % len(j)]] for i in [1000, 2000, 3000]))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
