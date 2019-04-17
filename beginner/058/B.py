def password(O: str, E: str)->str:
    ret = ''
    for i in range(len(E)*2):
        if i % 2:
            ret += E[i//2]
        else:
            ret += O[i//2]
    return ret + (O[-1] if len(E) < len(O) else '')


if __name__ == "__main__":
    O = input()
    E = input()
    ans = password(O, E)
    print(ans)
