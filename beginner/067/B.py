def snake_toy(N: int, K: int, l: list)->int:
    return sum(sorted(l)[-K:])


if __name__ == "__main__":
    N, K = map(int, input().split())
    l = [int(s) for s in input().split()]
    ans = snake_toy(N, K, l)
    print(ans)
