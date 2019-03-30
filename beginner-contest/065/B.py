def trained(N: int, A: list)->int:
    lightning = 1
    for i in range(N):
        if lightning == 2:
            return i
        lightning = A[lightning-1]
    return -1


if __name__ == "__main__":
    N = int(input())
    A = [int(input()) for _ in range(N)]
    ans = trained(N, A)
    print(ans)
