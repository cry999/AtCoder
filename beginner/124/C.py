def coloring_colorfully(S: str)->int:
    # 黒から始まるように変更した場合の操作と
    # 白から始まるように変更した場合の操作数。
    black, white = 0, 0

    for i, c in enumerate(S):
        if i % 2 == 0:
            if c == '0':
                white += 1
            else:
                black += 1
        else:
            if c == '0':
                black += 1
            else:
                white += 1

    return min(black, white)


if __name__ == "__main__":
    S = input()
    ans = coloring_colorfully(S)
    print(ans)
