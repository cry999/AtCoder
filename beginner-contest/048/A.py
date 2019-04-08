def atcoder_s_contest(s: str)->str:
    return 'A' + s[0] + 'C'


if __name__ == "__main__":
    _, s, _ = input().split()
    ans = atcoder_s_contest(s)
    print(ans)
