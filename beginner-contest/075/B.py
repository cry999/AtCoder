def minesweeper(H: int, W: int, S: list)->list:
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]
    ret = [[''] * W for _ in range(H)]

    for h in range(H):
        for w in range(W):
            if S[h][w] == '#':
                ret[h][w] = '#'
                continue

            count = 0
            for dh, dw in directions:
                if h + dh < 0:
                    continue
                if H <= h + dh:
                    continue
                if w + dw < 0:
                    continue
                if W <= w + dw:
                    continue
                if S[h+dh][w+dw] == '#':
                    count += 1
            ret[h][w] = str(count)

    return ret


if __name__ == "__main__":
    H = 0
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = minesweeper(H, W, S)
    for a in ans:
        print(''.join(a))
