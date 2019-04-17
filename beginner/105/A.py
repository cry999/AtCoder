def atcoder_crackers(N: int, K: int) -> int:
    return 0 if N % K == 0 else 1


if __name__ == "__main__":
    N, K = map(int, input().split())
    ans = atcoder_crackers(N, K)
    print(ans)
