def entrance_examination(T: int, X: int) -> float:
    return T / X


if __name__ == "__main__":
    T, X = [int(s) for s in input().split()]
    ans = entrance_examination(T, X)
    print(ans)
