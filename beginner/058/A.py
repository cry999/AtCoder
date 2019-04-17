def lll(a: int, b: int, c: int)->bool:
    return c-b == b-a


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    yes = lll(a, b, c)
    print('YES' if yes else 'NO')
