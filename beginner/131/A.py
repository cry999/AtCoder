def security(S: str)->bool:
    return S[0] != S[1] and S[1] != S[2] and S[2] != S[3]


if __name__ == "__main__":
    S = input()

    good = security(S)
    print('Good' if good else 'Bad')
