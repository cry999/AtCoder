import math


def sub_vec(t: tuple, s: tuple) -> tuple:
    (tx, ty), (sx, sy) = t, s
    return (tx-sx, ty-sy)


def dot(v1: tuple, v2: tuple) -> float:
    (x1, y1), (x2, y2) = v1, v2
    return x1*x2 + y1*y2


def abs_vec(v: tuple) -> float:
    x, y = v
    return math.sqrt(x*x + y*y)


def direct_appeal(A: tuple, B: tuple, C: tuple) -> float:
    ab, ac = sub_vec(B, A), sub_vec(C, A)
    S = math.sqrt((abs_vec(ab) * abs_vec(ac)) ** 2 - (dot(ab, ac) ** 2)) / 2
    return S


if __name__ == "__main__":
    xa, ya, xb, yb, xc, yc = map(int, input().split())

    ans = direct_appeal((xa, ya), (xb, yb), (xc, yc))
    print(ans)
