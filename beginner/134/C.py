def exception_handling(N: int, A: list)->list:
    sorted_A = sorted(A)
    return [sorted_A[-1] if a != sorted_A[-1] else sorted_A[-2] for a in A]


if __name__ == "__main__":
    N = int(input())
    A = [int(input()) for _ in range(N)]
    ans = exception_handling(N, A)
    for a in ans:
        print(a)
