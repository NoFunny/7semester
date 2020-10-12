import hashlib

from Crypto.Hash import SHA256
import sys

from Crypto.Util.number import inverse

import lab1


class signatureRSA:
    def __init__(self, p, q, m):
        self.m = m
        self.P = p
        self.N = p * q
        self.F = (p - 1) * (q - 1)
        self.D = lab1.generate_g(self.F)
        self.C = lab1.mulinv(self.D, self.F)
        if int.from_bytes(self.m, 'big') >= p:
            self.Y = self.m
            self.S = [0] * self.m.__len__()
            self.W = [0] * self.m.__len__()
        else:
            self.Y = -1
            self.S = -1
            self.W = -1

    def encode(self):
        if int.from_bytes(self.m, 'big') >= self.P:
            for i in range(0, self.m.__len__()):
                self.S[i] = lab1.fastModuloExponentiation(self.Y[i], self.C, self.N)
        else:
            self.S = lab1.fastModuloExponentiation(self.m, self.C, self.N)

    def decode(self, S, D, N):
        self.Y = self.m
        if int.from_bytes(self.Y, 'big') >= self.P:
            for i in range(0, self.m.__len__()):
                self.W[i] = lab1.fastModuloExponentiation(S[i], D, N)
        else:
            self.W = lab1.fastModuloExponentiation(S, D, N)

    def compare(self):
        if int.from_bytes(self.m, 'big') >= self.P:
            for i in range(0, self.m.__len__()):
                if self.Y[i] == self.W[i]:
                    print(self.Y[i], ' == ', self.W[i])
                else:
                    print(self.Y[i], '!= ', self.W[i])
                    print("Error!")
                    return False
                print("Successful!")
                return True
        else:
            if self.Y == self.W:
                print(self.Y, ' == ', self.W)
            else:
                print(self.Y, '!= ', self.W)
                print("Error!")
                return False
            print("Successful!")
            return True


class signatureElGamal:

    def __init__(self, p, g, m):
        self.p = p
        self.g = g
        self.h = m
        self.x = lab1.generate_g(p - 2)
        self.y = lab1.fastModuloExponentiation(self.g, self.x, self.p)
        self.k = lab1.generate_g(p - 2)
        print(lab1.genEuclideanAlgo(self.k, p-1))
        self.r = 0
        if int.from_bytes(self.h, 'big') >= self.p:
            self.u = [0] * m.__len__()
            self.s = [0] * m.__len__()
            self.k_tmp = [0] * m.__len__()
        else:
            self.r = 0
            self.u = 0
            self.s = 0
            self.k_tmp = 0

    def encode(self):
        self.r = lab1.fastModuloExponentiation(self.g, self.k, self.p)
        print('r = ', self.r)
        if int.from_bytes(self.h, 'big') >= self.p:
            for i in range(0, self.h.__len__()):
                # print(2)
                self.u[i] = (self.h[i] - self.x*self.r) % (self.p - 1)
                self.k_tmp[i] = lab1.mulinv(self.k, self.p - 1)
                self.s[i] = self.k_tmp[i] * self.u[i] % (self.p - 1)
        else:
            self.u = (self.h - self.x * self.r) % (self.p - 1)
            self.k_tmp = lab1.mulinv(self.k, self.p - 1)
            self.s = self.k_tmp * self.u % (self.p - 1)

    def decode(self, r, s):
        left = 0
        right = 0
        if int.from_bytes(self.h, 'big') >= self.p:
            left = [0] * self.h.__len__()
            right = [0] * self.h.__len__()
            # print('r = ', r)
            # print('s = ', s)
            # print('p = ', self.p)
            for i in range(0, self.h.__len__()):
                left[i] = lab1.fastModuloExponentiation(self.y, r, self.p) * \
                       lab1.fastModuloExponentiation(r, s[i], self.p)
                right[i] = lab1.fastModuloExponentiation(self.g, self.h[i], self.p)
        else:
            left = lab1.fastModuloExponentiation(self.y, r, self.p) * lab1.fastModuloExponentiation(r, s, self.p)
            right = lab1.fastModuloExponentiation(self.g, self.h, self.p)
        return left, right

    def compare(self, left, right):
        print('left = ', left[0])
        print('right = ', right[0])
        if int.from_bytes(self.h, 'big') >= self.p:
            for i in range(0, self.h.__len__()):
                if left == right:
                    print(left[i], ' == ', right[i])
                else:
                    print(left[i], ' != ', right[i])
                    print("Error!")
                    return False
                print("Successful!")
                return True
        else:
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
        # Лень
        pass


if __name__ == "__main__":
    main()
