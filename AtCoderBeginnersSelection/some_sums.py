def some_sums(N: int, A: int, B: int) -> int:
    ret = 0
    for n in range(1, N+1):
        s = sum([int(c) for c in str(n)])
        if A <= s and s <= B:
            ret += n

    return ret


if __name__ == "__main__":
    N, A, B = [int(s) for s in input().split()]
    ans = some_sums(N, A, B)
    print(ans)
