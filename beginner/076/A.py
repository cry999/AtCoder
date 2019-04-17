def rating_goal(R: float, G: float)->float:
    return 2*G - R


if __name__ == "__main__":
    R = int(input())
    G = int(input())
    ans = rating_goal(R, G)
    print(ans)
