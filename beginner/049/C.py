def daydream(S: str) -> bool:
    while True:
        if S.endswith('dream'):
            S = S[:-5]
        elif S.endswith('dreamer'):
            S = S[:-7]
        elif S.endswith('erase'):
            if S[:-5].endswith('eras'):
                S = S[:-4]
            else:
                S = S[:-5]
        elif S.endswith('eraser'):
            if S[:-6].endswith('eras'):
                S = S[:-5]
            else:
                S = S[:-6]
        else:
            break

    return S == ''


if __name__ == "__main__":
    S = input()
    ans = daydream(S)
    print('YES' if ans else 'NO')
