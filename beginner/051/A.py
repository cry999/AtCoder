def haiku(s: str)->str:
    return s[:5] + ' ' + s[6:13] + ' ' + s[14:]


if __name__ == "__main__":
    s = input()
    ans = haiku(s)
    print(ans)
