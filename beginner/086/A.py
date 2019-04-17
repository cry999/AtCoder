def product(A: int, B: int)->str:
    return 'Odd' if A % 2 and B % 2 else 'Even'


if __name__ == "__main__":
    A, B = map(int, input().split())
    ans = product(A, B)
    print(ans)
