def format_name(S: str)->str:
    return S[0].upper() + S[1:].lower()


if __name__ == "__main__":
    S = input()
    ans = format_name(S)
    print(ans)
