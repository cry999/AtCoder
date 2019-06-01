def sumo(S: str)->int:
    left = 15-len(S)
    wins = sum(c == 'o' for c in S)

    return left + wins >= 8


if __name__ == "__main__":
    S = input()

    yes = sumo(S)
    print('YES' if yes else 'NO')
