def hina_arare(N: int, S: list) -> str:
    return 'Four' if 'Y' in S else 'Three'


if __name__ == "__main__":
    N = int(input())
    S = input()
    ans = hina_arare(N, S)
    print(ans)
