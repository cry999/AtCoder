def otoshidama(N: int, Y: int)->int:
    Y //= 1000

    a0 = (Y-N) % 4
    b0 = ((Y-N) - 9 * a0) // 4

    m_min = max(- a0//4,  -(N-b0)//9)
    m_max = min((N-a0)//4, b0//9)+1

    for m in range(m_min, m_max):
        a = a0 + 4*m
        b = b0 - 9*m
        c = N - a - b

        if a < 0 or N < a:
            continue
        if b < 0 or N < b:
            continue
        if c < 0 or N < c:
            continue

        return (a, b, c)

    return (-1, -1, -1)


if __name__ == "__main__":
    N, Y = map(int, input().split())
    x, y, z = otoshidama(N, Y)
    print(x, y, z)
