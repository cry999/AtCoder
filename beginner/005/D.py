def make_delicious_takoyaki(N: int, D: list, Q: int, P: list)->list:
    S = [[0] * (N+1) for _ in range(N+1)]

    for r in range(N):
        for c in range(N):
            S[r+1][c+1] = D[r][c] + S[r][c+1]

    for c in range(N):
        for r in range(N):
            S[r+1][c+1] += S[r+1][c]

    # (r1, c1), (r2, c2) を左上と右下にもつ長方形の累積和を計算する
    def cum(r1: int, c1: int, r2: int, c2: int)->int:
        return S[r2][c2] - S[r1][c2] - S[r2][c1] + S[r1][c1]

    # for r in range(N):
    #     for c in range(N):
    #         print('r={}, c={}, cum={}'.format(r, c, cum(r, c, r+1, c+1)))

    # dp[n] = 面積 n の長方形の累積和の最大値
    dp = [0] * (N*N + 1)

    for r1 in range(N):
        for c1 in range(N):
            for r2 in range(r1, N):
                for c2 in range(c1, N):
                    area = (r2-r1+1)*(c2-c1+1)
                    dp[area] = max(dp[area], cum(r2+1, c2+1, r1, c1))

    # dp[n] = 面積 n 以下の長方形の累積和の最大値
    # に変更
    for i in range(N*N):
        dp[i+1] = max(dp[i+1], dp[i])

    return [dp[p] for p in P]


if __name__ == "__main__":
    N = int(input())
    D = [[int(s) for s in input().split()] for _ in range(N)]
    Q = int(input())
    P = [int(input()) for _ in range(Q)]

    ans = make_delicious_takoyaki(N, D, Q, P)
    for a in ans:
        print(a)
