def goro_awase(K: int, N: int, goro: list) -> list:
    # 3^K 通り (< 19683 ~ 2 * 10^4) の sk の長さの組み合わせ
    # を全探索。
    for i in range(3 ** K):
        # i を 3 進数で表して、k ビット目の値が n だとすると
        # k に対応する sk の長さは n+1 ということにする。
        d = {}
        for k in range(K):
            d[k+1] = (i % 3) + 1
            i //= 3

        for n, w in goro:
            # 各桁の値に対応する sk の仮定の長さの和と w の長さ
            # を比較する。一致しなければ失敗。
            assumpt_len = 0
            while n > 0:
                assumpt_len += d[n % 10]
                n //= 10

            if assumpt_len != len(w):
                # 失敗
                break
        else:
            # sk の仮定の長さが矛盾しなかった場合
            # 与えられた w から長さに見合った範囲の文字列を
            # k に割り当てていき、矛盾しないことを確認する。
            res = {}
            for n, w in goro:
                idx = 0

                digits = []
                while n > 0:
                    k = n % 10
                    n //= 10
                    digits.append(k)

                for k in reversed(digits):
                    sk = w[idx:idx + d[k]]
                    idx = idx + d[k]
                    if k in res and res[k] != sk:
                        break
                    res[k] = sk
                else:
                    # while 文全てパス
                    continue
                # while 文の途中で失敗した
                break
            else:
                # 全ての sk の組み合わせが正しかった。
                return res

    return None


if __name__ == "__main__":
    N = 0
    K, N = map(int, input().split())
    goro = []
    for _ in range(N):
        v, w = input().split()
        goro.append((int(v), w))

    ans = goro_awase(K, N, goro)
    if ans is None:
        raise Exception('error')
    else:
        for _, s in sorted(ans.items()):
            print(s)
