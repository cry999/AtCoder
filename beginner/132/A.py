def fifty_fifty(S: str)->bool:
    m = {}
    for c in S:
        m.setdefault(c, 0)
        m[c] += 1

    return len(m.keys()) == 2 and all(v == 2 for v in m.values())


if __name__ == "__main__":
    S = input()

    ans = fifty_fifty(S)
    print('Yes' if ans else 'No')
