def next_month(N: int)->int:
    if N == 12:
        return 1
    return N + 1


if __name__ == "__main__":
    N = int(input())
    ans = next_month(N)
    print(ans)
