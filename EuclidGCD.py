def gcd(a, b):
    while True:
        if a == b:
            return a
        elif a > b:
            a = a % b
        elif a < b:
            b = b % a
        if a == 0:
            return b
        if b == 0:
            return a
