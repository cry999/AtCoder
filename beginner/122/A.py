def double_helix(b: str)->str:
    if b == 'A':
        return 'T'
    if b == 'T':
        return 'A'
    if b == 'C':
        return 'G'
    return 'C'


if __name__ == "__main__":
    b = input()
    ans = double_helix(b)
    print(ans)
