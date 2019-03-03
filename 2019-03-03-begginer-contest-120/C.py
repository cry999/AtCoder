def unification(S: str) -> int:
    c0 = sum([int(c) for c in S])
    c1 = sum([1 - int(c) for c in S])

    return min(c0, c1) * 2


if __name__ == "__main__":
    S = input()
    answer = unification(S)
    print(answer)
