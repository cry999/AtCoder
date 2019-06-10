def balance(N: int, W: list)->int:
    S = [0] * (N+1)  # W の累積和
    sumW = sum(W)  # W の総和

    for i, w in enumerate(W):
        S[i+1] = S[i] + w

    min_diff = float('inf')
    for i in range(1, N):
        S1 = S[i]
        S2 = sumW-S[i]

        min_diff = min(min_diff, abs(S1-S2))

    return min_diff


if __name__ == "__main__":
    N = int(input())
    W = [int(s) for s in input().split()]

    ans = balance(N, W)
    print(ans)
