def something_on_it(S: str) -> int:
    return 700 + sum(100 if c == 'o' else 0 for c in S)


if __name__ == "__main__":
    S = input()
    ans = something_on_it(S)
    print(ans)
