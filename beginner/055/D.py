def menagerie(N: int, s: str) -> str:
    # Sheep: True, Wolf: False

    # 0 番目と 1 番目の道具ぶつの組み合わせだけ全探索。
    # その 2 頭が決まればあとは一意に決まる。
    is_sheeps = [[None] * N for _ in range(4)]

    # SS
    is_sheeps[0][:2] = True, True
    # SW
    is_sheeps[1][:2] = True, False
    # WS
    is_sheeps[2][:2] = False, True
    # WW
    is_sheeps[3][:2] = False, False

    for n in range(1, N):
        for is_sheep in is_sheeps:
            if (s[n] == 'o') == is_sheep[n]:
                # n 番目の動物が羊で発言が 'o'、あるいは
                # 狼で発言が 'x' なら n 番目の両隣は同じ動物
                is_sheep[(n + 1) % N] = is_sheep[n - 1]
            else:
                # n 番目の動物が羊で発言が 'x'、あるいは
                # 狼で発言が 'o' なら n 番目の両隣は違う動物
                is_sheep[(n + 1) % N] = not is_sheep[n - 1]

    for i, is_sheep in enumerate(is_sheeps):
        if is_sheep[0] != (i // 2 == 0):
            # n-1 番目の動物の発言を検証したときに、
            # 先頭の動物が仮定と矛盾する。
            continue
        if ((s[0] == 'o') == is_sheep[0]) != (is_sheep[1] == is_sheep[-1]):
            # 先頭の動物の発言を検証したときに、
            # 先頭の動物が仮定と矛盾している。
            continue
        return ''.join('S' if b else 'W' for b in is_sheep)

    return '-1'


if __name__ == "__main__":
    N = int(input())
    s = input()
    ans = menagerie(N, s)
    print(ans)
