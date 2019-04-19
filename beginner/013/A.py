def A(X: str)->int:
    return ord(X)-ord('A')+1


if __name__ == "__main__":
    X = input()
    ans = A(X)
    print(ans)
