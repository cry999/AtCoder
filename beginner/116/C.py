def grand_garden(N: int, H: list) -> int:
    before = 0
    op = 0
    for h in H:
        if before < h:
            op += h - before
        before = h

    return op


if __name__ == "__main__":
    N = int(input())
    H = [int(s) for s in input().split()]

    ans = grand_garden(N, H)
    print(ans)
