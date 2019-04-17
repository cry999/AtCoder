def rotation(C: list) -> bool:
    for n in range(3):
        if C[0][n] != C[1][2-n]:
            return False
    return True


if __name__ == "__main__":
    C = [list(map(str, input())) for _ in range(2)]
    yes = rotation(C)
    print('YES' if yes else 'NO')
