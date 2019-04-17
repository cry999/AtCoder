#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

#define MAX_N 300
#define INF 0x3f3f3f3f

struct Edge
{
public:
    int u, v, l;
    Edge() : u( 0 ), v( 0 ), l( 0 ) {}
    Edge( int u, int v, int l ) : u( u ), v( v ), l( l ) {}
};

typedef pair<int, int> edge;

int d[MAX_N][MAX_N];
int adj[MAX_N];

int solve( int N, int M, vector<Edge> edges )
{
    memset( d, INF, sizeof( d ) );
    memset( adj, INF, sizeof( adj ) );

    for ( auto e : edges )
    {
        if ( e.u == 1 )
            adj[e.v - 1] = e.l;
        else
            d[e.u - 1][e.v - 1] = d[e.v - 1][e.u - 1] = e.l;
    }

    // warshal-floyd
    for ( int k = 0; k < N; k++ )
        for ( int u = 0; u < N; u++ )
            for ( int v = 0; v < N; v++ )
                d[u][v] = min( d[u][v], d[u][k] + d[v][k] );

    int min_d = INF;
    for ( int u = 0; u < N; u++ )
    {
        int ul = adj[u];
        if ( ul >= INF ) continue;

        for ( int v = u + 1; v < N; v++ )
        {
            int vl = adj[v];
            if ( vl >= INF ) continue;

            min_d = min( min_d, ul + d[u][v] + vl );
        }
    }

    return min_d < INF ? min_d : -1;
}

int main( int argc, char **argv )
{
    int N, M;
    cin >> N >> M;

    vector<Edge> edges;

    for ( int i = 0; i < M; i++ )
    {
        int u, v, l;
        cin >> u >> v >> l;

        edges.push_back( Edge( u, v, l ) );
    }

    long long ans = solve( N, M, edges );

    cout << ans << endl;

    return 0;
}
