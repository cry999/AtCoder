import math


def dist(a: tuple, b: tuple)->float:
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def cheating_investigation(
        s: tuple, t: tuple, T: int, V: int, n: int, girls: list)->bool:
    for girl in girls:
        if dist(s, girl) + dist(girl, t) <= T*V:
            return True
    return False


if __name__ == "__main__":
    txa, tya, txb, tyb, T, V = map(int, input().split())
    n = int(input())
    girls = [tuple(int(s) for s in input().split()) for _ in range(n)]

    yes = cheating_investigation((txa, tya), (txb, tyb), T, V, n, girls)
    print('YES' if yes else 'NO')
