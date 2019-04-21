def sum1(n: int)->int:
    return n*(n+1)//2


def sum_from_to(left: int, center: int, right: int)->int:
    '''cener から移動して、[left, right] にマーブルを広げる
    時の移動量。
    '''
    if center < left:
        return sum1(right-center) - sum1(left-center-1)
    if right < center:
        return sum1(center-left) - sum1(center-right-1)
    # center を挟む
    return sum1(right-center) + sum1(center-left)


def marble(R: int, G: int, B: int)->int:
    min_movement = float('inf')

    for left_g in range(-400, 401):
        movement = 0

        # G の位置をまず決める
        right_g = left_g+G-1
        movement += sum_from_to(left_g, 0, right_g)

        # R の位置を次に決める。
        # R は一番右を決める。候補は G のすぐ左か、R
        # の中心(-100)から均等に左右にマーブルを分配
        # した時の位置。
        right_r = min(left_g-1, -100+(R-1)//2)
        left_r = right_r-R+1
        movement += sum_from_to(left_r, -100, right_r)

        # B の位置を次に決める。
        # R の次に決めたが、依存関係はない。
        # B は一番左を決める。候補は G のすぐ右か、B
        # の中心(100)から均等に左右にマーブルを分配し
        # た時の位置。
        left_b = max(right_g+1, 100-(B-1)//2)
        right_b = left_b+B-1
        movement += sum_from_to(left_b, 100, right_b)

        # 探索した最小値が答え
        min_movement = min(min_movement, movement)

    return min_movement


if __name__ == "__main__":
    R, G, B = map(int, input().split())

    min_movement = marble(R, G, B)
    print(min_movement)
