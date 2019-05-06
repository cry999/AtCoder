import math


MOD = 10**9 + 7
SIZE = 50000
fact = [1] * (SIZE+1)
fact_inv = [1] * (SIZE+1)


def mod_inv(n: int, mod: int)->int:
    b, u, v = mod, 1, 0
    while b > 0:
        t = n // b

        n -= t * b
        u -= t * v

        n, b = b, n
        u, v = v, u

    return (u+mod) % mod


def init_comb():
    fact[0] = 1
    for n in range(SIZE):
        fact[n+1] = ((n+1) * fact[n]) % MOD

    fact_inv[SIZE] = mod_inv(fact[SIZE], MOD)
    for n in range(SIZE, 0, -1):
        fact_inv[n-1] = (n * fact_inv[n]) % MOD


def comb(n: int, r: int)->int:
    if n < 0 or r < 0 or n < r:
        raise Exception()

    res = (fact[n] * fact_inv[r]) % MOD
    res = (res * fact_inv[n-r]) % MOD
    # print('{}C{} = {}'.format(n, r, res))
    return res


def sqrt(n: int)->int:
    '''n の平方根を求める。ただし、n の平方根が整数とならない場合は
    -1 を返す。
    '''
    if n < 0:
        return -1
    sq = math.floor(math.sqrt(n))
    if sq * sq == n:
        return sq
    if (sq+1) * (sq+1) == n:
        return sq+1
    return -1


def calc(n: int, k: int)->int:
    '''ながさ n のバイナリ列において回文かつ転倒数 k の個数を計算します。
    '''
    # バイナリ列は前半部分(ながさ M)だけ考えればよく
    # ここに含まれる 1 の個数が x であるとする。この時、
    # 転倒数は以下のように計算される。
    # 1. N is even
    #     2x(M-x) = K
    #     => x = (M +- sqrt(M^2 - 2K)) / 2
    # 2. N is odd
    #     2-a. center is 0
    #         2x(M-x) + x = K
    #         => x = (2M+1 +- sqrt((2M+1)^2 - 8K)) / 4
    #     2-b. center is 1
    #         2x(M-x) + (M-x) = K
    #         => x = (2M-1 +- sqrt((2M-1)^2 - 8(K-M))) / 4
    # このように求めた x について組み合わせ (M, x) を求めれば良い。
    # ただし、x が整数になるようにチェックしながら計算する。
    # 整数にならない場合は該当するものなしとみなす。

    m = n//2

    if n & 1:  # n is odd
        ans = 0

        # center is 0
        sq1 = sqrt((2*m+1)**2 - 8*k)
        if sq1 >= 0:
            if (2*m + 1 + sq1) % 4 == 0:
                x11 = (2*m + 1 + sq1) // 4
                if 0 <= x11 and x11 <= m:
                    ans += comb(m, x11)

            if sq1 > 0 and (2*m + 1 - sq1) % 4 == 0:
                x12 = (2*m + 1 - sq1) // 4
                if 0 <= x12 and x12 <= m:
                    ans += comb(m, x12)

        # center is 1
        sq2 = sqrt((2*m-1)**2 - 8*(k-m))
        if sq2 >= 0:
            if (2*m - 1 + sq2) % 4 == 0:
                x21 = (2*m - 1 + sq2) // 4
                if 0 <= x21 and x21 <= m:
                    ans += comb(m, x21)

            if sq2 > 0 and (2*m - 1 - sq2) % 4 == 0:
                x22 = (2*m - 1 - sq2) // 4
                if 0 <= x22 and x22 <= m:
                    ans += comb(m, x22)

        return ans % MOD
    else:  # n is even
        sq = sqrt(m*m - 2*k)
        if sq < 0:
            return 0

        ans = 0
        if (m + sq) % 2 == 0:
            x = (m + sq) // 2
            if 0 <= x and x <= m:
                ans += comb(m, x)

        # sq が 0 の場合ものぞく。
        # sq == 0 の場合は上の if 分と重複してしまうため。
        if sq > 0 and (m-sq) % 2 == 0:
            x = (m - sq) // 2
            if 0 <= x and x <= m:
                ans += comb(m, x)

        return ans % MOD


def nucleotide(Q: int, queries: list)->list:
    return [calc(n, k) for n, k in queries]


if __name__ == "__main__":
    Q = int(input())
    queries = [tuple(int(s) for s in input().split()) for _ in range(Q)]

    init_comb()

    for ans in nucleotide(Q, queries):
        print(ans)
