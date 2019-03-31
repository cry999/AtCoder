def restricted(A: int, B: int)->str:
    if A + B < 10:
        return str(A+B)
    return 'error'


if __name__ == "__main__":
    A, B = map(int, input().split())
    ans = restricted(A, B)
    print(ans)
