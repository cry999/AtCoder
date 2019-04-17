from math import ceil


def minimization(N: int, K: int, A: list) -> int:
    return 1 + ceil((N - K) / (K - 1))


if __name__ == "__main__":
    N, K = map(int, input().split())
    A = [int(s) for s in input().split()]
    ans = minimization(N, K, A)
    print(ans)
