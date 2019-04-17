def make_a_rectangle(N: int, A: list)->int:
    d = {}
    for a in A:
        d.setdefault(a, 0)
        d[a] += 1

    max1, max2 = 0, 0
    for v, p in sorted([(k, v) for k, v in d.items() if v > 1], key=lambda x: -x[0]):
        if max1 == 0:
            max1 = v
            if p >= 4:
                max2 = v
                break
        else:
            max2 = v
            break

    return max1 * max2


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = make_a_rectangle(N, A)
    print(ans)
