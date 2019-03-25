def around_square(N: int) -> int:
    n = 1
    while (n+1)*(n+1) <= N:
        n += 1
    return n * n


if __name__ == "__main__":
    N = int(input())
    ans = around_square(N)
    print(ans)
