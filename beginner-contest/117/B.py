def polygon(N: int, L: list) -> bool:
    max_l = max(L)
    return max_l < sum(L) - max_l


if __name__ == "__main__":
    N = int(input())
    L = [int(s) for s in input().split()]

    ans = polygon(N, L)
    print('Yes' if ans else 'No')
