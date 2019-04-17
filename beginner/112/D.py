import math


def divisors(n: int) -> list:
    s = int(math.sqrt(n))
    ret = []
    if s * s == n:
        ret.append(s)
    else:
        s += 1

    for i in range(1, s):
        if n % i == 0:
            ret.append(i)
            ret.append(n // i)

    return sorted(ret, reverse=True)


def partition(N: int, M: int) -> int:
    for gcd in divisors(M):
        if gcd * N > M:
            continue
        return gcd
    return -1


if __name__ == "__main__":
    N, M = map(int, input().split())
    ans = partition(N, M)
    print(ans)
