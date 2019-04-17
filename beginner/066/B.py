def ss(S: str)->int:
    n = len(S)
    ret = 0
    for i in range((n-1)//2):
        if S[i+1:].startswith(S[:i+1]):
            ret = 2*(i+1)

    return ret


if __name__ == "__main__":
    S = input()
    ans = ss(S)
    print(ans)
