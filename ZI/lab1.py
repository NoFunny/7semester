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
    result = 1
    t = math.floor(math.log2(x))
    tmp = a
    for num in range(t + 1):
        if num > 0: tmp *= tmp % p

        if (x % 2) == 1:
            result *= tmp
        x //= 2

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
    #sicret
    xA, xB = random.randint(1, 10), random.randint(1, 10)
    #open
    yA, yB = fastModuloExponentiation(g, xA, p), fastModuloExponentiation(g, xB, p)
    if yA >= p and yB >= p:
        sys.exit('Public key greatest mod')
    else:
        zA, zB = fastModuloExponentiation(yA, xA, p), fastModuloExponentiation(yB, xB, p)
    return zA == zB

def firstEntry(list, x): 
    index = 0
    
    for elem in list:
        if elem == x: return index
        index += 1

    return -1

def babyGiantStep(a, p, y):
    # random generate m & k
    m, k = random.randint(1, 10) * log2(p)+1, random.randint(1, 10) * log2(p)    
    # m, k = 6, 4
    # --------------

    result = [0, 0]
    iList, jList = [fastModuloExponentiation(a, m, p)], [y]

    for j in range(1, m):
        jList.append((a * jList[j-1]) % p) # in this case faster than call.fastModuloExponentiation()

    for i in range(1, k - 1):
        result[i] = firstEntry(jList, iList[i - 1])
        if result[i] != -1: 
            result[0] = i
            break
        iList.append((iList[i-1] * iList[i-1]) % p)
    
    return result[0] * m - result[1]

def main():
    # Section №1 --- # Fast modulo expotential
    p, a, x = int(input())

    if not isPrime(p): sys.exit('ERROR. You entered a composite number. Try again.')
    
    print(fastModuloExponentiation(a, x, p))

    # Section №2 --- # Generalized Euclidean algorithm.
    a, b = int(input()), int(input())

    gcd, x, y = genEuclideanAlgo(a, b)

    print('GCD = ', gcd, 'X = ', x, 'Y = ', y)

    # Section №3 --- # Diffi-Hallman protocol. Generating common key's.
    p, g = int(input()), int(input())

    print(diffieHellmanProtocol(p, g))

    # Section №4 --- # Baby step, Giant step algorithm.
    a, p, y = int(input()), int(input()), int(input())

    result = babyGiantStep(a, p, y)

    if fastModuloExponentiation(a, result, p) == y: print(a, '^', result, ' mod ', p, ' = ', y)
    else: print('Verification failed')

if __name__ == "__main__":
    main()