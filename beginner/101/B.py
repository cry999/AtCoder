def digit_sums(N: int) -> bool:
    s = 0
    temp = N
    while temp > 0:
        s += temp % 10
        temp //= 10
    return N % s == 0


if __name__ == "__main__":
    N = int(input())
    yes = digit_sums(N)
    print('Yes' if yes else 'No')
