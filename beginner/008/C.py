def coins(N: int, C: list)->float:
    '''
    c の約数が C に n こあったとする。この時、c が表になる組み合わせは
    ```
    (N この並びから c とその約数を並べるための場所を確保)
    x (c の約数の並び)
    x (c の約数の並びの間で c が表になるように置ける場所)
    x (c とその約数以外の数字の並び)
    = N_C_{n+1} x n! x (n//2 + 1) x (N-(n+1))!
    ```
    通りとなる。

    また、`全組み合わせでの表の個数 = 各コインの全組み合わせでの表になる回数`
    が成り立つので、上の式を各コインについて計算すれば良い。
    '''
    # 計算に利用する comb (組み合わせ)と fact (階乗)をあらかじめ計算しておく
    comb = [[0] * (N+1) for _ in range(N+1)]
    comb[0][0] = 1
    for n in range(N):
        comb[n+1][0] = comb[n][0]
        for r in range(N):
            comb[n+1][r+1] = comb[n][r] + comb[n][r+1]

    fact = [0] * (N+1)
    fact[0] = 1
    for n in range(N):
        fact[n+1] = (n+1) * fact[n]

    total_front = 0
    for c in C:
        # -1 は自分の分
        div_num = sum(c % cc == 0 for cc in C) - 1
        # c とその約数を並べる場所の確保
        front = comb[N][div_num+1]
        # 約数の並べ方
        front *= fact[div_num]
        # c の置き場所(約数が前に偶数個ある場所)
        front *= div_num//2 + 1
        # 他のコインの並べ方
        front *= fact[N-div_num-1]

        total_front += front

    return total_front / fact[N]


if __name__ == "__main__":
    N = int(input())
    C = [int(input()) for _ in range(N)]
    ans = coins(N, C)
    print(ans)
