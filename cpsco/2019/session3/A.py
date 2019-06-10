def asoko(S: str)->str:
    res = ''
    for c in S:
        if c == 'O':
            res += 'A'
        elif c == 'A':
            res += 'O'
        else:
            res += c
    return res


if __name__ == "__main__":
    S = input()

    ans = asoko(S)
    print(ans)
