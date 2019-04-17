def formula(S: str)->int:
    t = 0           # 今計算中の値
    in_mul = False  # 乗算中かどうか
    count = 0       # 変換回数

    for c in S:
        if c == '*':
            in_mul = True
        elif c == '+':
            in_mul = False
        else:
            if in_mul:
                t *= int(c)
            else:
                if t > 0:
                    # 前回までの計算結果が 0 出ないなら
                    # 一箇所変換しないといけない。
                    count += 1

                t = int(c)

    return count + (t > 0)


if __name__ == "__main__":
    S = input()
    ans = formula(S)
    print(ans)
