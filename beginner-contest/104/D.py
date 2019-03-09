def we_love_abc(S: str)->int:
    ABC = 'ABC'
    MOD = 1000000007

    dp = [0, 0, 0, 0]
    dp[3] = 1

    for c in reversed(S):
        for j in range(3):
            m1 = 3 if c == '?' else 1
            m2 = 1 if c == '?' or c == ABC[j] else 0
            dp[j] = (m1 * dp[j] + m2 * dp[j+1]) % MOD
        dp[3] = (3 if c == '?' else 1) * dp[3]
        dp[3] %= MOD

    return dp[0] % MOD


if __name__ == "__main__":
    S = input()
    ans = we_love_abc(S)
    print(ans)
