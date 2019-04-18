def dec6th(M: int, D: int) -> bool:
    return M % D == 0


if __name__ == "__main__":
    M, D = map(int, input().split())
    yes = dec6th(M, D)
    print('YES' if yes else 'NO')
