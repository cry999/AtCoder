#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define MAX_V 100000
#define MAX_LOG_V 17

vector<int> G[MAX_V];
int root;

int parent[MAX_LOG_V][MAX_V];
int depth[MAX_V];

void dfs( int v, int p, int d )
{
    parent[0][v] = p;
    depth[v] = d;

    for ( int i = 0; i < (int)G[v].size(); i++ )
        if ( G[v][i] != p ) { dfs( G[v][i], v, d + 1 ); }
}

void lca_init( int V )
{
    memset( parent, 0, sizeof( parent ) );
    memset( depth, 0, sizeof( depth ) );

    dfs( root, -1, 0 );

    for ( int k = 0; k + 1 < MAX_LOG_V; k++ )
    {
        for ( int v = 0; v < V; v++ )
        {
            if ( parent[k][v] < 0 )
                parent[k + 1][v] = -1;
            else
                parent[k + 1][v] = parent[k][parent[k][v]];
        }
    }
}

int lca( int u, int v )
{
    if ( depth[u] > depth[v] ) swap( u, v );

    for ( int k = 0; k < MAX_LOG_V; k++ )
        if ( ( ( depth[v] - depth[u] ) >> k ) & 1 ) v = parent[k][v];

    if ( u == v ) return u;

    for ( int k = MAX_LOG_V - 1; k >= 0; k-- )
    {
        if ( parent[k][u] != parent[k][v] )
        {
            u = parent[k][u];
            v = parent[k][v];
        }
    }
    return parent[0][u];
}

int dist( int u, int v )
{
    int l = lca( u, v );
    return depth[u] + depth[v] - 2 * depth[l];
}

int main( int argc, char **argv )
{
    int N;
    cin >> N;

    root = 0;
    for ( int i = 0; i < N - 1; i++ )
    {
        int x, y;
        cin >> x >> y;

        G[x - 1].push_back( y - 1 );
        G[y - 1].push_back( x - 1 );
    }

    lca_init( N );

    int Q;
    cin >> Q;

    for ( int q = 0; q < Q; q++ )
    {
        int a, b;
        cin >> a >> b;

        cout << dist( a - 1, b - 1 ) + 1 << endl;
    }

    return 0;
}
