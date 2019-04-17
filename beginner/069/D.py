def grid_coloring(H: int, W: int, N: int, A: list)->list:
    h, w = 0, 0
    dw = 1
    ret = [[''] * W for _ in range(H)]
    for i, a in enumerate(A):
        for _ in range(a):
            ret[h][w] = str(i+1)
            if w + dw == W:
                h += 1
                dw = -1
            elif w + dw == -1:
                h += 1
                dw = 1
            else:
                w += dw
    return ret


if __name__ == "__main__":
    H, W = map(int, input().split())
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = grid_coloring(H, W, N, A)
    print('\n'.join(map(' '.join, ans)))
