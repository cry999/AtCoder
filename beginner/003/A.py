def salary(N: int)->int:
    return 10000*(N+1)//2


if __name__ == "__main__":
    N = int(input())

    ans = salary(N)
    print(ans)
