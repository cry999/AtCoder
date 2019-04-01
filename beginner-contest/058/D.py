def mul_mod(mod: int, *args)->int:
    ret = 1
    for a in args:
        ret = (ret * a) % mod
    return ret


def rectangles(n: int, m: int, X: list, Y: list)->int:
    MOD = 10**9 + 7

    DX = []
    x0 = X[0]
    for x in X[1:]:
        DX.append((x-x0) % MOD)
        x0 = x

    DY = []
    y0 = Y[0]
    for y in Y[1:]:
        DY.append((y-y0) % MOD)
        y0 = y

    dx_sum = sum(mul_mod(MOD, i+1, n-1-i, dx) for i, dx in enumerate(DX))
    dy_sum = sum(mul_mod(MOD, i+1, m-1-i, dy) for i, dy in enumerate(DY))

    return (dx_sum * dy_sum) % MOD


if __name__ == "__main__":
    n, m = map(int, input().split())
    X = [int(s) for s in input().split()]
    Y = [int(s) for s in input().split()]
    ans = rectangles(n, m, X, Y)
    print(ans)
