def after_school(N: int, A: int, B: int, D: list)->int:
    # 計算しやすいように最後の次の日にデートすることにする
    sortedD = [0] + sorted(D) + [N+1]
    N = N+2
    date_num = B+2
    last_date = -1

    for next_anniversary in sortedD:
        if A < next_anniversary - last_date:
            # 最後にデートした日から次の記念日までの
            # 間隔が A 日以上開いているなら間に
            # (d - last_date) // A 回のデートが
            # 必要
            date_num += (next_anniversary-last_date-1) // A
        last_date = next_anniversary

    return N-date_num


if __name__ == "__main__":
    N, A, B = map(int, input().split())
    D = [int(s) for s in input().split()] if B > 0 else []

    ans = after_school(N, A, B, D)
    print(ans)
