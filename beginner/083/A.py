def libra(A: int, B: int, C: int, D: int) -> str:
    if A + B > C + D:
        return 'Left'
    if A + B < C + D:
        return 'Right'
    return 'Balanced'


if __name__ == "__main__":
    A, B, C, D = map(int, input().split())
    ans = libra(A, B, C, D)
    print(ans)
