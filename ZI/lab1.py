#!/usr/bin/python3
import math


#Villson Theorem
def isPrime(n):
    if (math.factorial(n - 1) + 1) % n != 0:
        return False
    else:
        return True

def fast_exponentiation(a, x, m):
    y = 1
    # a * d mod m = 1
    if x < 0:
        # search d
        a = ewklid(a,m)[0]
        x = -x
    s = a
    while x:
        if x&1:
            y = y*s % m
        s *= s % m
        x >>= 1
    return y

def ewklid(a,b):
    if a < 0 or b < 0:
        return 'Incorrect data'
    if a == 0:
        x = 0
        y = 1
        return b, 0, 1
    x, x1, y, y1 = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, x1 = x1, x - x1*q
        y, y1 = y1, y - y1*q
    return x, y, a

def diffie_hellman(base, privat_key, public_key, mod):
    if isPrime(base) and isPrime(mod):
        return fast_exponentiation(base, privat_key*public_key, mod)
    else:
        print('base or mod is not prime')

# def gelfond_shenx():


def main():
    # print('for ewklid')
    # print('a =')
    # a = int(input())
    # print('b =')
    # b = int(input())
    # print('| x | y | ewklid |')
    # print(ewklid(a, b))
    # print('for POW')
    print('base =')
    base = int(input())
    print('privat_key =')
    privat_key = int(input())
    print('public_key =')
    public_key = int(input())
    # print('x =')
    # x = int(input())
    print('m =')
    mod = int(input())
    print(diffie_hellman(base,privat_key,public_key,mod))
    # print('pow')
    # print(fast_exponentiation(a,x,p))

if __name__ == "__main__":
    main()