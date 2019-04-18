def do_cross(l1: tuple, l2: tuple) -> bool:
    (ax, ay), (bx, by) = l1
    (cx, cy), (dx, dy) = l2

    ta = (cx - dx) * (ay - cy) + (cy - dy) * (cx - ax)
    tb = (cx - dx) * (by - cy) + (cy - dy) * (cx - bx)
    tc = (ax - bx) * (cy - ay) + (ay - by) * (ax - cx)
    td = (ax - bx) * (dy - ay) + (ay - by) * (ax - dx)

    return tc * td < 0 and ta * tb < 0


def cut_in_two(line: tuple, N: int, poligon: list) -> int:
    cross_points = 0
    for i in range(N):
        l = (poligon[i-1], poligon[i])

        if do_cross(l, line):
            cross_points += 1

    return 1 + cross_points//2


if __name__ == "__main__":
    Ax, Ay, Bx, By = map(int, input().split())
    N = int(input())
    poligon = [tuple(int(s) for s in input().split()) for _ in range(N)]
    ans = cut_in_two(((Ax, Ay), (Bx, By)), N, poligon)
    print(ans)
