def dic_seq(A: str)->str:
    if A == 'a':
        return None
    return 'a'


if __name__ == "__main__":
    A = input()

    ans = dic_seq(A)
    print(ans if ans else '-1')
