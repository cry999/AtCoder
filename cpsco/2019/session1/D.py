def mod_pow(a: int, n: int, mod: int) -> int:
    res = 1
    while n > 0:
        if n & 1:
            res *= a
            res %= mod
        a *= a
        a %= mod

        n >>= 1

    return res


def dessert_planning(N: int) -> int:
    MOD = 10**9 + 7

    return (8 * mod_pow(5, N-1, MOD)) % MOD


if __name__ == "__main__":
    N = int(input())

    ans = dessert_planning(N)
    print(ans)
