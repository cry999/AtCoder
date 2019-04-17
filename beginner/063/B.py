def varied(S: str)->bool:
    d = {}
    for c in S:
        if c in d:
            return False
        d[c] = True
    return True


if __name__ == "__main__":
    S = input()
    yes = varied(S)
    print('yes' if yes else 'no')
