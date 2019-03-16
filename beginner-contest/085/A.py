def already_2018(S: str)->str:
    return '2018' + S[4:]


if __name__ == "__main__":
    S = input()
    ans = already_2018(S)
    print(ans)
