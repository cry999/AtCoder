def abc_of_abc(S: str) -> bool:
    return 'a' in S and 'b' in S and 'c' in S


if __name__ == "__main__":
    S = input()
    yes = abc_of_abc(S)
    print('Yes' if yes else 'No')
