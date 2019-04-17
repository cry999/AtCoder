def parking(N: int, A: int, B: int) -> int:
    return min(N * A, B)


if __name__ == "__main__":
    N, A, B = map(int, input().split())
    ans = parking(N, A, B)
    print(ans)
