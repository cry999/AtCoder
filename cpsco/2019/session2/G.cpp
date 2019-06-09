#include <algorithm>
#include <iostream>
#include <vector>

#define MAX_N 50000
#define MAX_Q 50000

using namespace std;

struct UnionFind
{
private:
    vector<int> root;

public:
    UnionFind( int size ) { root.resize( size, -1 ); }

    bool same( int x, int y ) { return find( x ) == find( y ); }

    int find( int x )
    {
        if ( root[x] < 0 ) return x;

        return root[x] = find( root[x] );
    }

    bool unite( int x, int y )
    {
        int rx = find( x );
        int ry = find( y );

        if ( rx == ry ) return false;

        if ( root[ry] < root[rx] ) swap( rx, ry );

        root[rx] += root[ry];
        root[ry] = rx;

        return true;
    }
};

struct Edge
{
    int from;
    int to;
    long long cost;

    bool operator<( const Edge &another ) const { return cost < another.cost; }
};

int main( int argc, char **argv )
{
    // inputs
    int N, M;
    cin >> N >> M;

    vector<Edge> defined, undefined;
    for ( int i = 0; i < M; i++ )
    {
        int u, v;
        cin >> u >> v;

        bool isX;
        cin >> isX;

        if ( isX )
        {
            char x;
            cin >> x;

            undefined.push_back( {u - 1, v - 1, 0} );
        }
        else
        {
            int w;
            cin >> w;

            defined.push_back( {u - 1, v - 1, w} );
        }
    }

    // solve
    sort( defined.begin(), defined.end() );

    UnionFind minTree( N ), noXminTree( N );
    int usedXNum = 0;
    long long totalCost = 0;

    for ( auto e : undefined )
    {
        if ( minTree.unite( e.from, e.to ) ) usedXNum++;
    }

    for ( auto e : defined )
    {
        if ( minTree.unite( e.from, e.to ) )
        {
            totalCost += e.cost;
            noXminTree.unite( e.from, e.to );
        }
    }

    vector<long long> xnum( defined.size() + 1 );
    vector<long long> cost( defined.size() + 1 );

    xnum[0] = usedXNum;
    cost[0] = 0;

    for ( int i = 0; i < defined.size(); i++ )
    {
        xnum[i + 1] = xnum[i];
        cost[i + 1] = cost[i];

        Edge e = defined[i];
        if ( noXminTree.unite( e.from, e.to ) )
        {
            xnum[i + 1]--;
            cost[i + 1] += e.cost;
        }
    }

    int Q;
    cin >> Q;

    for ( int i = 0; i < Q; i++ )
    {
        int a;
        cin >> a;

        auto itr =
            upper_bound( defined.begin(), defined.end(), ( Edge ){0, 0, a} );
        int idx = itr - defined.begin();

        long long num = xnum[idx];
        long long c = cost[idx];

        cout << totalCost + num * a + c << endl;
    }

    return 0;
}
