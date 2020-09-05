#!/usr/bin/python3


def fast_exponentiation(a, x, p):
    s = a
    y = 1
    while x:
        if x&1:
            y = y*s % p
        s *= s % p
        x >>= 1
    return y

def ewklid(a,b):
    if a < 0 or b < 0 or a < b:
        return 'Incorrect data'
    x, x1, y, y1 = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, x1 = x1, x - x1*q
        y, y1 = y1, y - y1*q
    return (x, y, a)

def diffi_hellman():
    # in progress

def genfold_shnex():
    # in progress

def main():
    print('for ewklid')
    print('a =')
    a = int(input())
    print('b =')
    b = int(input())
    print('| x | y | ewklid |')
    print(ewklid(a, b))
    print('for POW')
    print('a =')
    a = int(input())
    print('x =')
    x = int(input())
    print('p =')
    p = int(input())
    print('pow')
    print(fast_exponentiation(a,x,p))
if __name__ == "__main__":
    main()