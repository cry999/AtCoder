def palace(N: int, T: int, A: int, H: list) -> int:
    best_t = float('inf')
    best_i = 0

    for i, h in enumerate(H):
        t = T - 0.006*h
        if abs(A - best_t) > abs(A - t):
            best_t = t
            best_i = i

    return best_i + 1


if __name__ == "__main__":
    N = int(input())
    T, A = map(int, input().split())
    H = map(int, input().split())
    ans = palace(N, T, A, H)
    print(ans)
