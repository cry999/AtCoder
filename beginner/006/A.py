def world_fizz_buff(N: int)->bool:
    return N % 3 == 0 or '3' in str(N)


if __name__ == "__main__":
    N = int(input())

    yes = world_fizz_buff(N)
    print('YES' if yes else 'NO')
