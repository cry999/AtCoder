#include <iostream>
#include <queue>

#define MAX_N 100000
#define MAX_X 1000000000

using namespace std;

template <typename M, typename N>
M gcd( M a, N b )
{
    a = abs( a );
    b = abs( b );

    if ( a < b ) return gcd( b, a );
    M r;
    while ( ( r = a % b ) )
    {
        a = b;
        b = r;
    }
    return b;
}

namespace fraction
{

template <typename T>
struct Fraction
{
public:
    T numerator;
    T denominator;

    Fraction( T numerator, T denominator )
    {
        if ( numerator == 0 )
        {
            this->numerator = 0;
            this->denominator = 1;
        }
        else
        {
            T g = gcd<T, T>( numerator, denominator );
            this->numerator = numerator / g;
            this->denominator = denominator / g;
        }
    }

    Fraction operator+( const Fraction &rhs )
    {
        long long num =
            numerator * rhs.denominator + denominator * rhs.numerator;
        long long den = rhs.denominator * denominator;
        return Fraction( num, den );
    }

    Fraction operator-( const Fraction &rhs )
    {
        long long num =
            numerator * rhs.denominator - denominator * rhs.numerator;
        long long den = rhs.denominator * denominator;
        return Fraction( num, den );
    }

    friend constexpr ostream &operator<<( ostream &o, const Fraction &m )
    {
        return ( o << ( m.numerator ) << "/" << ( m.denominator ) );
    }

    friend constexpr istream &operator>>( istream &i, Fraction &m )
    {
        return ( i >> ( m.numerator ) << "/" << ( m.denominator ) );
    }
};

template <typename T>
inline bool const operator<( const Fraction<T> &l, const Fraction<T> &r )
{
    return l.numerator * r.denominator < r.numerator * l.denominator;
}

template <typename T>
inline bool const operator>( const Fraction<T> &l, const Fraction<T> &r )
{
    return r < l;
}

template <typename T>
inline bool const operator<=( const Fraction<T> &l, const Fraction<T> &r )
{
    return !( r < l );
}

template <typename T>
inline bool const operator>=( const Fraction<T> &l, const Fraction<T> &r )
{
    return !( l < r );
}
} // namespace fraction

using frac_t = fraction::Fraction<long long>;

typedef pair<int, int> P;
typedef pair<frac_t, P> T;

int a[MAX_N];
int x[MAX_N];

int main( int argc, char **argv )
{
    long long N, X;
    cin >> N >> X;

    long long A = 0;
    for ( int i = 0; i < N; i++ )
    {
        cin >> a[i];
        A += a[i];
    }

    priority_queue<T> que; // T は (減少値、(index, 個数))
    for ( int i = 0; i < N; i++ )
    {
        long long l = 0;
        long long r = X + 1;

        // |x/a - X/A| の減少値が変化する x を探す。
        while ( r - l > 1 )
        {
            long long m = ( l + r ) / 2;
            if ( A * m <= a[i] * X )
                l = m;
            else
                r = m;
        }

        // 単純減少中
        que.push( T( frac_t( 1, a[i] ), P( i, l ) ) );

        // 符号の変更点
        if ( l < X && A * l != a[i] * X )
        {
            frac_t val = frac_t( 2 * X, A ) - frac_t( 2 * l + 1, a[i] );
            que.push( T( val, P( i, 1 ) ) );
            l++;
        }

        // 単純増加中
        que.push( T( frac_t( -1, a[i] ), P( i, MAX_X ) ) );
    }

    while ( !que.empty() && X > 0 )
    {
        frac_t val = que.top().first;
        int idx = que.top().second.first;
        int cnt = que.top().second.second;
        que.pop();

        // cout << val << ":";
        // cout << idx << ",";
        // cout << cnt << endl;

        x[idx] += min( (long long)cnt, X );
        X -= min( (long long)cnt, X );
    }

    for ( int i = 0; i < N; i++ ) cout << x[i] << endl;

    return 0;
}
