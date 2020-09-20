#!/usr/bin/python3
# coding=utf-8
import sys
import math
import random
import os
import io
import lab1


# Поиск всех простых чисел до P
def eratosthenes(p):
    s = [x for x in range(5, p + 1) if
         x not in [i for sub in [list(range(2 * j, p + 1, j)) for j in range(2, p // 2)] for i in sub]]
    return s[random.randint(0, s.__len__()-1)]


def isPrime(n):
    if n <= 2: return False
    for num in range(2, math.floor(math.sqrt(n)).__int__()):
        if n % num == 0: return False
    return True


def shamir_secret(p, m):
    if not isPrime(p): sys.exit('ERROR. [P] must be prime number.')
    Ca = 7
    Cb = 5

    print(lab1.genEuclideanAlgo(Ca, p-1))
    # print(lab1.genEuclideanAlgo(5, p-1))
    print('Ca = ', Ca)
    print('Cb = ', Cb)
    print(lab1.genEuclideanAlgo(Ca, p-1))
    Da = lab1.genEuclideanAlgo(Ca, p-1)[1]
    print('Da = ', Da)
    Db = lab1.genEuclideanAlgo(Cb, p-1)[1]
    print('Db = ', Db)
    # print(Ca, Cb, Da, Db)
    x1 = lab1.fastModuloExponentiation(m, Ca, p)
    print(x1)
    x2 = lab1.fastModuloExponentiation(x1, Cb, p)
    print(x2)
    x3 = lab1.fastModuloExponentiation(x2, Da, p)
    print(x3)
    x4 = lab1.fastModuloExponentiation(x3, Db, p)
    print(x4)
    # print(m.__len__().__int__())
    # for i in range(m.__len__().__int__()):
        # print(i)
    print(x4, ' == ', m)
        # if not x4[i] == m[i]:
        #     print(1)
        #     return False
    return True


# def el_gamal(p):
#
# def vernam(p):
#
# def rsa(p):
#
def main():
    # Section №0 -- # Menu
    print('''Select case:
            1) Shamir secret
            2) El Gamal
            3) Vernam
            4) RSA''')

    select = int(input())

    if select == 1:
        with open("testData/giphy.gif", "rb") as image:
            data = image.read()
            m = bytes(data)
        print("Enter big prime number: ")
        p = int(input())
        m = 10
        print(shamir_secret(p, m))

    # if select == 2:
    #     el_gamal()
    #
    # if select == 3:
    #     vernam()
    #
    # if select == 4:
    #     rsa()


if __name__ == "__main__":
    main()
