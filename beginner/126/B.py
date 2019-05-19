def is_month(n: int)->bool:
    return 1 <= n and n <= 12


def yymm_or_mmyy(S: str)->str:
    first = int(S[:2])
    second = int(S[2:])

    if is_month(first) and is_month(second):
        return "AMBIGUOUS"
    elif is_month(first):
        return "MMYY"
    elif is_month(second):
        return "YYMM"

    return "NA"


if __name__ == "__main__":
    S = input()

    ans = yymm_or_mmyy(S)
    print(ans)
