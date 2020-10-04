import hashlib

from Crypto.Hash import SHA256
import sys

from Crypto.Util.number import inverse

import lab1


class signatureRSA:
    def __init__(self, p, q, m):
        if m is None:
            self.m = []
        else:
            self.m = int.from_bytes(m, byteorder='big')
        self.N = p * q
        self.F = (p - 1) * (q - 1)
        self.D = lab1.generate_g(self.F)
        self.C = inverse(self.F, self.D)
        self.Y = -1
        self.S = -1
        self.W = -1

    def encode(self):
        self.Y = self.m
        self.S = pow(self.Y, self.C, self.N)

    def decode(self, s, D, N):
        self.Y = self.m
        self.W = pow(s, D, N)

    def compare(self):
        if self.Y == self.W:
            print(self.Y, ' == ', self.W)
        else:
            print(self.Y, ' != ', self.W)
            print("Error!")
            return False
        print("Successful!")
        return True


class signatureElGamal:

    def __init__(self, p, g, m):
        self.p = p
        self.g = g
        self.h = int.from_bytes(m, byteorder='big')
        print(self.h)
        self.x = lab1.generate_g(p - 2)
        self.y = pow(self.g, self.x, self.p)
        self.k = lab1.generate_g(p - 2)
        self.r = 0
        self.u = 0
        self.s = 0
        self.k_tmp = 0

    def encode(self):
        self.r = pow(self.g, self.k, self.p)
        self.k_tmp = inverse(self.k, self.p-1)
        self.s = self.k_tmp * (self.h-self.x*self.r) % (self.p-1)

    def decode(self, s, r):
        left = pow(self.y, r, self.p) % self.p * pow(r, s, self.p) % self.p
        right = pow(self.g, self.h, self.p)
        return left, right

    def compare(self, left, right):
        if left == right:
            print(left, ' == ', right)
        else:
            print(left, ' != ', right)
            print("Error!")
            return False
        print("Successful!")
        return True


class signatureGOST:
    pass


def main():
    select = 0
    # Section №0 -- # Menu
    print('''Select case:
                1) signatureRSA
                2) signatureElGamal
                3) signatureGOST''')

    try:
        select = int(input())
    except ValueError:
        sys.exit("Тебе же сказали, выбери число от 1 до 3")
    except UnboundLocalError:
        sys.exit("Тебе же сказали, выбери число от 1 до 3")

    if select < 1 or select > 3:
        sys.exit("Тебе же сказали, выбери число от 1 до 3")

    if select == 1:
        hasher = hashlib.new('sha256')
        with open("testData/test.jpg", "rb") as f:
            m = f.read()
            hasher.update(m)
        f.close()
        P = lab1.generate_p()
        print("P = ", P)
        Q = lab1.generate_p()
        print("Q = ", Q)
        Alice = signatureRSA(P, Q, hasher.digest())
        Bob = signatureRSA(P, Q, hasher.digest())
        Alice.encode()
        Bob.decode(Alice.S, Alice.D, Alice.N)
        # print('Bob Y = ', Bob.Y)
        # print('Bob W = ', Bob.W)
        # print('Bob S = ', Bob.S)
        # print('Bob C = ', Bob.C)
        # print('Bob N = ', Bob.N)
        # print('Alice Y = ', Alice.Y)
        # print('Alice W = ', Alice.W)
        # print('Alice S = ', Alice.S)
        # print('Alice C = ', Alice.C)
        # print('Alice N = ', Alice.N)
        Bob.compare()

    if select == 2:
        hasher = hashlib.new('sha256')
        with open("testData/test.jpg", "rb") as f:
            m = f.read()
            hasher.update(m)
        f.close()
        P = lab1.generate_p()
        print("P = ", P)
        G = lab1.generate_g(P)
        print("G = ", G)
        Alice = signatureElGamal(P, G, m)
        Alice.encode()
        Bob = signatureElGamal(P, G, m)
        compare_value = Bob.decode(Alice.r, Alice.s)
        Bob.compare(compare_value[0], compare_value[1])

    if select == 3:
        #Лень
        pass


if __name__ == "__main__":
    main()
