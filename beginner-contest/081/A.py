def placing_marbles(s: str) -> int:
    return sum(c == '1' for c in s)


if __name__ == "__main__":
    s = input()
    ans = placing_marbles(s)
    print(ans)
