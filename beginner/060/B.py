def choose_integers(A: int, B: int, C: int) -> bool:
    n = A
    for _ in range(B):
        n %= B
        if n == C:
            return True
        n = (n + A)
    return False


if __name__ == "__main__":
    A, B, C = map(int, input().split())
    yes = choose_integers(A, B, C)
    print('YES' if yes else 'NO')
