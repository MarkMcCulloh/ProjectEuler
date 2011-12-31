#Mark McCulloh
#Project Euler: Problem 2

#Doesn't use a list
def main():
    Last_2 = 1
    Last_1 = 2
    EvenSum = 2
    Current = 0
    while Current < 4000000:
        Current = Last_1 + Last_2
        if not Current % 2: EvenSum += Current
        Last_2 = Last_1
        Last_1 = Current
    print EvenSum

if __name__ == '__main__':
    main()
