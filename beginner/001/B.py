def synop(m: int) -> int:
    if m < 100:
        return 0
    if m < 6000:
        return m * 10 // 1000
    if m < 35000:
        return m // 1000 + 50
    if m <= 70000:
        return ((m // 1000) - 30) // 5 + 80
    return 89


if __name__ == "__main__":
    m = int(input())

    ans = synop(m)
    print('{:02}'.format(ans))
