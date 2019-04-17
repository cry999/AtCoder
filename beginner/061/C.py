def big_array(N: int, K: int, queries: list)->int:
    d = {}
    for a, b in queries:
        d.setdefault(a, 0)
        d[a] += b

    count = 0
    ans = 0
    for k, v in sorted(d.items()):
        count += v
        if K <= count:
            ans = k
            break
    return ans


if __name__ == "__main__":
    N = 0
    N, K = map(int, input().split())
    queries = [tuple(map(int, input().split())) for _ in range(N)]
    ans = big_array(N, K, queries)
    print(ans)
