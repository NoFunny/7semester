#!/usr/bin/python3
import sys
import math
import random
import operator

def isPrime(n):
    if n <= 2: return False
    for num in range(2, math.floor(math.sqrt(n))):
        if n % num == 0: return False
    return True


def fastModuloExponentiation(a, x, p):
    if not isPrime(p): sys.exit('ERROR. [P] must be prime number.')
    if 1 > x >= p: sys.exit('ERROR. [X] Must be from range (1, 2, ... , p-1)')
    # if x < 0:
    #     a = genEuclideanAlgo()
    result = 1
    tmp = a
    while x:
        if x & 1:
            result = (result * tmp) % p
        tmp = (tmp * tmp) % p
        x >>= 1
    return result



def genEuclideanAlgo(a, b):
    if b > a: a, b = b, a

    U, V = [a, 1, 0], [b, 0, 1]

    while V[0] != 0:
        tmp = U[0] // V[0]
        tmpList = [U[0] % V[0], U[1] - tmp * V[1], U[2] - tmp * V[2]]
        U, V = V, tmpList
    return U


def diffieHellmanProtocol(p, g):
    if not isPrime(p): sys.exit('ERROR. [P] must be prime number.')

    q = (p - 1) / 2

    if not isPrime(q): sys.exit('ERROR. [Q] must be prime number.')
    if 1 >= g >= p - 1: sys.exit('ERROR. [G] Must be (1 < g < p - 1)')
    if fastModuloExponentiation(g, q, p) == 1: sys.exit('ERROR. [G] Must be (g^q mod p != 1)')

    xA, xB = random.randint(1, 10), random.randint(1, 10)
    yA, yB = fastModuloExponentiation(g, xA, p), fastModuloExponentiation(g, xB, p)
    zA, zB = fastModuloExponentiation(yB, xA, p), fastModuloExponentiation(yA, xB, p)

    if zA != zB: print('ERROR. zA != zB')

    return zA

def babyGiantStep(a, p, y):
    # random generate m & k
    # gn и n = m и k
    # log(p)
    # g^n mod p
    m, k = random.randint(1, 10) * math.floor(math.sqrt(p)) + 1, random.randint(1, 10) * math.floor(math.sqrt(p)) + 1

    # --------------
    steps = ({})
    n = math.floor(math.sqrt(p)+1)
    gn = fastModuloExponentiation(a,n,p)

    val1 = gn
    print('m = ', m)
    print('k = ', k)
    # m = n = sqrt(p)
    # Получение элемента: O(1).
    i = 0

    while i < m:
        steps[i] = val1
        val1 = (val1 * gn) % p
        i+=1

    val2 = y % p
    j = 0
    while j <= k-1:
        # Проход по словарю: O(n).
        if steps.get(val2):
            ans = steps.get(val2) * n - j
            if ans < p:
                return ans

        val2 = (val2 * a)  % p
        j+=1

    return -1


def main():
    # Section №0 -- # Menu
    print('''Select case:
        1) Fast Modulo Exponential
        2) Euclidean algorithm
        3) Diffie-Hellman protocol
        4) Baby-step, giant-step''')

    select = int(input())

    if select == 1:
        # Section №1 --- # Fast modulo exponential
        print('input p(Prime), a, x(1, 2, ... , p-1):')
        a, x, p = int(input()), int(input()), int(input())

        print(fastModuloExponentiation(a, x, p))

    if select == 2:
        # Section №2 --- # Generalized Euclidean algorithm.
        print('input a, b:')
        a, b = int(input()), int(input())

        gcd, x, y = genEuclideanAlgo(a, b)

        print('GCD = ', gcd, 'X = ', x, 'Y = ', y)

    if select == 3:
        # Section №3 --- # Diffie-Hellman protocol. Generating common key's.
        print('input p(Prime), g(1 < g < p - 1):')
        p, g = int(input()), int(input())
        # if not isPrime(p): sys.exit('ERROR. You entered a composite number. Try again.')
        print(diffieHellmanProtocol(p, g))

    if select == 4:
        # Section №4 --- # Baby step, Giant step algorithm.
        print('input a, p, y:')
        a, p, y = int(input()), int(input()), int(input())

        result = babyGiantStep(a, p, y)
        print('Result', result)
        if fastModuloExponentiation(a, result, p) == y:
            print(a, '^', result, ' mod ', p, ' = ', y)
        else:
            print('Verification failed')

if __name__ == "__main__":
    main()