from math import atan2, pi
from bisect import bisect_left


def triangle(N: int, points: list)->tuple:
    acute, right, obtuse = 0, 0, 0

    right_m = pi / 2 - 1e-9  # マイナスよりの直角
    right_p = pi / 2 + 1e-9  # プラスよりの直角
    PI2 = pi * 2

    for i, (x0, y0) in enumerate(points):
        angles = [atan2(y-y0, x-x0) for x, y in (points[:i] + points[i+1:])]
        angles.sort()

        # 一番大きい鋭角。
        s = bisect_left(angles, angles[0] + right_m)
        # 一番大きい鈍角。
        t = bisect_left(angles, angles[0] + pi)
        # 半周分を 2π 増やして追加する
        angles += [x + PI2 for x in angles[:t] + [10]]

        for i in range(N-1):
            r = angles[i]
            # s を一番小さい鈍角まで動かす。
            while angles[s] < r + right_m:
                s += 1
            # 誤差込みの直角
            while angles[s] <= r + right_p:
                s += 1
                right += 1
            # t を一番大きい鈍角まで動かす。
            while angles[t] < r + pi:
                t += 1
            obtuse += t - s

    acute = N*(N-1)*(N-2)//6 - (right+obtuse)

    return acute, right, obtuse


if __name__ == "__main__":
    N = int(input())
    points = [tuple(int(s) for s in input().split()) for _ in range(N)]
    acute, right, obtuse = triangle(N, points)
    print(acute, right, obtuse)
