#include <algorithm>
#include <iostream>

using namespace std;

#define MAX_N 1000000
#define MOD 1000000007

long long pow2[MAX_N + 1], fact[MAX_N + 1], fact_inv[MAX_N + 1];

long long mod_inv( long long n, long long mod )
{
    long long b = mod, u = 1, v = 0;
    while ( b > 0 )
    {
        long long t = n / b;
        n -= t * b;
        u -= t * v;

        swap( n, b ), swap( u, v );
    }
    return ( u + mod ) % mod;
}

long long bin_pow( long long a, long long n, long long mod )
{
    long res = 1;
    while ( n > 0 )
    {
        if ( n & 1 ) res = ( res * a ) % mod;
        a = ( a * a ) % MOD;
        n >>= 1;
    }
    return res;
}

void init( int N )
{
    pow2[0] = 1, fact[0] = 1;
    for ( int n = 0; n < N; n++ )
    {
        pow2[n + 1] = ( 2 * pow2[n] ) % MOD;
        fact[n + 1] = ( ( n + 1 ) * fact[n] ) % MOD;
    }

    fact_inv[N] = mod_inv( fact[N], MOD );
    for ( int n = N; n > 0; n-- ) fact_inv[n - 1] = ( n * fact_inv[n] ) % MOD;

    return;
}

long long comb( int n, int r )
{
    long long res = fact[n];
    res *= fact_inv[n - r];
    res %= MOD;

    res *= fact_inv[r];
    res %= MOD;

    return res;
}

long long one_third( int N )
{
    long long ans = 0;
    for ( int i = 1; i <= N; i++ )
    {
        long long w = pow2[i];

        if ( i & 1 )
            w = ( w + 1 ) % MOD;
        else
            w = ( w - 1 ) % MOD;

        long long t = comb( N, i );
        t = ( t * w ) % MOD;
        t = ( t * mod_inv( i, MOD ) ) % MOD;

        ans += t;
        ans %= MOD;
    }

    ans *= mod_inv( bin_pow( 3, N + 1, MOD ), MOD );
    ans %= MOD;

    ans *= mod_inv( N, MOD );
    ans %= MOD;

    return ans;
}

int main( int argc, char **argv )
{
    int N;
    cin >> N;

    init( N );

    cout << one_third( N ) << endl;

    return 0;
}
