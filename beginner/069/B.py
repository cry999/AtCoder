def i18n(s: str)->str:
    n = len(s)
    return s[0] + str(n-2) + s[-1]


if __name__ == "__main__":
    s = input()
    ans = i18n(s)
    print(ans)
