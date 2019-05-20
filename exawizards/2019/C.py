def snuke_the_wizard(N: int, Q: int, s: str, queries: list)->int:
    l, r = -1, N
    for t, d in reversed(queries):
        if d == 'R':
            if 0 <= r-1 and s[r-1] == t:
                r -= 1
            if 0 <= l and s[l] == t:
                l -= 1
        else:
            if l + 1 < N and s[l+1] == t:
                l += 1
            if r < N and s[r] == t:
                r += 1
    return r - l - 1 if l < r else 0


if __name__ == "__main__":
    Q = 0
    N, Q = map(int, input().split())
    s = input()
    queries = [tuple(input().split()) for _ in range(Q)]

    ans = snuke_the_wizard(N, Q, s, queries)
    print(ans)
