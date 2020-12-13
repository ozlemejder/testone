def rem(a, b):
    while (a >= b):
        a = a - b
    else:
        return (a)


def quotient(b, a):
    i = 0
    while (b >= a):
        b = b - a
        i = i + 1
    else:
        return (i)


def is_prime(n):
    if (n in range(2)):
        return (False)
    i = 2
    while (i in range(2, n)):
        if rem(n, i) == 0:
            return (False)
        else:
            i = i + 1
    else:
        return (True)


def ordered_gcd(a, b):
    if (a <= b):
        r = 1
        while (r > 0):
            r = rem(b, a)
            if (r == 0):
                return (a)
                break
            b = a
            a = r
        else:
            return (r)


def gcd(a, b):
    if (a <= b):
        return (ordered_gcd(a, b))
    else:
        return (ordered_gcd(b, a))


n = 10














