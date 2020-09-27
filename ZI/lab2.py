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


def shamir_secret(m, p):
    if not (isPrime(p) and (p > 255)): sys.exit('ERROR. [P] must be prime number or p <= 255.')
    Ca = eratosthenes(p - 1)
    Cb = eratosthenes(p - 1)
    Da = lab1.genEuclideanAlgo(Ca, p - 1)[1]
    Db = lab1.genEuclideanAlgo(Cb, p - 1)[1]
    if int.from_bytes(m, 'big') >= p:
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
                print("Error!")
                return False
        print("Successful!")
        return True
    else:
        x1 = lab1.fastModuloExponentiation(int.from_bytes(m, 'big'), Ca, p)
        x2 = lab1.fastModuloExponentiation(x1, Cb, p)
        x3 = lab1.fastModuloExponentiation(x2, Da, p)
        x4 = lab1.fastModuloExponentiation(x3, Db, p)
        # Проверка на равность полученного сообщения и изначального
        if not x4 == int.from_bytes(m, 'big'):
            print(x4, ' != ', m)
            print("Error!")
            return False
        print(x4, ' == ', m)
        print("Successful!")
        return True


def el_gamal(p, g, m):
    if not isPrime(p): sys.exit('ERROR. [P] must be prime number or p <= 255.')
    Ca = random.randint(1, p - 1)
    Cb = random.randint(1, p - 1)  # Алгоритм евлкида
    Cd = random.randint(1, p - 1)
    Da = lab1.fastModuloExponentiation(g, Ca, p)
    Db = lab1.fastModuloExponentiation(g, Cb, p)
    Dc = lab1.fastModuloExponentiation(g, Cd, p)
    # Зачем нужны Ca, Cd, Da, Dc пока что не разобрался, но в методичке они есть
    if int.from_bytes(m, 'big') >= p:
        k = [0] * m.__len__()
        r = [0] * m.__len__()
        mx = [0] * m.__len__()
        e = [0] * m.__len__()

        for i in range(0, m.__len__()):
            k[i] = random.randint(1, p - 2)
            print(k[i])
            r[i] = lab1.fastModuloExponentiation(g, k[i], p)
            e[i] = m[i] * lab1.fastModuloExponentiation(Db, k[i], p) % p
            mx[i] = e[i] * lab1.fastModuloExponentiation(r[i], p - 1 - Cb, p) % p
        for i in range(0, m.__len__()):
            if mx[i] == m[i]:
                print(mx[i], ' == ', m[i])
                continue
            else:
                print(mx[i], ' != ', m[i])
                print("Error!")
                return False
        print("Successful!")
        return True
    else:
        k = random.randint(1, p - 2)
        r = lab1.fastModuloExponentiation(g, k, p)
        e = m * lab1.fastModuloExponentiation(Db, k, p) % p
        mx = e * lab1.fastModuloExponentiation(r, p - 1 - Cb, p) % p
    if m == mx:
        print(m, ' == ', mx)
        print("Successful!")
        return True
    print(m, ' != ', mx)
    print("Error!")
    return False


class vernam:

    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.mx = [0] * m.__len__()

    def encrypt(self):
        mx = [0] * self.m.__len__()
        for i in range(1, self.m.__len__()):
            self.mx[i] = self.m[i] ^ self.k[i]

    def decrypt(self):
        # mx = [0] * self.m.__len__()
        for i in range(1, self.m.__len__()):
            self.m[i] = self.mx[i] ^ self.k[i]

    def compare(self):
        for i in range(1, self.m.__len__()):
            if self.m[i] == self.mx[i]:
                print(self.mx[i], ' == ', self.m[i])
                continue
            else:
                print(self.mx[i], ' != ', self.m[i])
                print("Error!")
                return False
        print("Successful!")
        return True


# def rsa(p):
#
def main():
    # TODO:
    # Нужно сделать генерацию P и G!

    # Section №0 -- # Menu
    print('''Select case:
            1) Shamir secret
            2) El Gamal
            3) Vernam
            4) RSA''')

    select = int(input())

    if select == 1:
        with open("testData/ЛСП - Один.mp3", "rb") as f:
            m = f.read()
            print(m)
        f.close()
        print("Enter p(Prime and p > 255):")
        p = int(input())
        print(shamir_secret(m, p))

    if select == 2:
        with open("testData/test.jpg", "rb") as f:
            m = f.read()
            print(m)
        f.close()
        print("Enter p(Prime and p > 255):")
        p = int(input())
        print("Enter g :")
        g = int(input())
        el_gamal(p, g, m)

    if select == 3:
        # with open("testData/test.jpg", "rb") as f:
        #     m = f.read()
        #     print(m)
        # f.close()
        a = "1000"
        b = "1010"
        y = int(a, 2) ^ int(b, 2)
        print(bin(y)[2:].zfill(len(a)))

    #     vernam()
    #
    # if select == 4:
    #     rsa()


if __name__ == "__main__":
    main()
