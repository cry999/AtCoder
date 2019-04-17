def pow_mod(a: int, n: int, mod: int)->int:
    ret = 1
    for _ in range(n):
        ret = (ret * a) % mod
    return ret


def ok(s: str)->bool:
    '''s が条件をみたすかを判定。
    :param s: 判定対象
    :return: 判定結果
    '''
    if 'AGC' == s[-3:]:
        return False
    if 'GAC' == s[-3:]:
        return False
    if 'ACG' == s[-3:]:
        return False
    if 'A' == s[0] and 'GC' == s[-2:]:
        return False
    if 'AG' == s[:2] and 'C' == s[-1]:
        return False
    return True


def we_like_agc(N: int)->int:
    MOD = 10**9 + 7
    AGCT = 'AGCT'

    # dp[i][str] は str の出現回数。
    # また、この dp は前回のメモだけあればいいので 0, 1 にのみ対応。
    dp = [{}, {}]

    # dp の初期化
    # 3 文字で構成される全ての文字列に対して初期化を行う。
    for c1 in AGCT:
        for c2 in AGCT:
            for c3 in AGCT:
                dp[0][c1 + c2 + c3] = 1 if ok(c1 + c2 + c3) else 0
                dp[1][c1 + c2 + c3] = 0

    # i-1 文字の最後の 3 文字を利用して i 文字目のありうる
    # 最後の 3 文字をカウントする。
    turn = 0
    for _ in range(3, N):
        next_turn = 1-turn
        for s, v in dp[turn].items():
            for c in AGCT:
                next_word = s[1:] + c
                if ok(s + c):
                    # i-1 文字の可能な文字列の後ろに c を足した時
                    # それも可能な文字列ならカウントアップ
                    dp[next_turn][next_word] += v
                    dp[next_turn][next_word] %= MOD
            # 次に使えるように初期化
            dp[turn][s] = 0
        # ターンの遷移
        turn = next_turn

    return sum(v for s, v in dp[(N+1) & 1].items() if ok(s)) % MOD


if __name__ == "__main__":
    N = int(input())
    ans = we_like_agc(N)
    print(ans)
