def upper_square(A: int, B: int) -> int:
    """C**2 < A*B を満たす最大の C を求めます。
    """
    l, r = min(A, B), max(A, B)
    while r - l > 1:
        m = (l + r) // 2
        if m * m < A * B:
            l = m
        else:
            r = m
    return l


def query(A: int, B: int) -> int:
    A, B = min(A, B), max(A, B)
    if A == B:
        # (1, 2A-1), ..., (A-1, A+1), (A+1, A-1), ..., (2A-1, 1)
        # が最大。
        return 2 * A - 2
    if B == A + 1:
        # (1, 2A), ..., (A-1, A+2), (A+2, A-1), ..., (2A, 1)
        # が最大。
        return 2 * A - 2

    # C = A
    # while (C + 1) ** 2 < A * B:
    #     C += 1
    C = upper_square(A, B)

    if A * B <= C * (C + 1):
        # (1, A+B−1), ..., (A−1, B+1), (A+1, 2C−A−1), ..., (C, C), ..., (2C−1, 1)
        # が最大。
        return 2 * C - 2

    # (1, A+B−1), ..., (A−1, B+1), (A+1, 2C−A), ..., (C, C+1), (C+1, C), ...,(2C, 1)
    # が最大。
    return 2*C - 1


def worst_case(Q: int, queries: list) -> list:
    return [query(A, B) for A, B in queries]


if __name__ == "__main__":
    Q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]
    ans = worst_case(Q, queries)
    for a in ans:
        print(a)
