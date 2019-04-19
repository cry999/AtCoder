def ceil(a: int, b: int)->int:
    if (a//b) * b == a:
        return a//b
    return a//b+1


def give_sweets(a: int, b: int)->int:
    return ceil(a, b)*b - a


if __name__ == "__main__":
    a = int(input())
    b = int(input())

    ans = give_sweets(a, b)
    print(ans)
