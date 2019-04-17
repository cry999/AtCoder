def iroha_and_haiku(A: int, B: int, C: int) -> bool:
    return [5, 5, 7] == sorted([A, B, C])


if __name__ == "__main__":
    A, B, C = map(int, input().split())
    yes = iroha_and_haiku(A, B, C)
    print('YES' if yes else 'NO')
