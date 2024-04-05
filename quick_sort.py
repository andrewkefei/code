list1 = [0, -1, 7, 2, 3, 3, 2, 1, 4, 9]


def re(list1):
    if len(list1) <= 1:
        return list1

    pivot = list1.pop()
    small = []
    big = []

    for i in list1:
        if i <= pivot:
            small.append(i)
        else:
            big.append(i)
    return re(small) + [pivot] + re(big)


if __name__ == "__main__":
    print(re(list1))
