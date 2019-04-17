def ft_robot(s: str, x: int, y: int) -> int:
    # 各方向への一回に移動可能な距離のリストをもつ。
    # ds[0] が x 軸方向用。ds[1] が y軸方向用。
    ds = [[], []]
    axis = 0
    cur_dis = 0
    for c in s:
        if c == 'T':
            ds[axis].append(cur_dis)
            axis = 1 - axis
            cur_dis = 0
        else:
            cur_dis += 1

    ds[axis].append(cur_dis)

    if len(ds[0]) > 0 and ds[0][0] != x:
        # 最初だけは方向が決まっているのでスタート位置に補正を入れることで対応する。
        ds[0][0] = abs(ds[0][0] - x)
    elif x != 0:
        ds[0].append(abs(x))

    ds[1].append(abs(y))

    # 移動方向は軸は決まっているが正負は決まっていないので自由に決める。
    # また、足し算なので順番は関係ない。
    sx, sy = 0, 0
    for dx in sorted(ds[0], key=lambda i: -i):
        if 0 < sx:
            sx -= dx
        else:
            sx += dx

    if sx != 0:
        return False

    for dy in sorted(ds[1], key=lambda i: - i):
        if 0 < sy:
            sy -= dy
        else:
            sy += dy

    return sy == 0


if __name__ == "__main__":
    s = input()
    x, y = map(int, input().split())
    yes = ft_robot(s, x, y)
    print('Yes' if yes else 'No')
