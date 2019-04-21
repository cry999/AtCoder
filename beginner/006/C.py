def sphinx(N: int, M: int)->tuple:
    # x, y, z をそれぞれ大人、老人、赤ん坊の人数とする
    # x + y + z = N
    # 2x + 3y + 4z = M
    # となり、これから z を消去することで、
    # 2x + y = 4N - M
    # となる。これはベズーの等式。
    # これが解を持つ条件は 4N - M が GCD(2, 1)=1
    # の倍数であること。

    # y が係数 1 なので探索しやすい
    for y in range(0, N+1):
        if (4*N-M-y) & 1 != 0:
            continue
        if (4*N-M-y) < 0:
            continue

        x = (4*N-M-y)//2
        z = N - x - y
        if z < 0 or N < z:
            continue

        return x, y, z

    return -1, -1, -1


if __name__ == "__main__":
    N, M = map(int, input().split())

    x, y, z = sphinx(N, M)
    print(x, y, z)
