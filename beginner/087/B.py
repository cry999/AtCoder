def coins(A: int, B: int, C: int, X: int) -> int:
    count = 0
    for a in range(A + 1):
        if X < 500 * a:
            break
        for b in range(B + 1):
            c = (X - 500 * a - 100 * b) // 50

            if c < 0:
                break

            if 0 <= c and c <= C and 500 * a + 100 * b + 50 * c == X:
                count += 1

    return count


if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    ans = coins(A, B, C, X)
    print(ans)
