def exam_and_wizard(a: list, b: list) -> int:
    if sum(a) < sum(b):
        return -1

    count = 0
    minus = 0
    usable = []
    for _a, _b in zip(a, b):
        if _a < _b:
            minus += _a - _b
            count += 1
        elif _a > _b:
            usable.append(_a - _b)
    
    usable = sorted(usable)
    while minus < 0:
        p = usable.pop()
        minus += p
        count += 1

    
    return count


if __name__ == "__main__":
    # ignore N
    _ = input()
    a = [int(s) for s in input().split()]
    b = [int(s) for s in input().split()]

    ans = exam_and_wizard(a, b)
    print(ans)
