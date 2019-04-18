def ceil(a: int, b: int)->int:
    if (a//b) * b == a:
        return a // b
    return a // b + 1


def summary(N: int, A: list)->int:
    s, c = 0, 0
    for a in A:
        if a == 0:
            continue
        s += a
        c += 1
    return ceil(s, c)


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]

    ans = summary(N, A)
    print(ans)
