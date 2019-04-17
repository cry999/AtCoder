from math import sqrt, ceil


def mul(iterable, mod: int = None)->int:
    ret = 1
    for v in iterable:
        ret *= v
        if mod:
            ret %= mod
    return ret


def factors_of_factorial(N: int)->int:
    prime_factors = {}

    for n in range(2, N+1):
        d = 2
        while n > 1:
            if n % d == 0:
                prime_factors.setdefault(d, 0)
            while n % d == 0:
                prime_factors[d] += 1
                n //= d
            d += 1
    return mul((p+1 for p in prime_factors.values()), mod=10**9+7)


if __name__ == "__main__":
    N = int(input())
    ans = factors_of_factorial(N)
    print(ans)
