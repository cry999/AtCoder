def coins(A: int, B: int, C: int, X: int) -> int:
    count = 0
    for a in range(A+1):
        if X < 500 * a:
            break

        xa = X - 500 * a
        for b in range(B+1):
            if xa < 100 * b:
                break

            xb = xa - 100 * b
            for c in range(C+1):
                if xb == 50 * c:
                    count += 1

    return count


if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())

    ans = coins(A, B, C, X)
    print(ans)
