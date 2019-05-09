#include <iostream>
#include <queue>

using namespace std;

typedef long long ll;
typedef pair<int, ll> P;

#define INF 1e16
#define mod 1000000007

struct state
{
    int i, j;
    ll cost;
};

struct edge
{
    int to, cost;
};

bool operator<( const state &a, const state &b ) { return a.cost > b.cost; }

int N, M, K;
vector<edge> G[1001];
int X[1001];
ll Y[1001];

ll dp[1001][2001];

int main()
{
    cin >> N >> M >> K;
    for ( int m = 0; m < M; m++ )
    {
        int a, b, c;
        cin >> a >> b >> c;

        G[a - 1].push_back( ( edge ){b - 1, c} );
        G[b - 1].push_back( ( edge ){a - 1, c} );
    }

    for ( int n = 0; n < N; n++ ) cin >> X[n] >> Y[n];
    for ( int i = 0; i < N; i++ )
        for ( int j = 0; j < 2 * K + 1; j++ ) dp[i][j] = INF;

    priority_queue<state> que;
    que.push( ( state ){0, 0, 0} );
    dp[0][0] = 0;

    while ( !que.empty() )
    {
        state s = que.top();
        que.pop();

        if ( dp[s.i][s.j] < s.cost ) continue;
        if ( s.j + X[s.i] <= 2 * K )
        {
            if ( dp[s.i][s.j + X[s.i]] > s.cost + Y[s.i] )
            {
                dp[s.i][s.j + X[s.i]] = s.cost + Y[s.i];
                que.push( ( state ){s.i, s.j + X[s.i], s.cost + Y[s.i]} );
            }
        }
        for ( auto e : G[s.i] )
        {
            if ( dp[e.to][s.j] > s.cost + e.cost )
            {
                dp[e.to][s.j] = s.cost + e.cost;
                que.push( ( state ){e.to, s.j, s.cost + e.cost} );
            }
        }
    }

    ll res = INF;
    for ( ll k = K; k < 2 * K + 1; k++ ) res = min( res, dp[N - 1][k] );

    cout << ( ( res == INF ) ? -1 : res ) << endl;

    return 0;
}
