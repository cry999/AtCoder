def together(N: int, A: list)->int:
    d = {}
    for a in A:
        d.setdefault(a, 0)
        d[a] += 1

        d.setdefault(a+1, 0)
        d[a+1] += 1

        d.setdefault(a-1, 0)
        d[a-1] += 1

    return max(d.values())


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = together(N, A)
    print(ans)
