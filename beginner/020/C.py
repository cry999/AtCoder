

def can_goal(
        x: int, start: tuple, goal: tuple,
        H: int, W: int, T: int, S: list)->bool:
    dirs = [(0, 1), (1, 0), (0, -1),  (-1, 0)]

    sh, sw = start
    gh, gw = goal

    d = [[float('inf')] * W for _ in range(H)]
    d[sh][sw] = 0

    update = True
    while update:
        update = False
        for h in range(H):
            for w in range(W):
                cost = 1 if S[h][w] != '#' else x
                for dh, dw in dirs:
                    if h + dh < 0 or H <= h + dh:
                        continue
                    if w + dw < 0 or W <= w + dw:
                        continue
                    if d[h][w] > d[h+dh][w+dw] + cost:
                        update = True
                        d[h][w] = d[h+dh][w+dw] + cost
    return d[gh][gw] <= T


def through_wall(H: int, W: int, T: int, S: list)->int:
    MAX_T = 10**9

    s, g = None, None
    for h in range(H):
        for w in range(W):
            if S[h][w] == 'S':
                s = (h, w)
            if S[h][w] == 'G':
                g = (h, w)

    l, r = -1, MAX_T * 100 + 1
    while r - l > 1:
        m = (r + l) // 2

        if can_goal(m, s, g, H, W, T, S):
            l = m
        else:
            r = m
    return l


if __name__ == "__main__":
    H = 0
    H, W, T = map(int, input().split())
    S = [input() for _ in range(H)]

    ans = through_wall(H, W, T, S)
    print(ans)
