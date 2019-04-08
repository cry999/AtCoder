def an_ordinary_game(s: str) -> str:
    return 'First' if (len(s) % 2) ^ (s[0] == s[-1]) else 'Second'


if __name__ == "__main__":
    s = input()
    ans = an_ordinary_game(s)
    print(ans)
