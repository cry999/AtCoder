#include <cmath>
#include <iostream>

using namespace std;

long long mod_pow( long long a, long long n, long long mod )
{
    long long res = 1;
    while ( n > 0 )
    {
        if ( n & 1 ) res = ( res * a ) % mod;

        a = ( a * a ) % mod;
        n >>= 1;
    }
    return res;
}

long long mod_inv( long long n, long long mod )
{
    long long b = mod;
    long long u = 1;
    long long v = 0;

    while ( b > 0 )
    {
        long long t = n / b;

        n -= t * b;
        u -= t * v;

        swap( n, b );
        swap( u, v );
    }

    return ( u + mod ) % mod;
}

long long q0() { return 5; }

long long q1() { return 5; }

long long q2() { return 10000LL * 10000LL * 10000LL - 1; }

long long q3()
{
    const long long LIMIT = 5 * 1000000000000000;
    long long l = 0;
    long long r = (long long)( sqrt( 50 ) ) * 10000000;

    while ( r - l > 1 )
    {
        long long m = ( l + r ) / 2;
        if ( 2 * m * ( m + 1 ) + 1 <= LIMIT )
            l = m;
        else
            r = m;
    }

    return l + 1 + 50000000;
}

long long q4() { return 1; }

long long q5()
{
    const long long MOD = 1000000007;
    const long long N = 2000000;

    long long ans = mod_pow( 2, 2 * N + 1, MOD ) - 1;
    long long c = N + 1;
    long long x = 2;

    for ( int n = N + 1; n <= 2 * N; n++ )
    {
        ans = ( ans - x + MOD ) % MOD;

        x = ( 2 * x + 2 * c ) % MOD;

        c = ( c * ( n + 1 ) ) % MOD;
        c = ( c * mod_inv( n - N + 1, MOD ) ) % MOD;
    }

    return ans;
}

int main( int argc, char **argv )
{
    int n;
    cin >> n;

    long long ans = -1;
    switch ( n )
    {
    case 0:
        ans = q0();
        break;
    case 1:
        ans = q1();
        break;
    case 2:
        ans = q2();
        break;
    case 3:
        ans = q3();
        break;
    case 4:
        ans = q4();
        break;
    case 5:
        ans = q5();
        break;
    }

    cout << ans << endl;

    return 0;
}
