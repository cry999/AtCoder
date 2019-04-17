def unbalanced(s: str) -> tuple:
    for i in range(len(s) - 1):
        c1, c2 = s[i], s[i + 1]
        if c1 == c2:
            return i+1, i+2
        if i + 2 < len(s):
            c3 = s[i + 2]
            if c1 == c3:
                return i+1, i+3
    return -1, -1


if __name__ == "__main__":
    s = input()
    a, b = unbalanced(s)
    print(a, b)
