def eating_symbols_easy(S: str) -> int:
    ans = 0
    for symbol in S:
        if symbol == '+':
            ans += 1
        else:
            ans -= 1
    return ans


if __name__ == "__main__":
    S = input()
    ans = eating_symbols_easy(S)
    print(ans)
