import math


def ok(y: list, z: list, D: int)->bool:
    d = 0
    for i in range(D):
        d += (y[i]-z[i]) ** 2

    s = int(math.sqrt(d))

    return s * s == d


def good_distance(N: int, D: int, X: list)->int:
    count = 0

    for i in range(N):
        y = X[i]
        for j in range(i+1, N):
            z = X[j]

            count += ok(y, z, D)

    return count


if __name__ == "__main__":
    N, D = map(int, input().split())
    X = [[int(s) for s in input().split()] for _ in range(N)]
    ans = good_distance(N, D, X)

    print(ans)
