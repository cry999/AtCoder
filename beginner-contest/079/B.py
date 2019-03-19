def lucas_number(N: int) -> int:
    l0, l1 = 2, 1
    if N == 0:
        return l0
    if N == 1:
        return l1

    l = 0
    for _ in range(1, N):
        l = l1 + l0
        l1, l0 = l, l1
    return l


if __name__ == "__main__":
    N = int(input())
    ans = lucas_number(N)
    print(ans)
