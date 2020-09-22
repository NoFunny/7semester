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
    return s[random.randint(0, s.__len__() - 1)]


def isPrime(n):
    if n <= 2: return False
    for num in range(2, math.floor(math.sqrt(n))):
        if n % num == 0: return False
    return True


def shamir_secret(p, m):
    if not isPrime(p): sys.exit('ERROR. [P] must be prime number.')
    Ca = eratosthenes(p - 1)
    Cb = eratosthenes(p - 1)
    Da = lab1.genEuclideanAlgo(Ca, p - 1)[1]
    Db = lab1.genEuclideanAlgo(Cb, p - 1)[1]
    if int.from_bytes(m, 'big') >= p:
        # print('m = ', m)
        # print('m = ', int.to_bytes(m, m, byteorder='little'))
        # m = int.to_bytes(m[0], m, byteorder='big')
        x1 = [0] * m.__len__()
        x2 = [0] * m.__len__()
        x3 = [0] * m.__len__()
        x4 = [0] * m.__len__()
        print(Ca, Cb, Da, Db)

        for i in range(0, m.__len__()):
            x1[i] = lab1.fastModuloExponentiation(m[i], Ca, p)
            x2[i] = lab1.fastModuloExponentiation(x1[i], Cb, p)
            x3[i] = lab1.fastModuloExponentiation(x2[i], Da, p)
            x4[i] = lab1.fastModuloExponentiation(x3[i], Db, p)
            # Проверка на равность полученного сообщения и изначального
        for i in range(0, m.__len__()):
            # print(x4)
            if x4[i] == m[i]:
                print(x4[i], ' == ', m[i])
                continue
            else:
                print(x4[i], ' != ', m[i])
                return False
        return True
    else:
        x1 = lab1.fastModuloExponentiation(int.from_bytes(m, 'big'), Ca, p)
        x2 = lab1.fastModuloExponentiation(x1, Cb, p)
        x3 = lab1.fastModuloExponentiation(x2, Da, p)
        x4 = lab1.fastModuloExponentiation(x3, Db, p)
        # Проверка на равность полученного сообщения и изначального
        if not x4 == int.from_bytes(m, 'big'):
            print(x4, ' != ', m)
            return False
        return True


# def el_gamal(p):
#
# def vernam(p):
#
# def rsa(p):1
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
        with open("lab2.py", "rb") as f:
            m = f.read()
            print(m)
        f.close()
        print("Enter p(Prime and p > 255):")
        p = int(input())
        # print('m = ', int.from_bytes(m))
        # print(int.from_bytes(m, 'big') > p)
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
