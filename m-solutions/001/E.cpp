#include <iostream>

#define MOD 1000003

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

mint_t fact[2 * MOD + 1];

void initFact()
{
    fact[0] = 1;
    for ( int i = 0; i < 2 * MOD; i++ ) fact[i + 1] = fact[i] * ( i + 1 );
}

int main( int argc, char **argv )
{
    initFact();

    int Q;
    cin >> Q;

    for ( int q = 0; q < Q; q++ )
    {
        int x, d, n;
        cin >> x >> d >> n;

        if ( x == 0 )
        {
            cout << 0 << endl;
            continue;
        }

        if ( d == 0 )
        {
            mint_t _x = x;
            _x = _x.pow( n );

            cout << _x << endl;
            continue;
        }

        mint_t _x = x;
        mint_t _d = d;

        _x /= _d;

        if ( _x.value() + n - 1 >= MOD )
        {
            cout << 0 << endl;
            continue;
        }

        mint_t ans =
            fact[_x.value() + n - 1] / fact[_x.value() - 1] * _d.pow( n );

        cout << ans << endl;
    }

    return 0;
}
