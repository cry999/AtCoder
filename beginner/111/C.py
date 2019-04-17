def dekoboko(n: int, v: list) -> int:
    o, e = {}, {}
    for i, vv in enumerate(v):
        if i % 2 == 0:
            if vv not in e:
                e[vv] = 1
            else:
                e[vv] += 1
        else:
            if vv not in o:
                o[vv] = 1
            else:
                o[vv] += 1

    ol = sorted(o.items(), key=lambda x: -x[1])
    el = sorted(e.items(), key=lambda x: -x[1])

    # pivot 選択
    # 頻度が最大のものを固定してそれに合わす様にしたいが、
    # 偶数番号列と奇数番号列とで同じあたいの pivot を使う
    # ことはできない。なので、頻度が最大のものがかぶる様な
    # ら、2番目に頻度が多いものを比較して、頻度の多い方は
    # 2番目のものを使う様にする。
    if ol[0][0] == el[0][0]:
        if len(ol) > 1:
            # 長さが 1 でない時は 2 番目に頻度が高いものの頻度を比べる。
            if ol[1][1] > el[1][1]:
                ol[0], ol[1] = ol[1], ol[0]
            else:
                el[0], el[1] = el[1], el[0]
        else:  # len(ol) == 1
            # 長さが 1 の時はダミーを挿入する
            el.append((0, 0))
            el[0], el[1] = el[1], el[0]

    return sum(v for _, v in ol[1:]) + sum(v for _, v in el[1:])


if __name__ == "__main__":
    n = int(input())
    v = map(int, input().split())
    ans = dekoboko(n, v)
    print(ans)
