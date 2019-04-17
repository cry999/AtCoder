def string_rotation(S: str, T: str)->bool:
    for i in range(len(S)):
        if S[i:] + S[:i] == T:
            return True
    return False


if __name__ == "__main__":
    S = input()
    T = input()
    yes = string_rotation(S, T)
    print('Yes' if yes else 'No')
