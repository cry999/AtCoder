def static_sushi(N: int, C: int, XV: list) -> int:
    Sv = [0] * (N+1)
    fr, fl = [0] * (N+1), [0] * (N+1)
    gr, gl = [0] * (N+1), [0] * (N+1)
    for i, (x, v) in enumerate(XV):
        Sv[i+1] = Sv[i] + v

        fl[i+1] = Sv[i+1] - x
        gl[i+1] = max(gl[i], fl[i+1])

        fr[i+1] = Sv[i+1] - 2*x
        gr[i+1] = max(gr[i], fr[i+1])

    max_cal = 0
    for ib, (xb, _) in enumerate(XV+[(C,0)]):
        cal_a1, cal_a2 = gr[ib], gl[ib]
        cal_b1, cal_b2 = Sv[N] - Sv[ib] - (C-xb), Sv[N] - Sv[ib] - 2*(C-xb)
        cal1, cal2 = cal_a1 + cal_b1, cal_a2 + cal_b2
        max_cal = max(max_cal, cal1, cal2)

    return max_cal


if __name__ == "__main__":
    N = 0
    N, C = map(int, input().split())
    XV = [tuple(map(int, input().split())) for _ in range(N)]
    ans = static_sushi(N, C, XV)
    print(ans)
