def meal_delivery(x: int, a: int, b: int)->str:
    return 'A' if abs(x - a) < abs(x - b) else 'B'


if __name__ == "__main__":
    x, a, b = map(int, input().split())
    ans = meal_delivery(x, a, b)
    print(ans)
