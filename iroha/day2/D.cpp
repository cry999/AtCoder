#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

#define MAX_N 200000
#define MAX_M 400000

class UnionFind
{
private:
    int size;
    vector<int> root;

public:
    UnionFind( int size )
    {
        this->size = size;
        this->root.resize( size, -1 );
    }

    int find( int x )
    {
        if ( root[x] < 0 ) return x;

        return root[x] = find( root[x] );
    }

    bool same( int x, int y ) { return find( x ) == find( y ); }

    void unite( int x, int y )
    {
        int rx = find( x );
        int ry = find( y );

        if ( rx == ry ) return;

        if ( root[ry] < root[rx] ) swap( rx, ry );

        root[rx] += root[ry];
        root[ry] = rx;
    }
};

struct edge
{
    int from, to, cost, idx;

    edge( int from, int to, int cost, int idx )
        : from( from ), to( to ), cost( cost ), idx( idx )
    {
    }

    edge() : from( 0 ), to( 0 ), cost( 0 ), idx( 0 ) {}
};

bool comp_edge( const edge &e1, const edge &e2 ) { return e1.cost < e2.cost; }

int N, M;
edge edges[MAX_M];

vector<int> the_happiest_gardening()
{
    sort( edges, edges + M, comp_edge );

    UnionFind uf = UnionFind( N );
    vector<int> res;

    for ( int i = 0; i < M; i++ )
    {
        edge e = edges[i];

        if ( uf.same( e.from, e.to ) ) continue;

        uf.unite( e.from, e.to );
        res.push_back( e.idx );
    }

    sort( res.begin(), res.end() );

    return res;
}

int main( int argc, char **argv )
{
    cin >> N >> M;
    for ( int i = 0; i < M; i++ )
    {
        int a, b, c;
        cin >> a >> b >> c;

        edges[i] = edge( a - 1, b - 1, -c, i + 1 );
    }

    for ( auto ans : the_happiest_gardening() ) cout << ans << endl;

    return 0;
}
