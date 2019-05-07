
MOD = 10**9 + 7
MAX_N = 100000
MAX_M = 100000
COMB_SIZE = MAX_N + MAX_M

fact = [1] * (COMB_SIZE+1)
fact_inv = [1] * (COMB_SIZE+1)


def init_comb():
    global fact, fact_inv

    fact[0] = 1
    for n in range(COMB_SIZE):
        fact[n+1] = ((n+1) * fact[n]) % MOD

    fact_inv[COMB_SIZE] = mod_inv(fact[COMB_SIZE], MOD)
    for n in range(COMB_SIZE, 0, -1):
        fact_inv[n-1] = (n * fact_inv[n]) % MOD


def comb(n: int, r: int)->int:
    if n < 0 or r < 0 or n < r:
        return 0

    res = (fact[n] * fact_inv[r]) % MOD
    res = (res * fact_inv[n-r]) % MOD

    return res


def mod_inv(n: int, mod: int)->int:
    b, u, v = mod, 1, 0
    while b > 0:
        t = n // b

        n -= t * b
        u -= t * v

        n, b = b, n
        u, v = v, u

    return (u+mod) % mod


def continuous_call(N: int, M: int)->int:
    if N < 3:
        return 0

    # 余事象で考える。
    other_events = 0
    for k in range(1, min(N, M)+1):
        t = (comb(k, N-k) * comb(M-1, k-1)) % MOD
        other_events = (other_events + t) % MOD

    all_evnets = comb(N+M-2, N-1)

    return (all_evnets - other_events) % MOD


if __name__ == "__main__":
    N, M = map(int, input().split())

    init_comb()

    ans = continuous_call(N, M)
    print(ans)
