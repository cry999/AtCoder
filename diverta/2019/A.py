def consecutive_integers(N: int, K: int)->int:
    return N - (K-1)


if __name__ == "__main__":
    N, K = map(int, input().split())

    ans = consecutive_integers(N, K)
    print(ans)
