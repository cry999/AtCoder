def maximum_difference(N: int, A: list)->int:
    return max(A) - min(A)


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = maximum_difference(N, A)
    print(ans)
