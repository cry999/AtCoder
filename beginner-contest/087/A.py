def buying_sweets(X: int, A: int, B: int) -> int:
    return (X - A) % B


if __name__ == "__main__":
    X = int(input())
    A = int(input())
    B = int(input())
    ans = buying_sweets(X, A, B)
    print(ans)
