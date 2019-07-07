def TorT(N: int, A: int, B: int)->int:
    return min(A*N, B)


if __name__ == "__main__":
    N, A, B = map(int, input().split())
    ans = TorT(N, A, B)
    print(ans)
