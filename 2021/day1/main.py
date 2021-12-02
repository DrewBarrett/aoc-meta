def main():
    with open("./input.txt") as inp:
        array = []
        for line in inp:
            array.append(int(line.strip()))

        p1(array)
        p2(array)


def p1(arr):
    last = None
    answer1 = 0
    for num in arr:
        print(num, end="")
        if last is None:
            print(" N/A - No previous mesurement")
            last = num
            continue
        if last < num:
            answer1 = answer1 + 1
            print(" increased")
        else:
            print(" decreased")
        last = num

    print(answer1)


def p2(arr):
    answer2 = 0
    prev1 = None
    prev2 = None
    prev3 = None
    for num in arr:
        if prev1 is None or prev2 is None or prev3 is None:
            prev3 = prev2
            prev2 = prev1
            prev1 = num
            continue
        old = prev1 + prev2 + prev3
        new = num + prev1 + prev2
        if old < new:
            answer2 = answer2 + 1
        prev3 = prev2
        prev2 = prev1
        prev1 = num
    print(answer2)
if __name__ == '__main__':
    main()
