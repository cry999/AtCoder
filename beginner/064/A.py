def rgb_cards(r: int, g: int, b: int)->bool:
    return (10*g + b) % 4 == 0


if __name__ == "__main__":
    r, g, b = map(int, input().split())
    yes = rgb_cards(r, g, b)
    print('YES' if yes else 'NO')
