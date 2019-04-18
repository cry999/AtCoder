def choku_go(X: str) -> bool:
    if len(X) == 0:
        return True

    if X.endswith('ch'):
        return choku_go(X[:-2])
    if X[-1] in 'oku':
        return choku_go(X[:-1])
    return False


if __name__ == "__main__":
    X = input()
    yes = choku_go(X)
    print('YES' if yes else 'NO')
