#include <algorithm>
#include <iomanip>
#include <iostream>

#define MAX_N 200
#define MAX_X 100000
#define MOD 1000000007

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

// Modint Comparer

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

// Modint Equality Comparer

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

mint fact[MAX_N + 1];
mint factInv[MAX_N + 1];

void initFact()
{
    fact[0] = 1;
    for ( int i = 0; i < MAX_N; i++ ) fact[i + 1] = fact[i] * mint( i + 1 );

    factInv[MAX_N] = mint( 1 ) / fact[MAX_N];
    for ( int i = MAX_N; i > 0; i-- ) factInv[i - 1] = factInv[i] * mint( i );
}

int S[MAX_N];
mint dp[MAX_N + 1][MAX_X + 1];

int main( int argc, char **argv )
{
    // initialize
    initFact();

    // input
    int N, X;
    cin >> N >> X;

    for ( int i = 0; i < N; i++ ) cin >> S[i];

    // computes dp
    sort( S, S + N, greater<mint>() );

    // initialize dp
    for ( int x = 0; x <= X; x++ ) { dp[N][x] = fact[N] * x; }

    for ( int i = N; i > 0; i-- )
    {
        for ( int x = 0; x <= X; x++ )
        {
            dp[i - 1][x] = dp[i][x] * ( N - i ) + dp[i][x % S[i - 1]];
            dp[i - 1][x] /= ( N + 1 - i );
        }
    }

    cout << dp[0][X] << endl;

    return 0;
}
