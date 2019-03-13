def bitter_alchemy(N: int, X: int, M: list) -> int:
    return N + (X - sum(M))//min(M)


if __name__ == "__main__":
    N = 0
    N, X = map(int, input().split())
    M = [int(input()) for _ in range(N)]
    ans = bitter_alchemy(N, X, M)
    print(ans)
