def weather_report(N: int, rainy: list) -> list:
    rainy.sort()

    start, end = 0, 0
    res = []
    for s, e in rainy:
        s -= s % 5
        e += 0 if e % 5 == 0 else(5 - e % 5)
        if e % 100 == 60:
            # 時間の繰り上がりができてしまったとき。
            e = e - 60 + 100

        if s <= end:
            # 連続している
            end = max(e, end)
        else:
            # 途切れている。
            if start == 0 and end == 0:
                # 初期状態はスキップ
                # continue
                pass
            else:
                res.append((start, end))
            start, end = s, e
    else:
        res.append((start, end))

    return res


if __name__ == "__main__":
    N = int(input())
    rainy = [tuple(int(s) for s in input().split('-')) for _ in range(N)]

    ans = weather_report(N, rainy)
    for s, e in ans:
        print('{:04}-{:04}'.format(s, e))
