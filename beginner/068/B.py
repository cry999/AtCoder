def break_number(N: int)->int:
    freq = [0] * (N+1)
    freq[0] = -float('inf')
    d = 2
    while d <= N:
        i = d
        while i <= N:
            freq[i] += 1
            i += d
        d <<= 1

    return freq.index(max(freq))


if __name__ == "__main__":
    N = int(input())
    ans = break_number(N)
    print(ans)
