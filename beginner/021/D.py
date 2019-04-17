def mod_inv(n: int, mod: int)->int:
    b, u, v = mod, 1, 0
    while b > 0:
        t = n // b

        n -= t * b
        u -= t * v

        n, b = b, n
        u, v = v, u

    return (u+mod) % mod


def multi_loop(n: int, k: int) -> int:
    MOD = 10**9 + 7

    # {(n-1) + (k-1)}_C_{k-1} を求める。
    # {n+1}C{r+1} = (n+1)!/((n-r)!(r+1)!)
    #             = (n+1)/(r+1) x nCr
    # より
    # {n+a}C{a} = (n+a)/a x {n+a-1}C{a-1}
    #           = ...
    #           = (n+a)/a x (n+a-1)/(a-1) x ... x (n+1)/1 x nC0
    c = 1
    for i in range(k):
        c = (c * (n + i)) % MOD
        c = (c * mod_inv(i + 1, MOD)) % MOD

    return c


if __name__ == "__main__":
    n = int(input())
    k = int(input())

    ans = multi_loop(n, k)
    print(ans)
