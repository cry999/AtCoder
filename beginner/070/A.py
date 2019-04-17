def palindromic_number(N: int) -> bool:
    n1, n100 = N % 10, N//100
    return n1 == n100


if __name__ == "__main__":
    N = int(input())
    yes = palindromic_number(N)
    print('Yes' if yes else 'No')
