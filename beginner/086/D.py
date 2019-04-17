def points(cx: int, cy: int, K: int)->list:
    # 中心
    ps = [(max(0, cx-K), max(0, cy-K), cx, cy)]

    # 右上
    x2, y2 = min(2*K, cx+K), min(2*K, cy+K)
    x1, y1 = cx, cy
    ps.append((x1, y1, x2, y2))

    if K < cy:
        # 右下
        x2, y2 = min(2*K, cx+K), cy - K
        x1, y1 = cx, max(0, y2-K)
        ps.append((x1, y1, x2, y2))

    if cx < K:
        # 右
        x2, y2 = min(2*K, cx+2*K), cy
        x1, y1 = cx + K, max(0, cy-K)
        ps.append((x1, y1, x2, y2))

    if K < cx:
        # 左上
        x2, y2 = cx - K, min(2*K, cy+K)
        x1, y1 = max(0, x2-K), cy
        ps.append((x1, y1, x2, y2))

    if K < cx and K < cy:
        # 左下
        x2, y2 = cx - K, cy - K
        x1, y1 = max(0, x2-K), max(0, y2-K)
        ps.append((x1, y1, x2, y2))

    return ps


def checker(N: int, K: int, XYC: list)->int:
    white = [[0] * (2*K + 1) for _ in range(2*K + 1)]
    for x, y, c in XYC:
        if c == 'B':
            x = x + K
        tx, ty = (x % (2*K)) + 1, (y % (2*K)) + 1
        white[tx][ty] += 1

    for ky in range(2*K):
        for kx in range(2*K):
            white[ky+1][kx+1] += white[ky+1][kx]

    for ky in range(2*K):
        for kx in range(2*K):
            white[ky+1][kx+1] += white[ky][kx+1]

    def get(x1: int, y1: int, x2: int, y2: int)->int:
        return white[y2][x2] - white[y2][x1] - white[y1][x2] + white[y1][x1]

    max_count = 0
    for ky in range(K, 2*K):
        for kx in range(2*K):
            count = sum(get(x1, y1, x2, y2)
                        for x1, y1, x2, y2 in points(kx, ky, K))
            max_count = max(max_count, count)
            if max_count == N:
                break
    return max_count


if __name__ == "__main__":
    N = 0
    N, K = map(int, input().split())
    XYC = []
    for _ in range(N):
        x, y, c = input().split()
        XYC.append((int(x), int(y), c))
    ans = checker(N, K, XYC)
    print(ans)
