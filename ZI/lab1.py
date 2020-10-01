#!/usr/bin/python3

import sys
import math
import random


# Поиск всех простых чисел до P
def eratosthenes(n, p):
    s = [x for x in range(n, p + 1) if
         x not in [i for sub in [list(range(2 * j, p + 1, j)) for j in range(2, p // 2)] for i in sub]]
    return s[random.randint(0, s.__len__() - 1)]


def isPrime(n):
    if (math.factorial(n - 1) + 1) % n != 0:
        return False
    else:
        return True


def mulinv(b, n):
    g, x, _ = genEuclideanAlgo(b, n)
    if g == 1:
        return x % n


def fastModuloExponentiation(a, x, p):
    if 1 > x >= p: sys.exit('ERROR. [X] Must be from range (1, 2, ... , p-1)')
    result = 1
    tmp = a
    if a == 0:
        return 0
    if x < 0:
        tmp = mulinv(a, p)
        x = -x
    while x:
        if x & 1:
            result = (result * tmp) % p
        tmp = (tmp * tmp) % p
        x >>= 1
    return result


def genEuclideanAlgo(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = genEuclideanAlgo(b % a, a)
        return g, y - (b // a) * x, x


def diffieHellmanProtocol():
    flag = 1
    while flag:
        q = eratosthenes(2, 110)
        print("q =", q)
        if not isPrime(q): sys.exit('ERROR. [q] must be prime number.')
        p = q * 2 + 1
        if not isPrime(p): flag = 1
        else: flag = 0

    g = random.randint(1, p - 1)
    while fastModuloExponentiation(g, q, p) == 1: g = random.randint(1, p - 1)

    xA, xB = random.randint(1, 10), random.randint(1, 10)
    yA, yB = fastModuloExponentiation(g, xA, p), fastModuloExponentiation(g, xB, p)
    zA, zB = fastModuloExponentiation(yB, xA, p), fastModuloExponentiation(yA, xB, p)

    if zA != zB: print('ERROR. [Diffie-Hellman] zA != zB')
    return zA


def babyGiantStep(a, p, y):
    if not isPrime(p): sys.exit('ERROR. [P] must be prime number.')
    steps = ({})
    # 2*sqrt(p)
    m = math.ceil(math.sqrt(p) + 1)
    k = fastModuloExponentiation(a, m, p)
    val1 = y % p
    i = 0

    # Время выполнения log(p)
    while i < m:
        print(steps)
        steps[val1] = i
        val1 = (val1 * a) % p
        i += 1
    val2 = fastModuloExponentiation(a, m, p)
    i = 1
    # Время выполнения log(p)
    while i <= k - 1:
        # Проход по словарю: O(k).
        if steps.__contains__(val2):
            print(steps[val2])
            ans = i * m - steps[val2]
            print('ans = ', ans)
            if fastModuloExponentiation(a, ans, p) == y:
                return ans
        val2 = (val2 * k) % p
        i += 1
        # Общая сложность sqrt(p)*log^2(p)
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
        g = random.randint(1, 23)
        p = eratosthenes(2, 110)
        x = random.randint(1, p-1)
        print("g = ", g)
        print("p = ", p)
        print("x = ", x)
        # g, x, p = int(input()), int(input()), int(input())

        print(fastModuloExponentiation(g, x, p))

    if select == 2:
        # Section №2 --- # Generalized Euclidean algorithm.
        print('input a, b:')
        a, b = int(input()), int(input())

        gcd, x, y = genEuclideanAlgo(a, b)

        print('GCD = ', gcd, 'X = ', x, 'Y = ', y)

    if select == 3:
        # Section №3 --- # Diffie-Hellman protocol. Generating common key's.
        print(diffieHellmanProtocol())

    if select == 4:
        # Section №4 --- # Baby step, Giant step algorithm.
        g = random.randint(1, 23)
        p = eratosthenes(2, 110)
        y = random.randint(1, 50)
        print("g = ", g)
        print("p = ", p)
        print("y = ", y)
        # g, p, y = int(input()), int(input()), int(input())

        result = babyGiantStep(g, p, y)
        print(g, '^', result, ' mod ', p, ' = ', y)


if __name__ == "__main__":
    main()
