INF = 10**18
A = 0
B = 0
A, B, Q = [int(s) for s in input().split()]

s = [-INF] + [int(input()) for _ in range(A)] + [INF]
t = [-INF] + [int(input()) for _ in range(B)] + [INF]


def bisect_right(a, x):
    l, r = 0, len(a)
    while r - l > 1:
        m = (l + r) // 2
        if a[m] <= x:
            l = m
        else:
            r = m
    return r


for _ in range(Q):
    q = int(input())

    sr = bisect_right(s, q)

    tr = bisect_right(t, q)

    res = INF
    for _s in s[sr-1:sr+1]:
        for _t in t[tr-1:tr+1]:
            res = min(res, abs(q-_s) + abs(_t-_s), abs(q-_t)+abs(_t-_s))

    print(res)
