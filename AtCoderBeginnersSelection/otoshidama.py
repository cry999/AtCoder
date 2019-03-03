def otoshidama(N: int, Y: int) -> tuple:
    """
    最初に Y //= 1000 としておくと、
    x + y + z = N and 10x + 5y + z = Y
    => 10x + 5y + (N - x - y) = Y
    => 9x + 4y = Y - N
    となる。これはべズーの等式と呼ばれるもの。これをとけば良い。
    :param N: x + y + z
    :param Y: total price
    :return: x, y, z
    """
    Y //= 1000
    x0 = 0
    for i in range(9):
        if (9*i) % 4 == (Y-N) % 4:
            x0 = i
            break

    y0 = (Y-N-(9*x0)) // 4
    mmin = max(-x0//4, (y0-N)//9)
    mmax = min((N-x0)//4, y0//9)

    for m in range(mmin, mmax+1, 1):
        x, y = x0 + 4*m, y0 - 9*m
        z = N - x - y

        if 0 <= x and 0 <= y and 0 <= z:
            return (x, y, z)

    return (-1, -1, -1)


if __name__ == "__main__":
    N, Y = [int(s) for s in input().split()]
    x, y, z = otoshidama(N, Y)
    print(x, y, z)
