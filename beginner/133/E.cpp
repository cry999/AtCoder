#include <cstdint>
#include <iostream>
#include <vector>

#define MOD 1000000007
#define MAX_N 100000

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

    Modint pow( int n )
    {
        Modint res = 1;
        Modint a = Modint( *this );

        while ( n != 0 )
        {
            if ( n & 1 ) res *= a;
            a *= a;
            n >>= 1;
        }

        return res;
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

using mint_t = mod::Modint<MOD>;

int N, K;
vector<int> G[MAX_N];

mint_t dfs( int v, int depth, int par, int seb )
{
    mint_t res = K - seb;
    if ( depth > 0 ) res -= 1;
    if ( depth > 1 ) res -= 1;

    int i = 0;
    for ( auto u : G[v] )
    {
        if ( u == par ) continue;

        res *= dfs( u, depth + 1, v, i );
        i++;
    }

    return res;
}

int main( int argc, char **argv )
{
    cin >> N >> K;

    for ( int i = 0; i < N - 1; i++ )
    {
        int a, b;
        cin >> a >> b;

        G[a - 1].push_back( b - 1 );
        G[b - 1].push_back( a - 1 );
    }

    cout << dfs( 0, 0, -1, 0 ) << endl;

    return 0;
}
