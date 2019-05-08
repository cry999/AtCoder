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

struct shop
{
    int num, price;
};

typedef pair<int, int> P;

int N, M, K;
vector<edge> G[MAX_N];
shop F[MAX_N];

// dp[n][k] = 町 n にたどり着いた時に花を k 本持っているための最小コスト
int64_t dp[MAX_N][MAX_K + 1];

int main( int argc, char **argv )
{
    // inputs
    cin >> N >> M >> K;
    for ( int m = 0; m < M; m++ )
    {
        int a, b, c;
        cin >> a >> b >> c;

        G[a - 1].push_back( ( edge ){b - 1, c} );
        G[b - 1].push_back( ( edge ){a - 1, c} );
    }
    for ( int n = 0; n < N; n++ ) { cin >> F[n].num >> F[n].price; }

    // 改造 dijkstra
    memset( dp, INF, sizeof( dp ) );
    dp[0][0] = 0;

    int n = F[0].num, p = F[0].price;
    for ( int k = 0; true; k += n )
    {
        if ( k >= K )
        {
            dp[0][K] = k * p;
            break;
        }
        dp[0][k] = k * p;
    }

    priority_queue<P> q;

    return 0;
}
