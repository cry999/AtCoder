def abc333(A: int, B: int)->bool:
    return (A == 1 or A == 3) and (B == 1 or B == 3)


if __name__ == "__main__":
    A, B = map(int, input().split())
    yes = abc333(A, B)
    print('Yes' if yes else 'No')
