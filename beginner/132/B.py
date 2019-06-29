def ordinary_number(N: int, p: list)->int:
    return sum(
        (p[i-1] < p[i] and p[i] < p[i+1]) or (p[i-1] > p[i] and p[i] > p[i+1])
        for i in range(1, N-1))


if __name__ == "__main__":
    N = int(input())
    P = [int(s) for s in input().split()]

    ans = ordinary_number(N, P)
    print(ans)
