def fact_mod(n: int, mod: int)->int:
    ret = 1
    while n > 0:
        ret = (ret * n) % mod
        n -= 1
    return ret


def reconciled(N: int, M: int)->int:
    MOD = 10**9 + 7
    if abs(N - M) > 1:
        return 0
    if abs(N - M) == 1:
        return (fact_mod(N, MOD) * fact_mod(M, MOD)) % MOD

    return (2 * fact_mod(N, MOD) * fact_mod(M, MOD)) % MOD


if __name__ == "__main__":
    N, M = map(int, input().split())
    ans = reconciled(N, M)
    print(ans)
