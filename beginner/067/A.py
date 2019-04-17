def sharing_cookies(A: int, B: int)->bool:
    return A % 3 == 0 or B % 3 == 0 or (A+B) % 3 == 0


if __name__ == "__main__":
    A, B = map(int, input().split())
    yes = sharing_cookies(A, B)
    print('Possible' if yes else 'Impossible')
