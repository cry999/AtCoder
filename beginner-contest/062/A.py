def grouping(x: int, y: int)->bool:
    group = [
        [1, 3, 5, 7, 8, 10, 12],
        [4, 6, 9, 11],
        [2],
    ]
    for g in group:
        if x in g and y in g:
            return True
        elif x in g:
            return False
        elif y in g:
            return False
    return False


if __name__ == "__main__":
    x, y = map(int, input().split())
    yes = grouping(x, y)
    print('Yes' if yes else 'No')
