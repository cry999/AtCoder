def sum_of_interior_angles(N: int)->int:
    return (N-2) * 180


if __name__ == "__main__":
    N = int(input())

    ans = sum_of_interior_angles(N)
    print(ans)
