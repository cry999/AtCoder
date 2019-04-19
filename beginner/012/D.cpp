#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

#define INF 0x3f3f3f3f
#define MAX_N 300
#define MAX_M 44850

// 最短距離を格納する配列
int d[MAX_N][MAX_N];

int main( int argc, char **argv )
{
    int N, M;
    cin >> N >> M;

    // initalize `d`
    memset( d, INF, sizeof( d ) );
    for ( int i = 0; i < N; i++ ) d[i][i] = 0;

    for ( int m = 0; m < M; m++ )
    {
        int u, v, t;
        cin >> u >> v >> t;

        d[u - 1][v - 1] = d[v - 1][u - 1] = t;
    }

    // warshall-floyd
    for ( int k = 0; k < N; k++ )
        for ( int u = 0; u < N; u++ )
            for ( int v = 0; v < N; v++ )
                d[u][v] = min( d[u][v], d[u][k] + d[k][v] );

    int min_d = INF;
    for ( int u = 0; u < N; u++ )
        min_d = min( min_d, *max_element( d[u], d[u] + N ) );

    cout << min_d << endl;

    return 0;
}
