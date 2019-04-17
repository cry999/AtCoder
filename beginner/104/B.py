def accepted(S: str)->bool:
    if S[0] != 'A':
        return False
    if sum(1 for c in S[2:-1] if c == 'C') != 1:
        return False

    sorted_s = ''.join(sorted(S)[2:])
    return sorted_s == sorted_s.lower()


if __name__ == "__main__":
    S = input()
    ac = accepted(S)
    print('AC' if ac else 'WA')
