def stones(N: int, S: str)->int:
    # 左から見た黒石の個数の累積和と
    # 右から見た白石の個数の累積和を保持し
    # その和が最小となる位置を探す。
    black, white = [0] * (N+1), [0] * (N+1)

    for i, c in enumerate(S):
        black[i+1] = black[i]
        if c == '#':
            black[i+1] += 1

    for i, c in enumerate(S[::-1]):
        white[N-i-1] = white[N-i]
        if c == '.':
            white[N-i-1] += 1

    # print(black)
    # print(white)

    return min(black[i] + white[i+1] for i in range(N))


if __name__ == "__main__":
    N = int(input())
    S = input()
    ans = stones(N, S)
    print(ans)
