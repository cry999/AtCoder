#include <algorithm>
#include <iostream>
#include <vector>

#define INF ( 1 << 29 )
#define MOD 1000000007
#define MAX_K 100
#define SQRT_MAX_N 80000

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

typedef pair<int, int> P;

vector<P> v;

mint_t dp[MAX_K + 1][SQRT_MAX_N]; // dp
mint_t s[SQRT_MAX_N];             // 累積和

int main( int argc, char **argv )
{
    int N, K;
    cin >> N >> K;

    int x = 1;
    while ( x <= N )
    {
        int d = N / x;

        int p = x;
        for ( int b = 30; b >= 0; b-- )
            if ( p + ( 1 << b ) <= N && N / ( p + ( 1 << b ) ) == d )
                p += 1 << b;

        v.emplace_back( x, p - x + 1 );
        x = p + 1;
    }

    dp[0][0] = 1;

    for ( int i = 1; i <= K; i++ )
    {
        s[0] = dp[i - 1][0];
        for ( int j = 1; j < v.size(); j++ ) s[j] = s[j - 1] + dp[i - 1][j];

        for ( int j = 0; j < v.size(); j++ )
        {
            int d = N / v[j].first;

            int idx =
                upper_bound( v.begin(), v.end(), P( d, INF ) ) - v.begin() - 1;
            dp[i][j] += s[idx] * v[j].second;
        }
    }

    mint_t ans = 0;
    for ( int j = 0; j < v.size(); j++ ) ans += dp[K][j];

    cout << ans << endl;

    return 0;
}
