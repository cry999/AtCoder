#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

#define MAX_N 200000

string S, T;

bool solve( int H, int W, int N, int r, int c )
{
    // それぞれ、スタート地点 (sr, sc) から上下左右の境界へのマージン
    const int U = r - 1;
    const int D = H - r;
    const int L = c - 1;
    const int R = W - c;

    // 高橋くんの移動可能範囲
    int sl, sr, su, sd;
    sl = sr = su = sd = 0;

    // 青木くんの移動可能範囲
    int tl, tr, tu, td;
    tl = tr = tu = td = 0;

    for ( int n = 0; n < N; n++ )
    {
        if ( S[n] == 'L' ) sl++;
        if ( S[n] == 'R' ) sr++;
        if ( S[n] == 'U' ) su++;
        if ( S[n] == 'D' ) sd++;

        // 高橋くんの移動後に盤の外へ移動できるのなら、こまは残らない。
        if ( L < sl - tr ) return false;
        if ( R < sr - tl ) return false;
        if ( U < su - td ) return false;
        if ( D < sd - tu ) return false;

        // 青木くんは自分盤内に収まるように移動可能範囲を計算しないといけない。
        if ( T[n] == 'L' && tl - sr < L ) tl++;
        if ( T[n] == 'R' && tr - sl < R ) tr++;
        if ( T[n] == 'U' && tu - sd < U ) tu++;
        if ( T[n] == 'D' && td - su < D ) td++;
    }

    // 全ての文字を処理後にまだ盤の外へ出ていない。つまり、こまは残る。
    return true;
}

int main( int argc, char **argv )
{
    int H, W, N;
    cin >> H >> W >> N;

    int sr, sc;
    cin >> sr >> sc;

    cin >> S;
    cin >> T;

    bool ans = solve( H, W, N, sr, sc );

    if ( ans )
        cout << "YES" << endl;
    else
        cout << "NO" << endl;

    return 0;
}
