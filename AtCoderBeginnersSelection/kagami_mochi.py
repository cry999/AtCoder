def kagami_mochi(N: int, D: list) -> int:
    _D = set(D)
    return len(_D)


if __name__ == "__main__":
    N = int(input())
    D = [int(input()) for _ in range(N)]
    ans = kagami_mochi(N, D)
    print(ans)
