#include <algorithm>
#include <iostream>

using namespace std;

int mod_inv( long n, long mod )
{
    long b = mod, u = 1, v = 0;

    while ( b > 0 )
    {
        long t = n / b;

        n -= t * b, u -= t * v;

        swap( n, b ), swap( u, v );
    }

    return ( u + mod ) % mod;
}

int ceil( int a, int b )
{
    if ( ( a / b ) * b == a ) return a / b;
    return a / b + 1;
}

#define MAX_K 3000
#define MOD 998244353

long __fact[MAX_K + 1];
long __inv[MAX_K + 1];

void init_comb()
{
    __fact[0] = __inv[0] = 1;
    for ( int n = 0; n <= MAX_K; n++ )
    {
        __fact[n + 1] = ( ( n + 1 ) * __fact[n] ) % MOD;
        __inv[n + 1] = mod_inv( ( n + 1 ) * __fact[n], MOD );
    }
    return;
}

int comb( int n, int r )
{
    long res = __fact[n];
    res = ( res * __inv[n - r] ) % MOD;
    res = ( res * __inv[r] ) % MOD;
    return res;
}

int banned_x( int N, int X )
{
    long res = 1;

    /* S は数列の和 */
    for ( int S = 1; S <= 2 * N; S++ )
    {
        if ( S < X )
        {
            /**
             * 1, 2 を合計で k 個利用するとする。1 を p 個、2 を q 個とすると
             * p+q=K; p+2q=S;
             * より
             * p=2K-S; q=S-K
             * となる。このとき、0, 1, 2 の並べ方は
             * comb(N,p) * comb(N-p,q)
             * である。また、
             * 0<=p; 0<=q
             * より
             * S/2<=k<=S
             * が成り立つ。
             */
            for ( int k = ceil( S, 2 ); k <= min( S, N ); k++ )
            {
                int p = 2 * k - S, q = S - k;
                res += 1L * comb( N, p ) * comb( N - p, q );
                res %= MOD;
            }
        }
        else if ( S == X )
        {
            continue;
        }
        else if ( ( S - X ) & 1 )
        {
            /* 2 を置かなければいけない場所 */
            int only2 = ( S - ( X - 1 ) ) / 2;

            /* 1 が含まれる場合 */
            if ( 2 * only2 < X - 1 )
            {
                /* SS は 1/2 どちらを置いてもいい区間 */
                int SS = X - 1 - 2 * only2;

                int start = ceil( SS, 2 );
                int end = min( N - 2 * only2, SS );

                /**
                 * k,p,q の意味は S < X の時と同じ。
                 * 全体的に 2 のために確保されている 2*only2
                 * の領域があることに注意する。
                 */
                for ( int k = start; k <= end; k++ )
                {
                    int p = 2 * k - SS, q = SS - k;
                    res += 1L * comb( N, k + 2 * only2 ) * comb( k, p );
                    res %= MOD;
                }
            }
            /* 1 が含まれない場合 */
            else if ( X & 1 )
            {
                res += comb( N, ceil( S, 2 ) );
                res %= MOD;
            }
        }
    }

    return res;
}

int main( int argc, char **argv )
{
    int N, X;
    cin >> N >> X;

    init_comb();

    cout << banned_x( N, X ) << endl;

    return 0;
}
