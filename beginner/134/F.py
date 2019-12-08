def permutation_oddness(n: int, k: int)->int:
    MOD = 10**9 + 7
    MAX_K = n*n//2

    if k > MAX_K or k % 2 == 1:
        return 0

    dp = [[[0] * (MAX_K+1) for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(n+1):
            for odd in range(0, MAX_K+1, 2):
                if odd < 2*j:
                    continue

                dp[i+1][j][odd] = (2*j+1) * dp[i][j][odd-2*j] % MOD
                if j+1 <= n:
                    dp[i+1][j][odd] += (j+1)*(j+1)*dp[i][j+1][odd-2*j] % MOD
                if j-1 >= 0:
                    dp[i+1][j][odd] += dp[i][j-1][odd-2*j] % MOD
                dp[i+1][j][odd] %= MOD

    return dp[n][0][k]


if __name__ == "__main__":
    n, k = map(int, input().split())
    ans = permutation_oddness(n, k)
    print(ans)
