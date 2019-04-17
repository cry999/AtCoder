def odd_string(s: str)->str:
    return ''.join(c for i, c in enumerate(s) if i % 2 == 0)


if __name__ == "__main__":
    s = input()
    ans = odd_string(s)
    print(ans)
