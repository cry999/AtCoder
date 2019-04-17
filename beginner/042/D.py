def mod_inv(n: int, mod: int)->int:
    b, u, v = mod, 1, 0
    while b > 0:
        t = n // b

        n -= t * b
        u -= t * v

        n, b = b, n
        u, v = v, u

    return (u+mod) % mod


def comb(r: int, c: int, mod: int) -> int:
    if c < 0 or r < c:
        raise Exception('invalid r={}, c={}'.format(r, c))
    if c == 0 or c == r:
        return 1
    return (comb(r-1, c-1, mod) + comb(r-1, c, mod)) % mod


# n+1Cr = (n+1)*n!/((n+1-r)!r!) = ((n+1)/(n+1-r)) * (n!/((n-r)!r!))
def iroha_and_grid(H: int, W: int, A: int, B: int) -> int:
    MOD = 10 ** 9 + 7

    c1, c2 = 1, 1

    uH, uW = H - A, B - 1
    r = uH - 1
    for n in range(r, (uH - 1) + (uW - 1) + 1):
        c1 = (c1 * (n + 1) * mod_inv(n + 1 - r, MOD)) % MOD

    lH, lW = A, W - B
    r = lH - 1
    for n in range(r, (lH - 1) + (lW - 1) + 1):
        c2 = (c2 * (n + 1) * mod_inv(n + 1 - r, MOD)) % MOD

    ret = 0
    for w in range(B, W):
        # 上の領域の高さと幅
        uH, uW = H - A, w - 1
        n = (uH - 1) + (uW - 1) + 1
        r = uH - 1
        c1 = (c1 * (n + 1) * mod_inv(n + 1 - r, MOD)) % MOD

        # 下の領域の高さと幅
        lH, lW = A, W - w
        n = (lH - 1) + (lW - 1)
        r = lH - 1
        c2 = (c2 * (n + 1 - r) * mod_inv(n + 1, MOD)) % MOD

        ret = (ret + c1 * c2) % MOD

    return ret


if __name__ == "__main__":
    H, W, A, B = map(int, input().split())
    ans = iroha_and_grid(H, W, A, B)
    print(ans)
