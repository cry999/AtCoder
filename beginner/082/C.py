def good_sequence(N: int, A: list) -> int:
    freq = {}
    for a in A:
        freq.setdefault(a, 0)
        freq[a] += 1

    return sum(f if f < n else f - n for n, f in freq.items())


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    ans = good_sequence(N, A)
    print(ans)
