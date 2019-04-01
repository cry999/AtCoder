def shiritori(A: str, B: str, C: str) -> bool:
    return A[-1] == B[0] and B[-1] == C[0]


if __name__ == "__main__":
    A, B, C = input().split()
    yes = shiritori(A, B, C)
    print('YES' if yes else 'NO')
