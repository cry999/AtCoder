import math


def dist(p1: tuple, p2: tuple) -> int:
    (x1, y1), (x2, y2) = p1, p2

    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def center_of_gravity(A: list, N: int) -> tuple:
    return sum(x for x, _ in A) / N, sum(y for _, y in A) / N


def farthest_point(A: list, p: tuple) -> tuple:
    max_dist = 0
    farthest = p
    for a in A:

        if max_dist < dist(p, a):
            max_dist = dist(p, a)
            farthest = a

    return farthest


def big_bang(N: int, A: list, B: list) -> float:
    cgA, cgB = center_of_gravity(A, N), center_of_gravity(B, N)
    fpA, fpB = farthest_point(A, cgA), farthest_point(B, cgB)

    return math.sqrt(dist(cgB, fpB) / dist(cgA, fpA))


if __name__ == "__main__":
    N = int(input())
    A = [tuple(int(s) for s in input().split()) for _ in range(N)]
    B = [tuple(int(s) for s in input().split()) for _ in range(N)]

    ans = big_bang(N, A, B)
    print(ans)
