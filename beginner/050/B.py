def contest_with_drinks_easy(N: int, T: list, M: int, drinks: list)->list:
    total = sum(T)
    return [total - T[p-1] + m for p, m in drinks]


if __name__ == "__main__":
    N = int(input())
    T = [int(s) for s in input().split()]
    M = int(input())
    drinks = [tuple(int(s) for s in input().split()) for _ in range(M)]
    ans = contest_with_drinks_easy(N, T, M, drinks)
    print('\n'.join(map(str, ans)))
