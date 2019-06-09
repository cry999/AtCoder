def scholarship_payment(M: int, N: int)->int:
    return M - (M//N)*(N-1)


if __name__ == "__main__":
    M, N = map(int, input().split())

    ans = scholarship_payment(M, N)
    print(ans)
