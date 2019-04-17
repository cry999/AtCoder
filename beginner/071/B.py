def not_found(S: str)->str:
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if c not in S:
            return c
    return 'None'


if __name__ == "__main__":
    S = input()
    ans = not_found(S)
    print(ans)
