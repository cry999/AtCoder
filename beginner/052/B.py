def increment_decrement(N: int, S: str)->int:
    x, max_x = 0, 0
    for c in S:
        if c == 'I':
            x += 1
            max_x = max(max_x, x)
        else:
            x -= 1
    return max_x


if __name__ == "__main__":
    N = int(input())
    S = input()
    ans = increment_decrement(N, S)
    print(ans)
