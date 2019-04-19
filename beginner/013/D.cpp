#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define MAX_N 100000
#define MAX_D 1000000000
#define MAX_LOG_D 30

int to2from[MAX_N + 1], from2to[MAX_LOG_D + 1][MAX_N + 1];

int main( int argc, char **argv )
{
    int N, M, D;
    cin >> N >> M >> D;

    for ( int n = 1; n <= N; n++ ) to2from[n] = n;

    for ( int m = 0; m < M; m++ )
    {
        int a;
        cin >> a;

        swap( to2from[a], to2from[a + 1] );
    }

    // 1 回の置換を初期化
    for ( int n = 1; n <= N; n++ ) from2to[0][to2from[n]] = n;

    // 2^k 回の置換を初期化
    for ( int k = 1; k <= MAX_LOG_D; k++ )
        for ( int n = 1; n <= N; n++ )
            // from2to[k-1] に二回通すことで 2^k 回通した置換を得られる。
            from2to[k][n] = from2to[k - 1][from2to[k - 1][n]];

    // D を binary 表現にして通す必要のある 2^k の置換を判定する
    for ( int n = 1; n <= N; n++ )
    {
        int v = n;
        for ( int k = 0; ( 1 << k ) <= D; k++ )
        {
            if ( ( D & ( 1 << k ) ) == 0 ) continue;

            v = from2to[k][v];
        }
        cout << v << endl;
    }
    return 0;
}
