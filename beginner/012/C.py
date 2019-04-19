def kuku(N: int)->list:
    total = sum(i*j for i in range(1, 10) for j in range(1, 10))
    forgotten = total - N

    return [
        (i, j)
        for i in range(1, 10)
        for j in range(1, 10)
        if i * j == forgotten]


if __name__ == "__main__":
    N = int(input())

    ans = kuku(N)
    for a, b in ans:
        print('{} x {}'.format(a, b))
