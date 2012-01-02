#Project Euler: Problem 4

def main():
    N = 3
    Max = (10 **  N     ) - 1
    Min = (10 ** (N - 1)) - 1
    a = b = Max
    Combos = []
    while a > Min:
        b = Max
        while b > Min:
            Combos.append(str(a * b))
            b -= 1
        a -= 1
    Palindromes = []
    Combos.sort()
    for i in Combos:
        test1 = list(i)
        test2 = list(i)
        test1.reverse()
        if test1 == test2: Palindromes.append(int(i))
    print max(Palindromes)


if __name__ == '__main__':
    main()
