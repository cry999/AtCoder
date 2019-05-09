#include <algorithm>
#include <cstring>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define MAX_N 1000
#define MAX_M 2000
#define MAX_K 1000

#define INF 1 << 31

struct edge
{
    int to, cost;
};

typedef pair<int, int> P;

int N, M, K;
vector<edge> G[MAX_N * ( MAX_K + 1 )];

// dp[n][k] = 町 n にたどり着いた時に花を k 本持っているための最小コスト
int64_t dp[MAX_N * ( MAX_K + 1 )];

int main( int argc, char **argv )
{
    // inputs
    cin >> N >> M >> K;
    for ( int m = 0; m < M; m++ )
    {
        int a, b, c;
        cin >> a >> b >> c;

        // 各階層に同じグラフを作る。
        for ( int k = 0; k <= K; k++ )
        {
            G[( a - 1 ) + k * N].push_back( ( edge ){( b - 1 ) + k * N, c} );
            G[( b - 1 ) + k * N].push_back( ( edge ){( a - 1 ) + k * N, c} );
        }
    }
    for ( int n = 0; n < N; n++ )
    {
        int num, price;
        cin >> num >> price;

        // ある階層 k の頂点 n から階層 k+num の頂点 n にコスト price
        // の辺が作れる。 ただし、k+num が K より大きい場合は K
        // として扱う。つまり、0 ~ K-1 層は花 を k 本買った状態を表す層
        // となるが、K 層目は K 本以上買った状態を表す層となる。
        // あと、この層間の辺は一方通行。
        for ( int k = 0; k < K; k++ )
        {
            if ( k + num <= K )
                G[n + k * N].push_back( ( edge ){n + ( k + num ) * N, price} );
            else
                G[n + k * N].push_back( ( edge ){n + K * N, price} );
        }
    }

    // dijkstra
    memset( dp, -1, sizeof( dp ) );
    dp[0] = 0;

    priority_queue<P> q;
    q.push( P( dp[0], 0 ) );

    while ( !q.empty() )
    {
        int u = q.top().second;
        q.pop();

        for ( auto e : G[u] )
        {
            int alt = dp[u] + e.cost;
            if ( dp[e.to] < 0 || alt < dp[e.to] )
            {
                dp[e.to] = alt;
                q.push( P( dp[e.to], e.to ) );
            }
        }
    }

    cout << dp[( N - 1 ) + K * N] << endl;

    return 0;
}
