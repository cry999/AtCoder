def shot_king(N: int, balloons: list) -> int:
    Xmax = max(h + (N - 1) * s for h, s in balloons)

    def check(opt: int) -> bool:
        time_limits = [(opt - h) // s for h, s in balloons]
        time_limits.sort()

        return all(t >= i for i, t in enumerate(time_limits))

    l, r = 0, Xmax
    while r - l > 1:
        m = (r + l) // 2
        if check(m):
            r = m
        else:
            l = m
    return r


if __name__ == "__main__":
    N = int(input())
    balloons = [tuple(int(s) for s in input().split()) for _ in range(N)]

    ans = shot_king(N, balloons)
    print(ans)
