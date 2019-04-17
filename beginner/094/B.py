def toll_gates(N: int, M: int, X: int, A: list) -> int:
    to0 = sum(1 for a in A if a < X)
    toN = sum(1 for a in A if a > X)
    return min(to0, toN)


if __name__ == "__main__":
    N, M, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = toll_gates(N, M, X, A)
    print(ans)
