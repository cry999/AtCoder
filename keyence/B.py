KEYENCE = 'keyence'


def keyence_string(s: str) -> bool:
    i = 0
    for i, c in enumerate(KEYENCE):
        if s[i] != c:
            break

    return s.endswith(KEYENCE[i:])


if __name__ == "__main__":
    s = input()

    if keyence_string(s):
        print('YES')
    else:
        print('NO')
