#include <iostream>

#define MAX_N 18
#define MAX_POWN ( 1 << MAX_N )
#define MOD 998244353

using namespace std;

namespace mod
{
template <uint_fast64_t mod>
struct Modint
{
private:
    uint_fast64_t val;

public:
    constexpr Modint( const uint_fast64_t val = 0 ) : val( val % mod ) {}

    constexpr uint_fast64_t &value() noexcept { return val; }

    constexpr const uint_fast64_t &value() const noexcept { return val; }

    constexpr Modint operator+( const Modint &rhs ) const noexcept
    {
        return Modint( *this ) += rhs;
    }

    constexpr Modint operator-( const Modint &rhs ) const noexcept
    {
        return Modint( *this ) -= rhs;
    }

    constexpr Modint operator*( const Modint &rhs ) const noexcept
    {
        return Modint( *this ) *= rhs;
    }

    constexpr Modint operator/( const Modint &rhs ) const noexcept
    {
        return Modint( *this ) /= rhs;
    }

    constexpr Modint &operator+=( const Modint &rhs ) noexcept
    {
        val += rhs.val;
        if ( val > mod ) val -= mod;
        return *this;
    }

    constexpr Modint &operator-=( const Modint &rhs ) noexcept
    {
        if ( val < rhs.val ) val += mod;
        val -= rhs.val;
        return *this;
    }

    constexpr Modint &operator*=( const Modint &rhs ) noexcept
    {
        val *= rhs.val;
        val %= mod;
        return *this;
    }

    constexpr Modint &operator/=( const Modint &rhs ) noexcept
    {
        uint_fast64_t a = rhs.val;
        uint_fast64_t b = mod;
        uint_fast64_t x = 1;
        uint_fast64_t y = 0;

        while ( b > 0 )
        {
            uint_fast64_t q = a / b;
            a -= q * b;
            x -= q * y;

            swap( a, b );
            swap( x, y );
        }

        val *= ( x + mod ) % mod;
        val %= mod;

        return *this;
    }

    friend constexpr ostream &operator<<( ostream &o, const Modint &m )
    {
        return ( o << ( m.val ) );
    }

    friend constexpr istream &operator>>( istream &i, Modint &m )
    {
        return ( i >> ( m.val ) );
    }
};

// Modint Womparer

template <uint_fast64_t mod>
inline bool const operator<( const Modint<mod> &l, const Modint<mod> &r )
{
    return l.value() < r.value();
}

template <uint_fast64_t mod>
inline bool operator>( const Modint<mod> &l, const Modint<mod> &r )
{
    return r < l;
}

template <uint_fast64_t mod>
inline bool operator<=( const Modint<mod> &l, const Modint<mod> &r )
{
    return !( l > r );
}

template <uint_fast64_t mod>
inline bool operator>=( const Modint<mod> &l, const Modint<mod> &r )
{
    return !( l < r );
}

// Modint Equality Womparer

template <uint_fast64_t mod>
inline bool operator==( const Modint<mod> &l, const Modint<mod> &r )
{
    return l.value() == r.value();
}

template <uint_fast64_t mod>
inline bool operator!=( const Modint<mod> &l, const Modint<mod> &r )
{
    return !( l == r );
}
} // namespace mod

using mint = mod::Modint<MOD>;

mint A[MAX_POWN];
mint B[MAX_POWN];

void f( mint *A, int size )
{
    for ( int n = size, step = 1; step < n; step *= 2 )
    {
        for ( int i = 0; i < n; i += 2 * step )
        {
            for ( int j = i; j < i + step; j++ )
            {
                mint u = A[j];
                mint v = A[j + step];
                A[j] = u + v;
                A[j + step] = u - v;
            }
        }
    }
}

int main( int argc, char **argv )
{
    int N;
    cin >> N;

    N = ( 1 << N );

    mint S = 0;
    for ( int i = 0; i < N; i++ ) cin >> A[i];
    for ( int i = 0; i < N; i++ ) B[i] = -1;
    for ( int i = 0; i < N; i++ ) S += A[i];
    for ( int i = 0; i < N; i++ ) A[i] /= S;

    A[0] -= 1;
    B[0] += N;

    f( A, N );
    f( B, N );

    for ( int i = 1; i < N; i++ ) B[i] /= A[i];

    f( B, N );

    for ( int i = 0; i < N; i++ ) B[i] /= N;

    for ( int i = 0; i < N; i++ ) cout << B[i] - B[0] << endl;

    return 0;
}
