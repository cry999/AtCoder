def digit(n: int)->int:
    '''n の桁数を計算します。
    '''
    if n == 0:
        return 1
    res = 0
    while n > 0:
        res += 1
        n //= 10
    return res


def roulette(N: int, M: list, A: list)->int:
    MOD = 10**9 + 7

    cM = 1
    dp = [0] * (N+1)
    for n in range(N):
        for m in range(M[n]):
            dp[n+1] += (dp[n] * (10 ** digit(A[n][m]))) % MOD
            dp[n+1] %= MOD
            dp[n+1] += (cM * A[n][m]) % MOD
            dp[n+1] %= MOD
        cM = (cM * M[n]) % MOD

    return dp[N]


if __name__ == "__main__":
    N = int(input())
    M = [0] * N
    A = [[] for _ in range(N)]
    for n in range(N):
        inp = [int(s) for s in input().split()]
        M[n] = inp[0]
        A[n] = inp[1:]

    ans = roulette(N, M, A)
    print(ans)
