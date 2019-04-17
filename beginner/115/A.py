def christmas_eve_eve_eve(D: int) -> str:
    ret = ['Christmas'] + (['Eve'] * (25 - D))
    return ' '.join(ret)


if __name__ == "__main__":
    D = int(input())
    ans = christmas_eve_eve_eve(D)
    print(ans)
