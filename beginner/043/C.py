def be_together(N: int, A: list) -> int:
    ave = sum(A) // N

    def f(y: int) -> int:
        return sum((a-y)**2 for a in A)

    return min(f(ave), f(ave + 1))


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = be_together(N, A)
    print(ans)
