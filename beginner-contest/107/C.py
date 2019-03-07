def candles(N: int, K: int, X: int)->int:
    min_d = float('inf')
    for i in range(N-K+1):
        xl, xr = X[i], X[i+K-1]
        min_d = min(min_d, abs(xl) + abs(xr - xl), abs(xr) + abs(xr - xl))

    return min_d


if __name__ == "__main__":
    N, K = map(int, input().split())
    X = [int(s) for s in input().split()]
    ans = candles(N, K, X)
    print(ans)
