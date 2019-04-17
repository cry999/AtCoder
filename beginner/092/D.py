def grid_components(A: int, B: int) -> list:
    K = 32
    grid = [
        ['#' if k < K else '.' for _ in range(2 * K)]
        for k in range(2 * K)]

    r, c = 0, 0
    for _ in range(A - 1):
        grid[r][c] = '.'

        c += 2
        if c >= 2 * K:
            r += 2
            c = 0

    r, c = 0, 0
    for _ in range(B - 1):
        grid[(2*K-1) - r][(2*K-1) - c] = '#'
        c += 2
        if c >= 2 * K:
            r += 2
            c = 0

    return grid


if __name__ == "__main__":
    A, B = map(int, input().split())
    ans = grid_components(A, B)
    h, w = len(ans), len(ans[0])
    print(h, w)
    for row in ans:
        print(''.join(row))
