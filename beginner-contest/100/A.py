def happy_birthday(A: int, B: int) -> bool:
    return A <= 8 and B <= 8


if __name__ == "__main__":
    A, B = map(int, input().split())
    yes = happy_birthday(A, B)
    print('Yay!' if yes else ':(')
