#!/usr/bin/python3

import sys
import math
import random


def isPrime(n):
    if n <= 2: return False
    for num in range(2, math.floor(math.sqrt(n).__int__())):
        if n % num == 0: return False
    return True


def mulinv(b, n):
    g, x, _ = genEuclideanAlgo(b, n)
    if g == 1:
        return x % n


def fastModuloExponentiation(a, x, p):
    if not isPrime(p): sys.exit('ERROR. [P] must be prime number.')
    if 1 > x >= p: sys.exit('ERROR. [X] Must be from range (1, 2, ... , p-1)')
    result = 1
    tmp = a
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
    # if b > a: a, b = b, a
    #
    # U, V = [a, 1, 0], [b, 0, 1]
    #
    # while V[0] != 0:
    #     tmp = U[0] // V[0]
    #     tmpList = [U[0] % V[0], U[1] - tmp * V[1], U[2] - tmp * V[2]]
    #     U, V = V, tmpList
    # return U
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = genEuclideanAlgo(b % a, a)
        return g, y - (b // a) * x, x


def diffieHellmanProtocol(q):
    if not isPrime(q): sys.exit('ERROR. [q] must be prime number.')
    p = q * 2 + 1
    if not isPrime(p): sys.exit('ERROR. [p = 2q + 1] must be prime number.')

    g = random.randint(1, p - 1)
    while fastModuloExponentiation(g, q, p) == 1: g = random.randint(1, p - 1)

    xA, xB = random.randint(1, 10), random.randint(1, 10)
    yA, yB = fastModuloExponentiation(g, xA, p), fastModuloExponentiation(g, xB, p)
    zA, zB = fastModuloExponentiation(yB, xA, p), fastModuloExponentiation(yA, xB, p)

    if zA != zB: print('ERROR. [Diffie-Hellman] zA != zB')
    return zA


def babyGiantStep(a, p, y):
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
            if fastModuloExponentiation(a, ans, p) == y:
                return ans
        val2 = (val2 * k) % p
        i += 1
        # Общая сложность sqrt(p)*log^2(p)
    return -1


def main():
    mulinv(15, 23)
    # Section №0 -- # Menu
    print('''Select case:
        1) Fast Modulo Exponential
        2) Euclidean algorithm
        3) Diffie-Hellman protocol
        4) Baby-step, giant-step''')

    select = int(input())

    if select == 1:
        # Section №1 --- # Fast modulo exponential
        print('input g, x(1, 2, ... , p-1), p(Prime), :')
        g, x, p = int(input()), int(input()), int(input())
        # print('Generate g...')
        # g = generate_G(p)

        print(fastModuloExponentiation(g, x, p))

    if select == 2:
        # Section №2 --- # Generalized Euclidean algorithm.
        print('input a, b:')
        a, b = int(input()), int(input())

        gcd, x, y = genEuclideanAlgo(a, b)

        print('GCD = ', gcd, 'X = ', x, 'Y = ', y)

    if select == 3:
        # Section №3 --- # Diffie-Hellman protocol. Generating common key's.
        print('input q(Prime)')
        q = int(input())
        print(diffieHellmanProtocol(q))

    if select == 4:
        # Section №4 --- # Baby step, Giant step algorithm.
        print('input g, p, y:')
        g, p, y = int(input()), int(input()), int(input())

        result = babyGiantStep(g, p, y)
        print(g, '^', result, ' mod ', p, ' = ', y)


if __name__ == "__main__":
    main()
