#include <iostream>
#include <set>
#include <vector>

#define MAX_N 100000
#define MAX_X 100000

using namespace std;

typedef pair<int, int> P;

struct UnionFind
{
private:
    vector<int> root;

public:
    UnionFind( int size ) { root.resize( size, -1 ); }

    int find( int x )
    {
        if ( root[x] < 0 ) return x;
        return root[x] = find( root[x] );
    }

    bool same( int x, int y ) { return find( x ) == find( y ); }

    int size( int x ) { return -root[find( x )]; }

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

int main( int argc, char **argv )
{
    int N;
    cin >> N;

    vector<int> X( N );
    vector<int> Y( N );
    for ( int i = 0; i < N; i++ ) cin >> X[i] >> Y[i];

    UnionFind ufx = UnionFind( MAX_X + 1 );
    UnionFind ufy = UnionFind( MAX_X + 1 );

    vector<int> pairX( MAX_X + 1 );
    vector<int> pairY( MAX_X + 1 );
    for ( int i = 0; i < N; i++ )
    {
        if ( pairY[X[i]] > 0 ) ufy.unite( pairY[X[i]], Y[i] );
        pairY[X[i]] = Y[i];

        if ( pairX[Y[i]] > 0 ) ufx.unite( pairX[Y[i]], X[i] );
        pairX[Y[i]] = X[i];
    }

    long long ans = 0;
    set<P> checked;

    for ( int i = 0; i < N; i++ )
    {
        int rx = ufx.find( X[i] );
        int ry = ufy.find( Y[i] );

        if ( checked.find( P( rx, ry ) ) == checked.end() )
        {
            checked.insert( P( rx, ry ) );
            ans += (long long)ufx.size( rx ) * ufy.size( ry );
        }
    }

    cout << ( ans - N ) << endl;

    return 0;
}
