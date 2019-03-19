def hsi(N: int, M: int) -> float:
    return (100*(N-M) + 1900*M) * (1 << M)


if __name__ == "__main__":
    N, M = map(int, input().split())
    ans = hsi(N, M)
    print(ans)
