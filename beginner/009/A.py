def moving(N: int)->int:
    return N//2 + (N % 2)


if __name__ == "__main__":
    N = int(input())
    ans = moving(N)
    print(ans)
