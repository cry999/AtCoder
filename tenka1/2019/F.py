MOD = 998244353
MAX_K = 3000


def ceil(a: int, b: int)->int:
    '''a/b の切り上げを計算する。
    '''
    if (a // b) * b == a:
        return a//b
    return a//b + 1


# __fact[n] = n!
__fact = [0] * (MAX_K+1)
# __inv[n] = (n! の mod MOD に関する逆数)
__inv = [0] * (MAX_K+1)


def init_comb():
    # initialize __fact
    __fact[0] = 1
    __inv[0] = 1
    for n in range(MAX_K):
        __fact[n+1] = ((n+1) * __fact[n]) % MOD
        __inv[n+1] = mod_inv((n+1) * __fact[n], MOD)


def mod_inv(n: int, mod: int)->int:
    b, u, v = mod, 1, 0
    while b > 0:
        t = n // b

        n -= t * b
        u -= t * v

        n, b = b, n
        u, v = v, u

    return (u+mod) % mod


def comb(n: int, r: int)->int:
    '''nCr を計算する
    '''
    res = __fact[n]
    res = (res * __inv[n-r]) % MOD
    res = (res * __inv[r]) % MOD
    return res


def banned_x(N: int, X: int)->int:
    # 数列の全体の和を固定して調べる。
    # 数列の和の最大値は全て 2 でできている数列の 2*N
    res = 1  # 0 だけでできている分
    for S in range(1, 2*N+1):
        if S < X:
            # 1, 2 を合計で k 個利用するとする。
            # 1 を p 個、2 を q 個とすると
            # p+q=K; p+2q=S;
            # より
            # p=2K-S; q=S-K
            # となる。
            # このとき、0, 1, 2 の並べ方は
            # comb(N,p) * comb(N-p,q)
            # である。
            # また、0<=p; 0<=q より S/2<=k<=S が成り立つ。
            for k in range(ceil(S, 2), min(S, N)+1):
                p, q = 2*k - S, S-k
                res += comb(N, p) * comb(N-p, q)
                res %= MOD
        elif S == X:
            # nothing
            continue
        elif (S-X) & 1:
            # 2 を置かなければならない場所が [0, only2)
            # と (only2, N]
            only2 = (S-(X-1))//2

            # 1 が含まれない場合
            if 2*only2 >= X-1:
                if X & 1:
                    # 2 の置き方は N 個の位置から S//2 個
                    # 選ぶ組み合わせ。残りは 0 を置く
                    res += comb(N, S//2)
                    res %= MOD
            # 1 が含まれる場合
            else:
                # SS は 1,2 なんでも置いていいゾーンの幅
                SS = X-1-2*only2

                # k,p,q の変数の意味は S<X の時と同じ
                # ただし、2 は 2*only2 の領域にも置くので
                # 2 の個数は SS-k+2*only2 になり、
                # (N 個の位置から k+2*only2 個の位置を 1,2 用に確保)
                # x (k 個の位置から p 個の 1 を置く位置を確保)
                for k in range(ceil(SS, 2), min(N-2*only2, SS)+1):
                    p, q = 2*k-SS, SS-k
                    res += comb(N, k+2*only2) * comb(k, p)
                    res %= MOD
        # print('S={}, res={}'.format(S, res-tmp))

    return res


if __name__ == "__main__":
    N, X = map(int, input().split())

    init_comb()

    ans = banned_x(N, X)
    print(ans)
