namespace fraction
{

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
