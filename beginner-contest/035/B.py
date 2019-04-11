def drone(S: int, T: int)->int:
    d = {'L': 0, 'R': 0, 'U': 0, 'D': 0, '?': 0}
    for c in S:
        d[c] += 1

    dx = abs(d['L']-d['R'])
    dy = abs(d['U']-d['D'])

    if T == 1:
        # 最大値
        return dx + dy + d['?']

    min_d = dx + dy - d['?']
    if min_d >= 0:
        return min_d

    # '?' が余っている場合
    # - '?' が偶数個余っているならペア(LR あるいは UD)を作って
    # 0 にできる。
    # - '?' が奇数個余っているならペアにできないものがあるので
    # 1 余る。
    return (-min_d) % 2


if __name__ == "__main__":
    S = input()
    T = int(input())
    ans = drone(S, T)
    print(ans)
