#include <iostream>
#include <vector>

using namespace std;

class SegmentTree
{
private:
    int size;
    vector<long> dat;

    long __query( int a, int b, int k, int l, int r )
    {
        if ( r <= a || b <= l ) return 0;
        if ( a <= l && r <= b ) return dat[k];
        long vl = __query( a, b, 2 * k + 1, l, ( l + r ) / 2 );
        long vr = __query( a, b, 2 * k + 2, ( l + r ) / 2, r );
        return vl | vr;
    }

public:
    SegmentTree( int size )
    {
        this->size = 1;
        while ( this->size < size ) this->size <<= 1;
        dat.resize( 2 * this->size - 1, 0 );
    }

    void update( int idx, long val )
    {
        idx += size - 1;
        dat[idx] = val;
        while ( idx > 0 )
        {
            idx = ( idx - 1 ) / 2;
            dat[idx] = dat[2 * idx + 1] | dat[2 * idx + 2];
        }
    }

    long query( int a, int b ) { return __query( a, b, 0, 0, size ); }
};

int64_t N, K, A[100000];

bool check( int64_t C, SegmentTree st )
{
    int64_t res = 0;
    int r = 0;
    for ( int l = 0; l < N; l++ )
    {
        while ( r < N && st.query( l, r + 1 ) < C ) r++;
        res += N - r;
    }
    return ( res >= K );
}

int64_t or_problem()
{
    SegmentTree st = SegmentTree( N );
    for ( int i = 0; i < N; i++ ) st.update( i, A[i] );

    int64_t l = 0, r = 1LL << 60;
    while ( r - l > 1 )
    {
        int64_t m = ( l + r ) / 2;

        if ( check( m, st ) )
            l = m;
        else
            r = m;
    }
    return l;
}

int main()
{
    cin >> N >> K;
    for ( int i = 0; i < N; i++ ) cin >> A[i];

    int64_t ans = or_problem();
    cout << ans << endl;

    return 0;
}
