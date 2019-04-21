def trump(S: str, T: str)->bool:
    for s, t in zip(S, T):
        if s == t:
            continue
        elif s == '@' and t in 'atcoder':
            continue
        elif t == '@' and s in 'atcoder':
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    S = input()
    T = input()

    yes = trump(S, T)
    print('You can win' if yes else 'You will lose')
