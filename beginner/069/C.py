def four_adjacent(N: int, A: list)->bool:
    n2, n4 = 0, 0
    for a in A:
        if a % 4 == 0:
            n4 += 1
        elif a % 2 == 0:
            n2 += 1
    return N//2 == n4 or N <= 2*n4 + n2


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    yes = four_adjacent(N, A)
    print('Yes' if yes else 'No')
