__MATCH = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6, ]
__INF = float('inf')


def match_matching(N: int, M: int, A: list) -> int:
    # dp で最大桁数を求める
    dp = [-__INF] * (N+1)
    dp[0] = 0
    for i in range(1, N+1):
        dp[i] = max([-__INF] +
                    [dp[i - __MATCH[a]] for a in A if i >= __MATCH[a]]) + 1

    # 各桁の数字を決める
    _A = sorted(A, reverse=True)
    used_matches = 0
    ans = 0
    for n in range(dp[N], 0, -1):
        for a in _A:
            used_matches += __MATCH[a]
            if used_matches <= N and dp[N-used_matches] == n - 1:
                ans = ans * 10 + a
                break
            used_matches -= __MATCH[a]

    return ans


if __name__ == "__main__":
    N, M = [int(s) for s in input().split()]
    A = [int(s) for s in input().split()]

    ans = match_matching(N, M, A)

    print(ans)
