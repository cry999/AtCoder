def theater(N: int, queries: list)->int:
    return sum(r - l + 1 for l, r in queries)


if __name__ == "__main__":
    N = int(input())
    queries = [tuple(int(s) for s in input().split()) for _ in range(N)]
    ans = theater(N, queries)
    print(ans)
