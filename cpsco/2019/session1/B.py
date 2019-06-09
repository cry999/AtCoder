def beautiful_harmony(S: str) -> bool:
    freq = {}
    for c in S:
        freq.setdefault(c, 0)
        freq[c] += 1
    return all(freq[S[0]] == v for v in freq.values())


if __name__ == "__main__":
    S = input()

    yes = beautiful_harmony(S)
    print('Yes' if yes else 'No')
