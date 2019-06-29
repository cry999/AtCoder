#include <iostream>
#include <queue>
#include <vector>

#define MAX_N 100000
#define INF ( 1 << 29 )

using namespace std;

typedef pair<int, int> P;

int N, M;
vector<int> G[3 * MAX_N + 1];

int d[3 * MAX_N + 1];

int dijkstra( int s, int t, int N )
{
    priority_queue<P> que;
    for ( int v = 1; v <= N; v++ )
    {
        d[v] = ( v == s ) ? 0 : INF;
        que.push( P( -d[v], v ) );
    }

    while ( !que.empty() )
    {
        int u = que.top().second;
        que.pop();

        for ( auto v : G[u] )
        {
            int alt = d[u] + 1;
            if ( d[v] > alt )
            {
                d[v] = alt;
                que.push( P( -d[v], v ) );
            }
        }
    }

    return d[t] >= INF ? -1 : d[t];
}

int main( int argc, char **argv )
{

    cin >> N >> M;

    for ( int i = 0; i < M; i++ )
    {
        int u, v;
        cin >> u >> v;

        int us[] = {u, u + N, u + 2 * N};
        int vs[] = {v, v + N, v + 2 * N};

        // u0->v1; u1->v2; u2->v0;
        for ( int i = 0; i < 3; i++ ) G[us[i]].push_back( vs[( i + 1 ) % 3] );
    }

    int S, T;
    cin >> S >> T;

    int ans = dijkstra( S, T, 3 * N );
    cout << ( ans < 0 ? ans : ans / 3 ) << endl;

    return 0;
}
