#Project Euler: Problem 3

def main():
    i = int(600851475143 ** .5)
    while i > 0:
        if i % 2 == 0:
            i -= 1
            continue
        Prime = True
        if 600851475143 % i == 0:
            print i
            for a in range(2, i / 2):
                if i % a == 0:
                    Prime = False
                    break
            if Prime:
                break
        i -= 1
    print i

if __name__ == '__main__':
    main()
