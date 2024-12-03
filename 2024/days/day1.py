from collections import Counter


def main():
    lines = open("../inputs/day1.txt", "r").readlines()
    data = [line.split() for line in lines]
    list1 = []
    list2 = []
    for item in data:
        list1.append(int(item[0]))
        list2.append(int(item[1]))

    list1.sort()
    list2.sort()

    difference = 0

    for i in list1:
        diff = abs(list1[i] - list2[i])
        difference += diff

    print(difference)

    counter = Counter(list2)
    total_part_2 = 0

    for i in list1:
        total_part_2 += i * counter[i]

    print(total_part_2)


main()
