def winter(R: int, C: int, X: int, Y: int, D: int, L: int)->int:
    MOD = 10**9 + 7

    # (X x Y) の区画の作り方
    res = ((R-X+1) * (C-Y+1)) % MOD

    comb = [[0] * (X*Y+1) for i in range(X*Y + 1)]
    comb[0][0] = 1

    for n in range(X*Y):
        comb[n+1][0] = 1
        for r in range(n+1):
            comb[n + 1][r + 1] = (comb[n][r] + comb[n][r + 1]) % MOD

    def combi(n: int, r: int) -> int:
        if n < r:
            return 0
        return comb[n][r]

    if X*Y == D + L:
        # 何も考えず配置しても、上下左右の最大値のさがそれぞれ X, Y となるように
        # 取れる。
        res = (res * comb[X*Y][D]) % MOD
        res = (res * comb[X*Y-D][L]) % MOD
    else:
        # (X-i)*(Y-j) (0 <= i, 0 <= j and (i != 0 or j != 0)) に
        # おさまってしまう場合がある。それらの可能性を引く。

        stuff = D+L
        whole = combi(X*Y, stuff)
        ud_1 = combi(X*(Y-1), stuff)*2
        rl_1 = combi((X-1)*Y, stuff)*2
        ud_2 = combi(X*(Y-2), stuff)
        rl_2 = combi((X-2)*Y, stuff)
        ru_2 = combi((X-1)*(Y-1), stuff)*4
        ud_3 = combi((X-1)*(Y-2), stuff)*2
        rl_3 = combi((X-2)*(Y-1), stuff)*2
        rlud_4 = combi((X-2)*(Y-2), stuff) if X*Y != 1 else 0
        whole = whole-(ud_1+rl_1)+(ud_2+rl_2+ru_2)-(ud_3+rl_3)+rlud_4

        res = (res * whole * combi(stuff, D)) % MOD

    return res


if __name__ == "__main__":
    R, C = map(int, input().split())
    X, Y = map(int, input().split())
    D, L = map(int, input().split())

    ans = winter(R, C, X, Y, D, L)
    print(ans)
