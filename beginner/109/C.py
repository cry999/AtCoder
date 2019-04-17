def gcd(a: int, b: int)->int:
    if a < b:
        a, b = b, a

    if b == 0:
        return a

    return gcd(b, a % b)


def skip(N: int, X: int, x: list)->int:
    sorted_x = sorted([X] + x)
    dists = [sorted_x[i+1] - sorted_x[i] for i in range(len(x))]
    before = 0
    for d in dists:
        before = gcd(before, d)
    return before


if __name__ == "__main__":
    N, X = map(int, input().split())
    x = [int(s) for s in input().split()]
    ans = skip(N, X, x)
    print(ans)
