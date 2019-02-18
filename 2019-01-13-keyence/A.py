def is1974(n1: int, n2: int, n3: int, n4: int) -> bool:
    a = sorted([n1, n2, n3, n4])
    return a[0] == 1 and a[1] == 4 and a[2] == 7 and a[3] == 9


if __name__ == "__main__":
    n1, n2, n3, n4 = [int(s) for s in input().split()]

    if is1974(n1, n2, n3, n4):
        print('YES')
    else:
        print('NO')
