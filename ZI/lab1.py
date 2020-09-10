#!/usr/bin/python3
import sys
import math
import random

def isPrime(n):
    if (n <= 2): return False
    for num in range(2, math.floor(math.sqrt(n))):
        if (n % num == 0): return False
    return True

def fastModuloExponentiation(a, x, p):
    if not isPrime(p): sys.exit('ERROR. [P] must be prime number.')
    if x < 1 or x >= p: sys.exit('ERROR. [X] Must be from range (1, 2, ... , p-1)')
    
    result = 1
    t = math.floor(math.log2(x))
    tmp = a
    for num in range(t + 1):
        if num > 0: tmp *= tmp % p

        if (x % 2) == 1:
            result *= tmp
        x >>= 1

    return result % p
        

def genEuclideanAlgo(a, b):
    if b > a: a, b = b, a
    
    U, V = [a, 1, 0], [b, 0, 1]

    while (V[0] != 0):
        tmp = U[0] // V[0]
        tmpList = [U[0] % V[0], U[1] - tmp * V[1], U[2] - tmp * V[2]]
        U, V = V, tmpList
    return U

def diffieHellmanProtocol(p, g):
    if not isPrime(p): sys.exit('ERROR. [P] must be prime number.')

    q = (p - 1) / 2

    if not isPrime(q): sys.exit('ERROR. [Q] must be prime number.')
    if g <= 1 and g >= p - 1: sys.exit('ERROR. [G] Must be (1 < g < p - 1)')
    if fastModuloExponentiation(g, q, p) == 1: sys.exit('ERROR. [G] Must be (g^q mod p != 1)')

    xA, xB = random.randint(1, 10), random.randint(1, 10)
    yA, yB = fastModuloExponentiation(g, xA, p), fastModuloExponentiation(g, xB, p)
    zA, zB = fastModuloExponentiation(yB, xA, p), fastModuloExponentiation(yA, xB, p)
    
    if zA != zB: print('ERROR. zA != zB')

    return zA
    

def firstEntry(list, x): 
    index = 0
    
    for elem in list:
        if elem == x: return index
        index += 1

    return -1

def babyGiantStep(a, p, y):
    # random generate m & k
    m, k = random.randint(1, 10) * math.floor(math.log2(p))+2, random.randint(1, 10) * math.floor(math.log2(p))+2    
    # --------------

    result = [0, 0]
    giantSteps, babySteps = [fastModuloExponentiation(a, m, p)], [y]

    for j in range(1, m):
        babySteps.append((a * babySteps[j-1]) % p) # in this case faster than call.fastModuloExponentiation()

    for i in range(1, k - 1):
        result[i] = firstEntry(babySteps, giantSteps[i - 1])
        if result[i] != -1: 
            result[0] = i
            break
        giantSteps.append((giantSteps[i-1] * giantSteps[i-1]) % p)
    
    return result[0] * m - result[1]

def main():
    # Section №0 -- # Menu
    print('''Select case:
        1) Fast Modulo Exponentioal
        2) Euclidean algorithm
        3) Diffi-Hallman protocol
        4) Baby-step, giant-step''')

    select = int(input())

    if select == 1:
        # Section №1 --- # Fast modulo expotential
        print('input p(Prime), a, x(1, 2, ... , p-1):')
        p, a, x = int(input()), int(input()), int(input())

        print(fastModuloExponentiation(a, x, p))

    if select == 2:
        # Section №2 --- # Generalized Euclidean algorithm.
        print('input a, b:')
        a, b = int(input()), int(input())

        gcd, x, y = genEuclideanAlgo(a, b)

        print('GCD = ', gcd, 'X = ', x, 'Y = ', y)

    if select == 3:
        # Section №3 --- # Diffi-Hallman protocol. Generating common key's.
        print('input p(Prime), g(1 < g < p - 1):')
        p, g = int(input()), int(input())
        # if not isPrime(p): sys.exit('ERROR. You entered a composite number. Try again.')
        print(diffieHellmanProtocol(p, g))
        
    if select == 4:
        # Section №4 --- # Baby step, Giant step algorithm.
        print('input a, p, y:')
        a, p, y = int(input()), int(input()), int(input())

        result = babyGiantStep(a, p, y)

        if fastModuloExponentiation(a, result, p) == y: print(a, '^', result, ' mod ', p, ' = ', y)
        else: print('Verification failed')



if __name__ == "__main__":
    main()