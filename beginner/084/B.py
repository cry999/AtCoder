def postal_code(A: int, B: int, S: str)->bool:
    if '-' in S[:A]:
        return False
    if S[A] != '-':
        return False
    if '-' in S[-B:]:
        return False
    return True


if __name__ == "__main__":
    A, B = map(int, input().split())
    S = input()
    yes = postal_code(A, B, S)
    print('Yes' if yes else 'No')
