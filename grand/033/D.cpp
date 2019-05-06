#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

#define MAX_H 185
#define MAX_W 185
#define MAX_COMPLEXITY 16

int H, W;
string A[MAX_H];

// sum[h][w] = (0, 0) を左上の点 (h, w) を右下の点とする長方形内の黒ますの個数
int sum[MAX_H + 1][MAX_W + 1];
// dph2[w1][w2][h1][c] = (h1, w1)-(h1, w2) を上辺とする長方形で複雑さが c
// 以下となる最大の h2
int dph2[MAX_W + 1][MAX_W + 1][MAX_H + 1][2];
// dpw2[h1][h2][w1][c] = (h1, w1)-(h2, w1) を左辺とする長方形で複雑さが c
// 以下となる最大の w2
int dpw2[MAX_H + 1][MAX_H + 1][MAX_W + 1][2];

/**
 * (h1, w1) を左上、(h2, w2) を右下とする長方形の複雑さが 0
 * であるかを判定します。
 *
 * Judges whether complexity of the rectangle whose left-upper is (h1, w1) and
 * right-down is (h2, w2) is 0 or not.
 */
bool complexity_is_0( int h1, int w1, int h2, int w2 )
{
    int black_num = sum[h2][w2] - sum[h1][w2] - sum[h2][w1] + sum[h1][w1];
    int white_num = ( h2 - h1 ) * ( w2 - w1 ) - black_num;

    return black_num == 0 || white_num == 0;
}

/**
 * initialize `sum`
 */
void init_sum()
{
    for ( int h = 0; h < H; h++ )
    {
        for ( int w = 0; w < W; w++ )
        {
            sum[h + 1][w + 1] = sum[h + 1][w] + sum[h][w + 1] - sum[h][w];
            if ( A[h][w] == '#' ) sum[h + 1][w + 1]++;
        }
    }
}

void init_dp()
{
    for ( int h1 = 0; h1 < H; h1++ )
    {
        for ( int w1 = 0; w1 < W; w1++ )
        {
            int w2 = W;
            // dpw2 の複雑さ 0 の初期化
            // h1, h2, w1 を固定した状態で w2 を複雑さが 0 になるまで縮める。
            // h2 <- h2+1 とした時に w2 は明らかに前回以下の大きさになるので
            // W から縮めていくことで尺取り法になる。
            for ( int h2 = h1 + 1; h2 <= H; h2++ )
            {
                while ( w1 < w2 && !complexity_is_0( h1, w1, h2, w2 ) ) w2--;
                dpw2[h1][h2][w1][0] = w2;
            }

            int h2 = H;
            // dph2 の複雑さ 0 の初期化
            // 上と同様に尺取り法にする。
            for ( int w2 = w1 + 1; w2 <= W; w2++ )
            {
                while ( h1 < h2 && !complexity_is_0( h1, w1, h2, w2 ) ) h2--;
                dph2[w1][w2][h1][0] = h2;
            }
        }
    }
}

int solve()
{
    if ( complexity_is_0( 0, 0, H, W ) ) return 0;

    // 複雑さ c が小さい方から見ていくことで、dp に c
    // に関する領域を持たなくて済む。
    for ( int c = 1; c <= MAX_COMPLEXITY; c++ )
    {
        for ( int h1 = 0; h1 < H; h1++ )
        {
            for ( int w1 = 0; w1 < W; w1++ )
            {
                // dph2 と dpw2
                // の自身のみで求められる分割について先に求めておく。

                // h1, h2, w1 を固定して w2 の最大値を探索する場合の横分割
                for ( int h2 = h1 + 1; h2 <= H; h2++ )
                {
                    // 複雑さ 0 の時の最大の w2 を初期値として、
                    // 横に複雑さが k-1 以下の領域が存在できれば
                    // それを加える。
                    int w2 = dpw2[h1][h2][w1][0];

                    if ( w2 == W )
                        // 横には何もない。
                        dpw2[h1][h2][w1][1] = w2;
                    else
                        // 横に繋げられるかも。
                        dpw2[h1][h2][w1][1] = dpw2[h1][h2][w2][0];
                }

                // w1, w2, h1 を固定して h2 の最大値を探索する場合の縦分割
                for ( int w2 = w1 + 1; w2 <= W; w2++ )
                {
                    // 上と同様に、複雑さ 0 の h2 を初期値として、
                    // 縦に複雑さが k-1 以下の領域を繋げられるか
                    // 試みる。
                    int h2 = dph2[w1][w2][h1][0];

                    if ( h2 == H )
                        // 縦には何もない。
                        dph2[w1][w2][h1][1] = h2;
                    else
                        // 縦に繋げられるかも。
                        dph2[w1][w2][h1][1] = dph2[w1][w2][h2][0];
                }

                // 残りは互いを利用しないといけない分割について求める。

                // h1, h2, w1 を固定して w2 の最大値を探索する場合の縦分割
                for ( int h2 = h1 + 1; h2 <= H; h2++ )
                {
                    int w2 = dpw2[h1][h2][w1][1];

                    while ( w2 < W && h2 <= dph2[w1][w2 + 1][h1][1] ) w2++;

                    dpw2[h1][h2][w1][0] = w2;
                }

                // w1, w2, h1 を固定して h2 の最大値を探索する場合の横分割
                for ( int w2 = w1 + 1; w2 <= W; w2++ )
                {
                    int h2 = dph2[w1][w2][h1][1];

                    while ( h2 < H && w2 <= dpw2[h1][h2 + 1][w1][1] ) h2++;

                    dph2[w1][w2][h1][0] = h2;
                }
            }
        }

        // 複雑さ c 以下にできた
        if ( dph2[0][W][0][0] == H || dpw2[0][H][0][0] == W ) return c;
    }

    // 失敗
    return -1;
}

int main( int argc, char **argv )
{
    cin >> H >> W;
    for ( int h = 0; h < H; h++ ) cin >> A[h];

    init_sum();
    init_dp();

    int ans = solve();

    cout << ans << endl;

    return 0;
}
