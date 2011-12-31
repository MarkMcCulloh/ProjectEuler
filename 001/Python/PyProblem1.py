#Mark McCulloh
#Project Euler: Problem 1

def main():
    Sum = 0
    for i in range(1000):
        if not i % 5 or not i % 3: Sum += i
    print Sum

if __name__ == '__main__':
    main()
