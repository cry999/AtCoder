def programming_lecture(N: int, K: int, R: list)->float:
    R.sort()

    rate = 0
    for r in R[-K:]:
        rate = (r + rate)/2

    return rate


if __name__ == "__main__":
    N, K = map(int, input().split())
    R = [int(s) for s in input().split()]

    ans = programming_lecture(N, K, R)
    print(ans)
