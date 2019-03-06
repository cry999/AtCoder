def string_transformation(S: int, T: int) -> bool:
    ds = {}
    dt = {}
    for s, t in zip(S, T):
        if s in ds:
            if ds[s] != t:
                return False
        else:
            ds[s] = t

        if t in dt:
            if dt[t] != s:
                return False
        else:
            dt[t] = s

    return True


if __name__ == "__main__":
    S = input()
    T = input()
    ans = string_transformation(S, T)
    print('Yes' if ans else 'No')
