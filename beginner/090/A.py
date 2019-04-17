def diagonal_string(C: list) -> str:
    return ''.join(C[i][i] for i in range(3))


if __name__ == "__main__":
    C = [input() for _ in range(3)]
    ans = diagonal_string(C)
    print(ans)
