def prime_fact(n: int)->list:
    '''n の素因数を返す
    '''
    if n < 2:
        return []

    d = 2
    res = []
    while n > 1 and d * d <= n:
        if n % d == 0:
            res.append(d)
        while n % d == 0:
            n //= d
        d += 1

    if n > 1:
        # n が素数
        res.append(n)

    return res


def gen_primes(n: int)->int:
    '''n まで(n 含む)の素数を返します。
    '''
    if n < 2:
        return []
    primes = [2]

    if n < 3:
        return primes
    primes.append(3)

    def is_prime(n: int)->bool:
        for p in primes:
            if n % p == 0:
                return False
        return True

    # 2,3 以降の素数は 6k+1 あるいは 6k-1
    # の形をしていることを利用して列挙する。
    for k in range((N+1)//6):
        k += 1

        if is_prime(6*k-1):
            primes.append(6*k-1)

        if is_prime(6*k+1):
            primes.append(6*k+1)

    return primes


def gcd(a: int, b: int)->int:
    if a < b:
        a, b = b, a
    return a if b == 0 else gcd(b, a % b)


def gcd_list(A: list)->int:
    if len(A) == 0:
        return 0
    if len(A) == 1:
        return A[0]

    g = abs(A[0])
    for a in A[1:]:
        g = gcd(g, abs(a))
    return g


def polynominal_divisors(N: int, A: list)->list:
    # primes = prime_fact(abs(A[-1]))
    A.reverse()
    # 候補となる素数は、N 以下の素数あるいは、aN の素因数

    def check(p: int)->bool:
        '''素数 p が任意の整数 x について f(x) を割り切れるかを
        check する。具体的には、

        - a0
        - a1 + ap + a{2p-1} + ...
        - a2 + a{p+1} + a{2p} + ...
        ...
        - a{p-1} + a{2p-2} + ...
        という項が p で割り切れるかを検査する。
        '''
        if A[0] % p != 0:
            return False

        for i in range(1, min(N, p)):
            # ai + a{i+p-1} + ... を求めて
            # p で割り切れるか検査する。
            # print('p={}'.format(p))
            b = 0
            while i <= N:
                # print('i={}'.format(i))
                b = (b + A[i]) % p
                i += p-1
            if b != 0:
                return False
        return True

    primes = set(gen_primes(N) + prime_fact(gcd_list(A)))
    res = [p for p in primes if check(p)]
    res.sort()

    return res


if __name__ == "__main__":
    N = int(input())
    A = [int(input()) for _ in range(N+1)]

    ans = polynominal_divisors(N, A)
    for a in ans:
        print(a)
