#!/usr/bin/python3
import math


#Villson Theorem
def isPrime(n):
    if (math.factorial(n - 1) + 1) % n != 0:
        return False
    else:
        return True

def check_gen(p):
    if p <= 2:
        return False
    tmp = p - 1
    q = tmp//2
    if tmp%2 != 0 or not(isPrime(q)):
        return False    
    g = p-2
    while fast_exponentiation(g,q,p) == 1:
        g -= 1
    if g <= 1:
        return False
    return g


def fast_exponentiation(base, x, mod):
    y = 1
    # base * d mod m = 1
    if x < 0:
        # search d
        base = ewklid(base,mod)[0]
        x = -x
    s = base
    while x:
        if x&1:
            y = y*s % mod
        s *= s % mod
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

def diffie_hellman(private_key, public_key, mod):
    if public_key < mod:
        return fast_exponentiation(public_key,private_key, mod)
    else:
        print('Public key greatest than mod!')

def gelfond_shanks():


def main():
    print('enter mod(prime number):')
    tmp = int(input())
    mod = 0
    if isPrime(tmp):
        mod = tmp * 2 + 1
    print('mod = ',mod)
    tmp = check_gen(mod)
    if tmp:
        base = tmp
    print('base = ',base)
    print('my_privat_key =')
    my_private_key = int(input())
    my_public_key = fast_exponentiation(base, my_private_key, mod)
    print('my_public_key = ',my_public_key)
    print('eva_privat_key =')
    eva_public_key = int((input()))
    print('pow = ', fast_exponentiation(base, my_private_key, mod))
    print('ewklid = ', ewklid(100500900,200400500))
    print('DiffieHellman = ', diffie_hellman(eva_public_key,my_private_key, mod))
    # print('x =')
    # x = int(input())
    # print('m =')
    # mod = int(input())
    # print(diffie_hellman(my_privat_key,public_key,mod))
    # print('pow')
    # print(fast_exponentiation(a,x,p))

if __name__ == "__main__":
    main()