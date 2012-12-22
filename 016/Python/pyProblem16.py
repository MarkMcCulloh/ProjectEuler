#Problem 16

def main():
    List = list(str(2**1000))
    Sum = 0
    for i in List:
        Sum += int(i)
    print Sum

if __name__ == '__main__':
    main()