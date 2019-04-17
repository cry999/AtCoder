def _abs(N: int, Z: int, W: int, A: list) -> int:
    if N == 1:
        return abs(A[0] - W)
    return max(abs(A[N-1] - A[N-2]), abs(A[N-1] - W))


if __name__ == "__main__":
    N, Z, W = map(int, input().split())
    A = [int(s) for s in input().split()]
    ans = _abs(N, Z, W, A)
    print(ans)
