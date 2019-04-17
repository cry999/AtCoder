def traveling_plan(N: int, A: list) -> list:
    # 計算しやすいように最初と最後に原点を加えておく。
    A = [0] + A + [0]
    # 向き付き距離。d[i] = A[i+1] - A[i]
    d = [0] * (N + 1)
    # 総移動距離
    S = 0

    for i in range(0, N + 1):
        d[i] = A[i+1] - A[i]
        S += abs(d[i])

    def diff(a: int, b: int) -> int:
        return (a + b) - (max(a, b) - min(a, b))

    return [S - diff(abs(d[i]), abs(d[i + 1])) if d[i] * d[i + 1] < 0 else S
            for i in range(N)]


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = traveling_plan(N, A)
    for a in ans:
        print(a)
