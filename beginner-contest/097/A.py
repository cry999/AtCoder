def colorful_transceivers(
        a: int, b: int, c: int, d: int) -> bool:
    return (abs(a-b) <= d and abs(b-c) <= d) or abs(a-c) <= d


if __name__ == "__main__":
    a, b, c, d = map(int, input().split())
    yes = colorful_transceivers(a, b, c, d)
    print('Yes' if yes else 'No')
