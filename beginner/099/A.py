def abd(N: int) -> str:
    return 'ABC' if N < 1000 else 'ABD'


if __name__ == "__main__":
    N = int(input())
    ans = abd(N)
    print(ans)
