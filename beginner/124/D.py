def handstand(N: int, K: int, S: str)->int:
    # S を圧縮する。連続している数字の数にする。
    # 例) 111001101 -> [[2, 1], [3, 2, 1]]
    seq = [[], []]
    # S を前から探索する時に使用する変数
    # cur_c は現在見ている文字、cur_n はその文字の連続数
    cur_c, cur_n = S[0], 0

    # 計算しやすいように 1 で始まり、1 で終わる列にしたい。
    if S[0] == '0':
        seq[1].append(0)

    for c in S:
        if cur_c != c:
            seq[int(cur_c)].append(cur_n)
            cur_c = c
            cur_n = 0
        cur_n += 1
    else:
        seq[int(cur_c)].append(cur_n)

    # 計算しやすいように 1 で始まり、1 で終わる列にしたい。
    if S[-1] == '0':
        seq[1].append(0)

    if len(seq[0]) <= K:
        # 0 の領域が K こ以内なら全てひっくり返せる。
        return N

    # cum[i] は i の累積和
    cum = [sum(seq[0][:K]), sum(seq[1][:K+1])]
    max_up = sum(cum)

    for k in range(len(seq[0])-K):
        cum[0] += seq[0][k+K] - seq[0][k]
        cum[1] += seq[1][k+K+1] - seq[1][k]

        max_up = max(max_up, sum(cum))

    return max_up


if __name__ == "__main__":
    N, K = map(int, input().split())
    S = input()
    ans = handstand(N, K, S)
    print(ans)
