#include <cmath>
#include <iostream>
#include <map>
#include <vector>

#define INF ( 1 << 30 )
#define MAX_N 1000
#define MAX_A 1000000

using namespace std;

template <long long iniV, const int &( *updateF )( const int &, const int & )>
struct Segtree
{
private:
    int size;
    vector<long long> data;

public:
    Segtree( int size )
    {
        int n = 1;
        while ( n < size ) n <<= 1;

        this->size = n;
        this->data.resize( 2 * n - 1, iniV );
    }

    void update( int idx, long long val )
    {
        idx += size - 1;
        data[idx] = val;

        while ( idx > 0 )
        {
            idx = ( idx - 1 ) / 2;
            data[idx] = updateF( data[2 * idx + 1], data[2 * idx + 2] );
        }
    }

    long long query( int l, int r )
    {
        return query( l, r, 0, 0, size );
        // return 0;
    }

private:
    long long query( int a, int b, int node, int l, int r )
    {
        // no crossing
        if ( b <= l || r <= a ) return iniV;

        // whole included
        if ( a <= l && r <= b ) return data[node];

        int m = ( l + r ) / 2;
        int vl = query( a, b, 2 * node + 1, l, m );
        int vr = query( a, b, 2 * node + 2, m, r );

        return updateF( vl, vr );
    }
};

using RMQ = Segtree<-INF, max>;

int N;
int A[MAX_N];

long long solve()
{
    RMQ rmq( MAX_A + 1 );
    for ( int i = 0; i < MAX_A + 1; i++ ) rmq.update( i, 0 );

    for ( int i = 0; i < N; i++ )
    {
        int sq = sqrt( A[i] );

        map<int, long long> m;

        for ( int x = 1; x <= sq; x++ )
            m[A[i] / x] = A[i] / x + rmq.query( x, x + 1 );

        int r = A[i] + 1;
        for ( int x = 1; x * sq < A[i]; x++ )
        {
            int l = A[i] / ( x + 1 ) + 1;
            long long v = rmq.query( l, r ) + x;

            m[x] = max( m[x], v );

            r = l;
        }

        for ( auto keyValue : m )
        {
            int key = keyValue.first;
            long long value = keyValue.second;

            if ( rmq.query( key, key + 1 ) < value ) rmq.update( key, value );
        }
    }

    return rmq.query( 1, MAX_A + 1 );
}

int main( int argc, char **argv )
{
    cin >> N;

    for ( int i = 0; i < N; i++ ) cin >> A[i];

    cout << solve() << endl;

    return 0;
}
