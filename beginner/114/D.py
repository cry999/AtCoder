def prime_fact(n: int) -> dict:
    ret = {}
    div = 2
    while n >= div:
        if n % div == 0:
            n //= div
            ret[div] = 1
        while n % div == 0:
            n //= div
            ret[div] += 1
        if div == 2:
            div += 1
        else:
            div += 2
    return ret


def fact(n: int) -> int:
    if n < 0:
        return -1
    if n == 0:
        return 1
    return n*fact(n-1)


def q756(N: int) -> int:
    f = fact(N)
    p = prime_fact(f)

    # それぞれ 74, 24, 14, 4, 2, 個以上の因数の数
    c74, c24, c14, c4, c2 = 0, 0, 0, 0, 0
    for v in p.values():
        if v >= 74:
            c74 += 1
        if v >= 24:
            c24 += 1
        if v >= 14:
            c14 += 1
        if v >= 4:
            c4 += 1
        if v >= 2:
            c2 += 1

    ret = c74
    if c2 > 1:
        ret += c24 * (c2-1)
    if c4 > 1:
        ret += c14 * (c4-1)
    if c2 > 2 and c4 > 1:
        ret += ((c4 * (c4-1)) // 2) * (c2-2)

    return ret


if __name__ == "__main__":
    N = int(input())
    ans = q756(N)
    print(ans)
