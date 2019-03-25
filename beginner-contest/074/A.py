def bichrome_cells(N: int, A: int)->int:
    return N*N - A


if __name__ == "__main__":
    N = int(input())
    A = int(input())
    ans = bichrome_cells(N, A)
    print(ans)
