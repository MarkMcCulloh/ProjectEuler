def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

BestPrimes = filter(lambda x: x % 3 == 1,primes(1370743248841+1))

##

import itertools

#The 843553th prime is 12906067

#Primes = [7, 13, 19, 31, 37, 43, 61, 67, 73, 79, 97, 103, 109, 127, 139, 151, 157, 163, 181, 193, 199, 211, 223, 229, 241, 271, 277, 283]
Primes = [7, 13, 19, 31, 37, 43, 61, 67, 73, 79]

TFactorList = []
DFactorList = []
FinalList = []
Counter = 0
MAX = 500000000000

#Every permutation of the primelist, in sets of three
TFactorList = list(itertools.permutations(Primes, 3))
DFactorList = list(itertools.permutations(Primes, 2))

####

for Triplet in TFactorList:
    Number = (Triplet[0]**2)*(Triplet[1]**4)*(Triplet[2]**4)
    FinalList.append(Number)

for Couple in DFactorList:
    Number = (Couple[0]**14)*(Couple[1]**4)
    FinalList.append(Number)
    Number = (Couple[0]**24)*(Couple[1]**2)
    FinalList.append(Number)

#FinalList = list(set(FinalList))

FinalList = map(lambda x: int(x**.5), FinalList)

'''for n in range(len(FinalList)):
    print DFactorList[n]
    print '{0:f}'.format(FinalList[n])'''

'''for n in FinalList:
    Tester = n
    SCounter = 1
    while Tester <= MAX:
        if not SCounter in ManyPrimes:
            Counter += 1
            Tester = n * SCounter
        SCounter += 1
    print Counter'''

for n in FinalList:
    Counter1 = Counter2 = 0
    N1 = (MAX // n)
    N2 = N1 ** 2
    # find the largest number in ManyPrimes such that:

    A = 0

    while BestPrimes[A] * (n ** .5) <= MAX:
        if BestPrimes[A] * n <= MAX:
            Counter1 += 1
        Counter2 += 1
        A += 1

    Counter -= Counter1 + Counter2

    print n
    print N1, N2
    print Counter1, Counter2
    print Counter
    print ''

print "\nThe answer is:",Counter

#Wrong Answers
#34963320
#106708864
#66108600
#53354432
#33054300
#66116003
#66116007
#33061707
#53362268
#33061703
#65797146
#66434868