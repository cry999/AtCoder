def traveling_atcodeer_problem(N: int, A: list)->int:
    return max(A) - min(A)


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = traveling_atcodeer_problem(N, A)
    print(ans)
