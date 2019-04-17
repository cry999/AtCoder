def kth_substring(s: str, K: int) -> str:
    kth_word = ''     # K 番目の文字列
    kth_word_len = 0  # K 番目の文字列の長さ
    n = len(s)        # s の文字列の長さ

    # 最初の文字から順番に決定していく。
    while K > 0:
        # 探索した文字列を格納する。
        d = set()
        # 例えば 'c' で始まる文字列に対して、'a'、 'b'で
        # 始まる文字列の総数
        prev_count = 0
        # 探索に使う用の文字列
        temp = ''
        for c in 'abcdefghijklmnopqrstuvwxyz':
            temp = kth_word + c
            # s の頭から temp で始まる文字列を探し、
            # それが見つかれば、それをそのまま伸ばして
            # 全て d に入れる
            for i in range(n):
                if s[i:].startswith(temp):
                    for j in range(i, n):
                        d.add(s[i:j+kth_word_len+1])
                        if len(d) >= K:
                            break
                if len(d) >= K:
                    break
            if len(d) >= K:
                break
            # 次の文字に探索対象が変わるとき、現在保持している
            # 文字列の数を保持しておく
            prev_count = len(d)

        # temp から始まる文字列は prev_count 番目以降なので
        # 目標を temp から始まる文字列の K - prev_count 番目
        # の文字列に変更する
        K -= prev_count + 1
        kth_word = temp
    return kth_word


if __name__ == "__main__":
    s = input()
    K = int(input())
    ans = kth_substring(s, K)
    print(ans)
