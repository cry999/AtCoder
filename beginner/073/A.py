def september9(N: int)->bool:
    return N % 10 == 9 or (N//10) % 10 == 9


if __name__ == "__main__":
    N = int(input())
    yes = september9(N)
    print('Yes' if yes else 'No')
