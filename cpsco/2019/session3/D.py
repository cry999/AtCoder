def decode_rgb_sequences(N: int, S: str)->bool:
    if S[0] != 'R':
        return False

    if S[-1] != 'B':
        return False

    if 'RB' in S:
        return False

    if 'GG' in S:
        return False

    return True


if __name__ == "__main__":
    N = int(input())
    S = input()

    yes = decode_rgb_sequences(N, S)
    print('Yes' if yes else 'No')
