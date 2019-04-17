def programming_education(N: int) -> str:
    if N == 1:
        return 'Hello World'

    A = int(input())
    B = int(input())
    return str(A + B)


if __name__ == "__main__":
    N = int(input())
    ans = programming_education(N)
    print(ans)
