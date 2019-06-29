def divide_the_problems(N: int, D: list)->int:
    D.sort()
    return D[N//2]-D[N//2-1]


if __name__ == "__main__":
    N = int(input())
    D = [int(s) for s in input().split()]

    ans = divide_the_problems(N, D)
    print(ans)
