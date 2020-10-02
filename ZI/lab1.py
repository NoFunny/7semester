#!/usr/bin/python3

import sys
import math
import random


def miller_rabin(n, k):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    t = n - 1
    s = 0
    while t % 2 == 0:
        t /= 2
        s += 1
    for i in range(0, k):
        a = random.randint(2, n - 2)
        x = fastModuloExponentiation(a, int(t), int(n))
        if x == 1 or x == n - 1:
            continue
        for r in range(1, s):
            x = fastModuloExponentiation(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        if x != n - 1:
            return False
    return True


def generate_p():
    q = random.randint(10 ** 6, 10 ** 9)
    while not (miller_rabin(q, int(math.log2(q))) and miller_rabin(q * 2 + 1, int(math.log2(q * 2 + 1)))):
        q = random.randint(10 ** 6, 10 ** 9)
    return 2 * q + 1


def generate_g(p):
    while True:
        g = random.randint(2, 100)
        if fastModuloExponentiation(g, int((p - 1) / 2), p) != 1 and isPrime(g):
            return g


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
    q = 0
    p = 0
    while flag:
        p = generate_p()
        q = generate_g(p)
        print("q =", q)
        if not isPrime(q):
            print('ERROR. [q] must be prime number.')
            flag = 1
        else:
            flag = 0

    g = generate_g(p)
    while fastModuloExponentiation(g, q, p) == 1: g = random.randint(1, p - 1)

    xA, xB = random.randint(1, 10), random.randint(1, 10)
    yA, yB = fastModuloExponentiation(g, xA, p), fastModuloExponentiation(g, xB, p)
    zA, zB = fastModuloExponentiation(yB, xA, p), fastModuloExponentiation(yA, xB, p)

    if zA != zB: print('ERROR. [Diffie-Hellman] zA != zB')
    return zA


def babyGiantStep(a, p, y):
    if not isPrime(p): sys.exit('ERROR. [P] must be prime number.')
    C = 0
    M = 0

    m = k = math.ceil(math.sqrt(p))

    A = []
    B = []
    for i in range(0, m):
        A.append((a ** i * y) % p)
        M += 1
    for i in range(1, k * m):
        B.append((a ** (i * m)) % p)
        M += 1

    d = {}

    for i in range(0, len(A)):
        d[A[i]] = i
        M += 1

    for i in range(0, len(B)):
        C += 1
        if d.get(B[i]) is not None:
            break

    x = (i + 1) * m - d[B[i]]
    M += 1
    print("x = " + str(x))

    C += M
    print(C)
    return x


def main():
    select = 0
    # Section №0 -- # Menu
    print('''Select case:
        1) Fast Modulo Exponential
        2) Euclidean algorithm
        3) Diffie-Hellman protocol
        4) Baby-step, giant-step''')

    try:
        select = int(input())
    except ValueError:
        print("Тебе же сказали, выбери число от 1 до 4")
    except UnboundLocalError:
        print("Тебе же сказали, выбери число от 1 до 4")

    if select == 1:
        # Section №1 --- # Fast modulo exponential
        p = generate_p()
        g = generate_g(p)
        x = random.randint(1, p - 1)
        # print("g = ", g)
        # print("p = ", p)
        # print("x = ", x)
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
        p = generate_p()
        g = generate_g(p)
        y = random.randint(1, 10 ** 9)
        print("g = ", g)
        print("p = ", p)
        print("y = ", y)
        # g, p, y = int(input()), int(input()), int(input())

        result = babyGiantStep(g, p, y)
        print(g, '^', result, ' mod ', p, ' = ', y)


if __name__ == "__main__":
    main()
