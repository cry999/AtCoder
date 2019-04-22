def snow_depth(H1: int, H2: int) -> int:
    return H1 - H2


if __name__ == "__main__":
    H1, H2 = map(int, [input() for _ in range(2)])

    ans = snow_depth(H1, H2)
    print(ans)
