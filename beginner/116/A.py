def right_triangle(AB: int, BC: int, CA: int) -> int:
    return (AB * BC) // 2


if __name__ == "__main__":
    AB, BC, CA = [int(s) for s in input().split()]
    ans = right_triangle(AB, BC, CA)
    print(ans)
