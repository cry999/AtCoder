def not_so_diverse(N: int, K: int, A: int) -> int:
    freq = [0] * N
    for a in A:
        freq[a - 1] += 1

    return sum(sorted(freq, reverse=True)[K:])


if __name__ == "__main__":
    N, K = map(int, input().split())
    A = [int(s) for s in input().split()]
    ans = not_so_diverse(N, K, A)
    print(ans)
