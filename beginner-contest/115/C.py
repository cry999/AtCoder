def christmas_eve(N: int, K: int, H: list) -> int:
    sorted_H = sorted(H, reverse=True)
    return min(sorted_H[i] - sorted_H[i + K - 1] for i in range(N - K + 1))


if __name__ == "__main__":
    N, K = [int(s) for s in input().split()]
    H = [int(input()) for _ in range(N)]
    ans = christmas_eve(N, K, H)
    print(ans)
