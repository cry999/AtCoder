def bounding(N: int, X: int, L: list)->int:
    D = [0] * (N+1)
    for i, l in enumerate(L):
        D[i+1] = D[i] + l

    l, r = 0, N+1
    while r-l > 1:
        m = (l+r)//2
        if D[m] <= X:
            l = m
        else:
            r = m

    return r


if __name__ == "__main__":
    N, X = map(int, input().split())
    L = [int(s) for s in input().split()]

    ans = bounding(N, X, L)
    print(ans)
