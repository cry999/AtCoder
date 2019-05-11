#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

#define MOD 1000000007
#define MAX_N 200000

using namespace std;

int N, Q;
int A[MAX_N];
string S;

template <uint_fast64_t mod>
class modint
{
private:
    uint_fast64_t val;

public:
    constexpr modint( const uint_fast64_t x = 0 ) noexcept : val( x % mod ) {}

    constexpr modint operator+( const modint rhs ) const noexcept
    {
        return modint( *this ) += rhs;
    }

    constexpr modint operator-( const modint rhs ) const noexcept
    {
        return modint( *this ) -= rhs;
    }

    constexpr modint operator*( const modint rhs ) const noexcept
    {
        return modint( *this ) *= rhs;
    }

    constexpr modint operator/( const modint rhs ) const noexcept
    {
        return modint( *this ) /= rhs;
    }

    constexpr const modint &operator+=( const modint &rhs ) noexcept
    {
        val += rhs.val;
        if ( val >= mod ) val -= mod;
        return *this;
    }

    constexpr modint &operator-=( const modint rhs ) noexcept
    {
        if ( val < rhs.val ) val += mod;
        val -= rhs.val;
        return *this;
    }

    constexpr modint &operator*=( const modint rhs ) noexcept
    {
        val *= rhs.val;
        val %= mod;
        return *this;
    }

    constexpr modint &operator/=( const modint rhs ) noexcept
    {
        uint_fast64_t e = mod - 2;
        modint tmp = rhs;
        while ( e )
        {
            if ( e & 1 ) *this *= tmp;
            tmp *= tmp;
            e >>= 1;
        }
        return *this;
    }

    constexpr uint_fast64_t &value() { return val; }
};

template <typename T>
class segtree
{
private:
    vector<T> data;
    int size;
    T init;

    void __update( int a, int b, T v, int k, int l, int r )
    {
        if ( r <= l ) return;
        if ( a <= l && r <= b )
            data[k] = v;
        else if ( l < b && a < r )
        {
            int lk = 2 * k + 1;
            int rk = 2 * k + 2;
            int m = ( l + r ) / 2;

            __update( a, b, v, lk, l, m );
            __update( a, b, v, rk, m, r );

            if ( S[m - 1] == '*' )
                data[k] = data[lk] * data[rk];
            else
                data[k] = data[lk] + data[rk];
        }
    }

    T __query( int a, int b, int k, int l, int r )
    {
        int lk = 2 * k + 1;
        int rk = 2 * k + 2;
        int m = ( l + r ) / 2;

        if ( r <= a || b <= l ) return init;
        if ( a <= l && r <= b ) return data[k];

        T lv = __query( a, b, lk, l, m );
        T rv = __query( a, b, rk, m, r );

        if ( S[m - 1] == '*' )
            return lv * rv;
        else
            return lv + rv;
    }

public:
    segtree( int size, T init )
    {
        int n = 1;
        while ( n < size ) n <<= 1;

        this->size = n;
        this->init = init;
        this->data.resize( 2 * n - 1, init );
    }

    void update( int a, int b, T v ) { return __update( a, b, v, 0, 0, size ); }
    T query( int a, int b ) { return __query( a, b, 0, 0, size ); }
};

using mint = modint<MOD>;

struct node
{
private:
    mint l, c, r;
    bool has_plus;
    bool empty;

public:
    node( mint l, mint c, mint r )
        : l( l ), c( c ), r( r ), has_plus( true ), empty( false )
    {
    }

    node( mint c ) : l( 0 ), c( c ), r( 0 ), has_plus( false ), empty( false )
    {
    }

    node() : empty( true ) {}

    mint value() { return l + c + r; }

    node operator+( const node rhs ) const
    {
        if ( empty ) return node( rhs );
        if ( rhs.empty ) return node( *this );

        if ( has_plus && rhs.has_plus )
            return node( l, ( c + r + rhs.l + rhs.c ), rhs.r );

        else if ( has_plus && !rhs.has_plus )
            return node( l, ( c + r ), rhs.c );

        else if ( !has_plus && rhs.has_plus )
            return node( c, ( rhs.l + rhs.c ), rhs.r );

        return node( c, 0, rhs.c );
    }

    node operator*( const node rhs ) const
    {
        if ( empty ) return node( rhs );
        if ( rhs.empty ) return node( *this );

        if ( has_plus && rhs.has_plus )
            return node( l, ( c + r * rhs.l + rhs.c ), rhs.r );

        else if ( has_plus && !rhs.has_plus )
            return node( l, c, r * rhs.c );

        else if ( !has_plus && rhs.has_plus )
            return node( c * rhs.l, rhs.c, rhs.r );

        return node( c * rhs.c );
    }
};

int main( int argc, char const *argv[] )
{
    cin >> N;
    for ( int n = 0; n < N; n++ ) cin >> A[n];
    cin >> S;

    // build segment tree
    segtree<node> seg( N, node() );
    for ( int n = 0; n < N; n++ ) seg.update( n, n + 1, node( A[n] ) );

    // handle query
    cin >> Q;
    for ( int q = 0; q < Q; q++ )
    {
        int T, X, Y;
        cin >> T >> X >> Y;

        X--;

        switch ( T )
        {
        case 1:
            // update
            A[X] = Y;
            seg.update( X, X + 1, node( Y ) );
            break;
        case 2:
            // flip operator card
            S[X] = (char)( '*' + '+' - S[X] );
            seg.update( X + 1, X + 2, node( A[X + 1] ) );
            break;
        case 3:
            // get [X, Y)
            mint res = seg.query( X, Y ).value();
            if ( res.value() < 0 ) exit( 1 );
            cout << res.value() << endl;
            break;
        }
    }

    /* code */
    return 0;
}
