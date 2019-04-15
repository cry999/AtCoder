def addition(N: int) -> int:
    MAX_POW = 3
    res = []

    for p in range(MAX_POW, -1, -1):
        if N >= (1 << p):
            N -= 1 << p
            res.append(1 << p)

    return res


if __name__ == "__main__":
    N = int(input())

    ans = addition(N)
    print(len(ans))
    for a in ans:
        print(a)
