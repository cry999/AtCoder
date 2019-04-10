import sys


def routes(H: int, W: int, A: list)->int:
    sys.setrecursionlimit(H*W+1)

    def in_range(h: int, w: int)->bool:
        return 0 <= h and h < H and 0 <= w and w < W

    memo = [[0] * W for _ in range(H)]
    # sortedA = sorted(
    #     (-A[h][w], h, w) for w in range(W) for h in range(H))

    def dfs(ch: int, cw: int)->int:
        if ch < 0 or H <= ch:
            return 0
        if cw < 0 or W <= cw:
            return 0

        if memo[ch][cw]:
            return memo[ch][cw]

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        memo[ch][cw] = 1 + sum(
            dfs(ch+dh, cw+dw)
            for dh, dw in dirs
            if in_range(ch+dh, cw+dw) and A[ch][cw] < A[ch+dh][cw+dw])
        return memo[ch][cw]

    # return sum(dfs(h, w) for _, h, w in sortedA)
    return sum(dfs(h, w) for w in range(W) for h in range(H))


if __name__ == "__main__":
    H = 0
    H, W = map(int, input().split())
    A = [[int(s) for s in input().split()] for _ in range(H)]
    ans = routes(H, W, A)
    print(ans)
