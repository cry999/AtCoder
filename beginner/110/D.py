from math import sqrt


def prime_facts(n: int) -> dict:
    res = {}
    d = 2
    while d * d <= n:
        if n % d == 0:
            res[d] = 1
            n //= d

            while n % d == 0:
                res[d] += 1
                n //= d

        if d == 2:
            d += 1
        else:
            d += 2

    if n > 1:
        res[n] = 1

    return res


def factorization(N: int, M: int) -> int:
    """以下の説明において、F(N, M) はこの関数と同値。

    `a1 x a2 x ... x aN = M (式 1)`
    となる数列 {aN} の組み合わせ数を F(N, M) とする。

    まず、(式 1)より {aN} は全て M の約数であることは明らか。

    ここで、M の約数列を {dm} とする。今、aN = di とすると、
    `a1 x a2 x ... x a{N-1} = M // di`
    が成り立ち、これを満たす数列 {a{N-1}} の組み合わせ数は F(N-1, M//di) である。

    aN は任意の di を取れるので、結局、
    `F(N, M) = sigma{di} F(N-1, M//di) = sigma{di} F(N-1, M)` (式 2)
    が成り立つ。

    さらに、M を場合分けして考える。

    M = 1 のとき、(式 2)より
    `F(N, 1) = F(N-1, 1) = ... = F(1, 1) = 1` (式 3)
    が成り立つ。

    M = p (p は素数)のとき、(式 2)と(式 3)より、
    `F(N, p) = F(N-1, p) + F(N-1, 1) = F(N-1, p) + 1`
    が成り立つ。この漸化式をとけば、
    `F(N, p) = N`
    が成り立つ。

    M = p^k (p は素数)の時、めんどくさい計算の果てに
    `F(N, p^k) = PI{i=0}{k-1}(N+i) / k!`
    が成り立つ。

    M = p1...pk (pi は全て異なる素数)の時、めんどくさい計算の果てに
    `F(N,p1...pk) = N^k`

    M = p1^k1 ... pm^km (pi は全て異なる素数)の時、めんどくさい計算の果てに
    `F(N,p1^k1...pm^km) = F(N,p1^k1)...F(N,pm^km)`
    が成り立つ。
    """
    # pi と fact の初期化
    pi = [1] * 101
    fact = [1] * 101
    for i in range(1, 101):
        pi[i] = (N+i-1) * pi[i-1]
        fact[i] = i * fact[i-1]

    primes = prime_facts(M)
    ret = 1
    for k in primes.values():
        ret *= pi[k] // fact[k]

    return ret % 1000000007


if __name__ == "__main__":
    N, M = map(int, input().split())
    ans = factorization(N, M)
    print(ans)
