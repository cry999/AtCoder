#include <iostream>
#include <map>
#include <vector>

#define MAX_N 100000
#define LOG_MAX_N 17

using namespace std;

struct Edge
{
    int to, color, cost;
};

struct Query
{
    int x, y, u, v;
};

int N, Q;
vector<Edge> G[MAX_N];
vector<Query> queries;

int __par[MAX_N][LOG_MAX_N + 1];
int __depth[MAX_N];

void __dfs( int u, int p, int dep )
{
    __par[u][0] = p;
    __depth[u] = dep;

    for ( auto e : G[u] )
    {
        if ( e.to == p ) continue;
        __dfs( e.to, u, dep + 1 );
    }
}

int par( int w, int i )
{
    for ( int n = 0; i && n <= LOG_MAX_N; n++ )
    {
        if ( i & 1 ) w = __par[w][n];
        i >>= 1;
    }
    return w;
}

int lca( int a, int b )
{
    if ( __depth[a] < __depth[b] )
        b = par( b, __depth[b] - __depth[a] );
    else
        a = par( a, __depth[a] - __depth[b] );

    if ( a == b ) return a;

    for ( int i = LOG_MAX_N; i >= 0; i-- )
    {
        int pa = par( a, 1 << i );
        int pb = par( b, 1 << i );

        if ( pa == pb ) continue;

        a = pa;
        b = pb;
    }

    return par( a, 1 );
}

int __dist[MAX_N];
int __cnum_work[MAX_N];
int __csum_work[MAX_N];
map<int, int> __cnum[MAX_N];
map<int, int> __csum[MAX_N];
vector<int> need[MAX_N];

void dps( int u, int dist )
{
    __dist[u] = dist;

    for ( auto color : need[u] )
    {
        __cnum[u][color] = __cnum_work[color];
        __csum[u][color] = __csum_work[color];
    }

    for ( auto e : G[u] )
    {
        if ( e.to == par( u, 1 ) ) continue;

        __cnum_work[e.color] += 1;
        __csum_work[e.color] += e.cost;

        dps( e.to, dist + e.cost );

        __cnum_work[e.color] -= 1;
        __csum_work[e.color] -= e.cost;
    }
}

int diff_cost_from_root( int to, int color, int newcost )
{
    return __dist[to] + __cnum[to][color] * newcost - __csum[to][color];
}

void init()
{
    __dfs( 0, 0, 0 );

    for ( int i = 0; i < LOG_MAX_N; i++ )
        for ( int w = 0; w < N; w++ ) __par[w][i + 1] = __par[__par[w][i]][i];

    for ( int i = 0; i < N; i++ ) __cnum_work[i] = __csum_work[i] = 0;
}

int main( int argc, char **argv )
{
    cin >> N >> Q;

    for ( int i = 0; i < N - 1; i++ )
    {
        int a, b, c, d;
        cin >> a >> b >> c >> d;

        G[a - 1].push_back( ( Edge ){b - 1, c, d} );
        G[b - 1].push_back( ( Edge ){a - 1, c, d} );
    }

    init();
    queries.resize( Q );

    for ( auto &q : queries )
    {
        cin >> q.x >> q.y >> q.u >> q.v;
        q.u--, q.v--;

        need[q.u].push_back( q.x );
        need[q.v].push_back( q.x );
        need[lca( q.u, q.v )].push_back( q.x );
    }

    dps( 0, 0 );

    for ( auto q : queries )
    {

        int l = lca( q.u, q.v );

        int dl = diff_cost_from_root( l, q.x, q.y );
        int du = diff_cost_from_root( q.u, q.x, q.y );
        int dv = diff_cost_from_root( q.v, q.x, q.y );

        cout << ( du + dv - 2 * dl ) << endl;
    }

    return 0;
}
