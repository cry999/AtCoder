def atcolor(n: int, queries: list)->int:
    MAX = 10**6
    s = [0] * (MAX+2)

    for l, r in queries:
        s[l] += 1
        s[r+1] -= 1

    for i in range(MAX+1):
        s[i+1] += s[i]

    return max(s)


if __name__ == "__main__":
    n = int(input())
    queries = [tuple(int(s) for s in input().split()) for _ in range(n)]
    ans = atcolor(n, queries)
    print(ans)
