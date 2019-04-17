def splitting_pile(N: int, A: list)->int:
    snuke, raccoon = A[0], sum(A[1:])

    min_diff = abs(snuke-raccoon)
    for a in A[1:-1]:
        snuke += a
        raccoon -= a
        min_diff = min(min_diff, abs(snuke-raccoon))

    return min_diff


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = splitting_pile(N, A)
    print(ans)
