def count_diamond(R: int, C: int, K: int, S: list) -> int:
    ok = [[True] * C for _ in range(R)]

    for row in range(R):
        for col in range(C):
            if S[row][col] == 'o':
                continue

            u, d = max(0, row-K+1), min(R-1, row+K-1)
            for rr in range(u, d+1):
                l = max(0, col-K+abs(row-rr) + 1)
                r = min(C-1, col+K-abs(row-rr)-1)
                for cc in range(l, r+1):
                    ok[rr][cc] = False

    return sum(
        ok[r][c]
        for r in range(K-1, R-K+1)
        for c in range(K-1, C-K+1))


if __name__ == "__main__":
    R = 0
    R, C, K = map(int, input().split())
    S = [input() for _ in range(R)]
    ans = count_diamond(R, C, K, S)
    print(ans)
