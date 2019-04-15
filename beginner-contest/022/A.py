def best_body(N: int, S: int, T: int, W: int, A: list) -> int:
    w = 0
    A = [W] + A
    best_body_days = 0
    for a in A:
        w += a
        if S <= w and w <= T:
            best_body_days += 1
    return best_body_days


if __name__ == "__main__":
    N = 0
    N, S, T = map(int, input().split())
    W = int(input())
    A = [int(input()) for _ in range(N-1)]

    ans = best_body(N, S, T, W, A)
    print(ans)
