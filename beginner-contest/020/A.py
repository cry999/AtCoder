def quiz(Q: int)->str:
    if Q == 1:
        return 'ABC'
    return 'chokudai'


if __name__ == "__main__":
    Q = int(input())

    ans = quiz(Q)
    print(ans)
