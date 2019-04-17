def equal_or_wildcard(s: str, t: str)->bool:
    for cs, ct in zip(s, t):
        if cs != '?' and cs != ct:
            return False
    return True


def dubious_document2(S: str, T: str)->str:
    ns, nt = len(S), len(T)
    for i in range(ns - nt, -1, -1):
        if equal_or_wildcard(S[i:i+nt], T):
            return (S[:i] + T + S[i+nt:]).replace('?', 'a')
    return 'UNRESTORABLE'


if __name__ == "__main__":
    S = input()
    T = input()
    ans = dubious_document2(S, T)
    print(ans)
