def five_antennas(a: int, b: int, c: int, d: int, e: int, k: int)->bool:
    antennas = [a, b, c, d, e]
    for i in range(5):
        for j in range(i+1, 5):
            if k < antennas[j] - antennas[i]:
                return False
    return True


if __name__ == "__main__":
    inputs = [int(input()) for _ in range(6)]
    a, b, c, d, e, k = inputs
    yes = five_antennas(a, b, c, d, e, k)
    print('Yay!' if yes else ':(')
