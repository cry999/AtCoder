def takahashis_information(C: list) -> bool:
    for a1 in range(C[0][0] + 1):
        b1 = C[0][0] - a1
        b2 = C[0][1] - a1
        b3 = C[0][2] - a1

        if b1 < 0 or b2 < 0 or b3 < 0:
            continue

        # check a2
        if C[1][0] - b1 != C[1][1] - b2:
            continue
        if C[1][1] - b2 != C[1][2] - b3:
            continue

        # check a3
        if C[2][0] - b1 != C[2][1] - b2:
            continue
        if C[2][1] - b2 != C[2][2] - b3:
            continue

        return True

    return False


if __name__ == "__main__":
    C = [[int(s) for s in input().split()] for _ in range(3)]
    yes = takahashis_information(C)
    print('Yes' if yes else 'No')
