#!/usr/bin/python3
# coding=utf-8
import sys
import math
import random
import os
import io
import lab1


def isPrime(n):
    if n <= 2: return False
    for num in range(2, math.floor(math.sqrt(n))):
        if n % num == 0: return False
    return True


def shamir_secret(m, p):
    if not (isPrime(p) and (p > 255)): sys.exit('ERROR. [P] must be prime number or p <= 255.')
    Ca = lab1.generate_g(p)
    Cb = lab1.generate_g(p)
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
        # out1 = [] * m.__len__()
        # out2 = [] * m.__len__()
        # out3 = [] * m.__len__()
        # out4 = [] * m.__len__()
        # out1 = bytearray(x1)
        # out2 = bytearray(x2)
        # out3 = bytearray(x3)
        out = bytearray(x4)
        # with open("x1.jpg", 'wb') as f:
        #     f.write(out1)
        # with open("x2.jpg", 'wb') as f:
        #     f.write(out2)
        # with open("x3.jpg", 'wb') as f:
        #     f.write(out3)
        with open("Shamir_out.jpg", 'wb') as f:
            f.write(out)
        for i in range(0, m.__len__()):
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
            r[i] = lab1.fastModuloExponentiation(g, k[i], p)
            e[i] = m[i] * lab1.fastModuloExponentiation(Db, k[i], p) % p
            mx[i] = e[i] * lab1.fastModuloExponentiation(r[i], p - 1 - Cb, p) % p
        out = bytearray(mx)
        with open("elGamal_out.jpg", 'wb') as f:
            f.write(out)
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


class Vernam:

    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.mx = [0] * m.__len__()
        self.decrypted_message = [0] * m.__len__()

    def encrypt(self):
        mx = [0] * self.m.__len__()
        for i in range(0, self.m.__len__()):
            print(i)
            self.mx[i] = self.m[i] ^ self.k[i]
        return self.mx

    def decrypt(self):
        for i in range(0, self.m.__len__()):
            self.decrypted_message[i] = self.mx[i] ^ self.k[i]
        return self.decrypted_message

    def compare(self):
        for i in range(0, self.m.__len__()):
            if self.m[i] == self.decrypted_message[i]:
                print(self.decrypted_message[i], ' == ', self.m[i])
                continue
            else:
                print(self.decrypted_message[i], ' != ', self.m[i])
                print("Error!")
                return False
        print("Successful!")
        return True


class RSA:
    # m < N
    def __init__(self, p, q, m):
        if m is None:
            self.m = []
        else:
            self.m = m
        self.N = p * q
        self.F = (p - 1) * (q - 1)
        self.D = lab1.generate_g(self.F)
        self.C = lab1.genEuclideanAlgo(self.D, self.F)[1]

    def encrypt(self, D, N):
        e = [0] * self.m.__len__()
        for i in range(0, self.m.__len__()):
            e[i] = lab1.fastModuloExponentiation(self.m[i], D, N)
        return e

    def decrypt(self, e):
        mx = [0] * e.__len__()
        for i in range(0, e.__len__()):
            mx[i] = lab1.fastModuloExponentiation(e[i], self.C, self.N)
        return mx

    @staticmethod
    def compare(mx, m):
        for i in range(0, m.__len__()):
            if m[i] == mx[i]:
                print(mx[i], ' == ', m[i])
                continue
            else:
                print(mx[i], ' != ', m[i])
                print("Error!")
                return False
        print("Successful!")
        return True


def main():
    select = 0
    # Section №0 -- # Menu
    print('''Select case:
            1) Shamir secret
            2) El Gamal
            3) Vernam
            4) RSA''')
    if select < 1 or select > 4:
        sys.exit("Тебе же сказали, выбери число от 1 до 4")
    try:
        select = int(input())
    except ValueError:
        print("Тебе же сказали, выбери число от 1 до 4")
    except UnboundLocalError:
        print("Тебе же сказали, выбери число от 1 до 4")

    if select == 1:
        with open("testData/test.jpg", "rb") as f:
            m = f.read()
            print(m)
        f.close()
        p = lab1.generate_p()
        print("P = ", p)
        print(shamir_secret(m, p))

    if select == 2:
        with open("testData/test.jpg", "rb") as f:
            m = f.read()
            print(m)
        f.close()
        p = lab1.generate_p()
        print("P = ", p)
        g = lab1.generate_g(p)
        print("G = ", g)
        el_gamal(p, g, m)

    if select == 3:
        with open("testData/test.jpg", "rb") as f:
            m = f.read()
            print(m)
        f.close()
        k = []
        for i in range(0, m.__len__()):
            k.append(random.randint(0, 255))
            # Проверка на длину ключа

        vernam = Vernam(m, k)
        encrypt = vernam.encrypt()
        decrypt = vernam.decrypt()
        print(vernam.compare())
        out = bytearray(encrypt)
        out2 = bytearray(decrypt)
        with open("Vernam_enc.jpg", 'wb') as f:
            f.write(out)
        with open("Vernam_dec.jpg", 'wb') as f:
            f.write(out2)
        del vernam

    if select == 4:
        with open("testData/test.jpg", "rb") as f:
            m = f.read()
            print(m)
        f.close()
        P = lab1.generate_p()
        print("P = ", P)
        Q = lab1.generate_p()
        print("Q = ", Q)
        Alice = RSA(P, Q, m)
        Bob = RSA(P, Q, None)
        encrypted_message = Alice.encrypt(Bob.D, Bob.N)
        print(encrypted_message)
        decrypted_message = Bob.decrypt(encrypted_message)
        RSA.compare(decrypted_message, m)
        out2 = bytearray(decrypted_message)
        with open("RSA_dec.jpg", 'wb') as f:
            f.write(out2)

        del Alice, Bob


if __name__ == "__main__":
    main()
