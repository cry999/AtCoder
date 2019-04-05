def honest_or_dishonest(a: str, b: str)->str:
    return 'H' if a == b else 'D'


if __name__ == "__main__":
    a, b = input().split()
    ans = honest_or_dishonest(a, b)
    print(ans)
