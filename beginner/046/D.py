def atcodeer_and_rock_paper(s: str) -> int:
    score = 0
    for i, c in enumerate(s):
        if i % 2 == 0 and c == 'p':
            score -= 1
        elif i % 2 == 1 and c == 'g':
            score += 1
    return score


if __name__ == "__main__":
    s = input()
    ans = atcodeer_and_rock_paper(s)
    print(ans)
