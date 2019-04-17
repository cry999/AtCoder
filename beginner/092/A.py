def traveling_budget(A: int, B: int, C: int, D: int)->int:
    return min(A, B) + min(C, D)


if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    ans = traveling_budget(A, B, C, D)
    print(ans)
