def thin(H: int, W: int, C: list)->list:
    return [C[h//2] for h in range(2*H)]


if __name__ == "__main__":
    H = 0
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = thin(H, W, C)
    print('\n'.join(ans))
