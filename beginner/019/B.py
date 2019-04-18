def compress(s: str)->str:
    cc, cn = s[0], 0
    res = ''

    for c in s:
        if cc == c:
            cn += 1
        else:
            res += cc + str(cn)
            cc, cn = c, 1
    else:
        res += cc + str(cn)

    return res


if __name__ == "__main__":
    s = input()
    ans = compress(s)
    print(ans)
