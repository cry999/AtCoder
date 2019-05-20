#include <iostream>

#define MOD 1000000007
#define MAX_B 100000
#define MAX_W 100000

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

const int MAX_COMB = MAX_B + MAX_W;

mint fact[MAX_COMB + 1];
mint factInv[MAX_COMB + 1];

void initFact()
{
    fact[0] = 1;
    for ( int i = 0; i < MAX_COMB; i++ ) fact[i + 1] = fact[i] * ( i + 1 );

    factInv[MAX_COMB] = mint( 1 ) / fact[MAX_COMB];
    for ( int i = MAX_COMB; i > 0; i-- ) factInv[i - 1] = factInv[i] * i;
}

mint comb( int n, int r )
{
    if ( n < 0 || r < 0 || n < r ) return 0;
    if ( r == 0 || r == n ) return 1;

    return fact[n] * factInv[r] * factInv[n - r];
}

int main( int argc, char **argv )
{
    initFact();

    int B, W;
    cin >> B >> W;

    mint probB = 0;
    mint probW = 0;
    mint inv2 = mint( 1 ) / 2;

    for ( int i = 1; i <= B + W; i++ )
    {
        // compute ans
        mint ans = ( mint( 1 ) - probB + probW ) / 2;

        cout << ans << endl;

        probB += comb( i - 1, B - 1 ) * inv2;
        probW += comb( i - 1, W - 1 ) * inv2;

        // compute next values
        inv2 /= 2;
    }

    return 0;
}
