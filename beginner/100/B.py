def ringos_favorite_numbers(D: int, N: int) -> int:
    if N == 100:
        return (N + 1) * (100 ** D)
    return N * (100 ** D)


if __name__ == "__main__":
    D, N = map(int, input().split())
    ans = ringos_favorite_numbers(D, N)
    print(ans)
