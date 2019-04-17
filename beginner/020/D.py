import math


def prime_factors(n: int)->dict:
    if n < 2:
        return []

    pf = []
    d = 2
    while n > 1:
        if n % d == 0:
            pf.append(d)
        while n % d == 0:
            n //= d
        d += 1

    return pf


def all_divisors(n: int)->list:
    '''n の全ての約数を返します。
    '''
    res = []

    d = 1
    while d*d < n:
        if n % d == 0:
            res.append(d)
            res.append(n//d)
        d += 1

    if d * d == n:
        res.append(d)

    return res


def mul(iterable: list)->int:
    ret = 1
    for i in iterable:
        ret *= i
    return ret


def select_N(l: list, N: int)->list:
    '''l から N 個の要素を選ぶ組み合わせを全て列挙して
    返す。
    '''
    if N < 1:
        return []
    if N == 1:
        return [[a] for a in l]

    ret = []
    for i, a in enumerate(l):
        for r in select_N(l[i+1:], N-1):
            ret.append([a] + r)
    return ret


def sum_lcm_whose_gcd_is_1(N: int, K: int, mod: int)->int:
    '''1 <= i <= N をみたす全ての数字 i について
    GCD(i, K) == 1 となる LCM(i, K) の和を求める。
    '''
    # GCD(i, K) != 1 となるものの和を取り除いていく。具体的には、K の約
    # 数の倍数が i に該当する。
    # 1. まず約数のうち素数であるものの倍数を取り除く。
    # 2. 次に、素因数 2 つの合成数の倍数がダブっているので取り除かれているので
    # それらを加え直す。
    # 3. 以下同様に素因数の数が奇数個のものは取り除き、偶数個のものは加え直して
    # いく。
    # 具体的には、K = p^ap x q^aq x r^ar と表わせたとする。ただし、
    # p < q < r とする。
    # S = (1 + 2 + 3 + 4 + 5 + 6 + 7 + ... + N)
    # Sp = (p + 2p + ... + qp + ... + rp + ... + pqr + ...)
    # Sq = (q + 2q + ... + pq + ... + rq + ... + pqr + ...)
    # Sr = (r + 2r + ... + pr + ... + qr + ... + pqr + ...)
    # 1 の操作で S' = S - (Sp + Sq + Sr) を実行する。
    # この時、pq・pr・qr の倍数はそれぞれ 1 回ずつ多く引かれている。また
    # pqr の倍数は 2 回多く引かれている。
    # Spq = (pq + 2pq + ... + pqr + ...)
    # Sqr = (qr + 2qr + ... + pqr + ...)
    # Srp = (rp + 2rp + ... + pqr + ...)
    # 2 の操作で S'' = S' + (Spq + Sqr + Srp) を実行する。
    # 今度は、pq・pr・qr の倍数が 1 回ずつ足されることで 1 の操作での補填
    # が成功し、pqr の倍数が 3 回多く足されることで、1 の操作と合わせて 1 回
    # 多く加えられていることになる。
    # Spqr = (pqr + 2pqr + ...)
    # 3 の操作では S''' = S'' - Spqr を実行する。
    # これで pqr の倍数も正しく引かれたことになる。
    pf = prime_factors(K)

    S = 0
    for i in range(1 << len(pf)):
        m = 1     # 今回対象となる素数の合成数
        idx = 0   # 今回対象となる素数のインデックス
        sign = 1  # 合成数の素因数の個数が偶数個なら加算、奇数個なら減算
        while i != 0:
            if i & 1 != 0:
                m *= pf[idx]
                sign *= -1
            idx += 1
            i >>= 1
        n = N // m  # m の倍数の個数
        S += sign * m * (n * (n+1) // 2)
        S %= mod

    return (S * K) % mod


def lcm_rush(N: int, K: int)->int:
    MOD = 10**9 + 7

    ans = 0
    for d in all_divisors(K):
        ans += d * sum_lcm_whose_gcd_is_1(N//d, K//d, MOD)
        ans %= MOD

    return ans


if __name__ == "__main__":
    N, K = map(int, input().split())
    ans = lcm_rush(N, K)
    print(ans)
