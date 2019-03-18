def new_year(M: int)->int:
    return 48-M


if __name__ == "__main__":
    M = int(input())
    ans = new_year(M)
    print(ans)
