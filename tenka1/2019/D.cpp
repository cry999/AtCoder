#include <algorithm>
#include <iostream>
#include <cstring>

using namespace std;

// a/b の切り上げを求める
int ceil( int a, int b )
{
    if ( ( a / b ) * b == a ) return a / b;

    return a / b + 1;
}

long pow_mod( long a, long n, long mod )
{
    if ( n == 0 ) return 1;

    if ( n & 1 )
    {
        long t = pow_mod( a, n - 1, mod );
        return ( a * t ) % mod;
    }
    else
    {
        long t = pow_mod( a, n >> 1, mod );
        return ( t * t ) % mod;
    }
}

#define MAX_N 300
#define MAX_A 300
#define MOD 998244353

// R が S/2 以上の場合を数える dp
long dp1[MAX_N + 1][MAX_N * MAX_A + 1];
// R=G=S/2 となる場合を数える dp
long dp2[MAX_N + 1][MAX_N * MAX_A + 1];

long A[MAX_N];

int main( int argc, char **argv )
{
    int N;
    cin >> N;

    long S = 0;
    for ( int n = 0; n < N; n++ )
    {
        cin >> A[n];
        S += A[n];
    }

    memset( dp1, 0, sizeof( dp1 ) );
    memset( dp2, 0, sizeof( dp2 ) );

    dp1[0][0] = dp2[0][0] = 1;

    long limit = ceil( S, 2 );

    for ( int n = 0; n < N; n++ )
    {
        long a = A[n];
        for ( int r = 0; r <= limit; r++ )
        {
            // R を使わない場合
            // R >= S/2 を求める時は、R で使わないものは B/G の二通り
            // あるので x2
            dp1[n + 1][r] = ( dp1[n + 1][r] + 2 * dp1[n][r] ) % MOD;
            // R=G=S/2 を求める時は、R で使わないものは全部 G にするので
            // x1
            dp2[n + 1][r] = ( dp2[n + 1][r] + 1 * dp2[n][r] ) % MOD;

            if ( limit < r + a )
            {
                // S/2 を超えるものをカウントするのは R >= S/2 を求める時だけ。
                // R=G=S/2 の場合は S/2 を超えるものは必要ない
                dp1[n + 1][limit] = ( dp1[n + 1][limit] + dp1[n][r] ) % MOD;
            }
            else
            {
                // 今回の a を利用して S/2 以下になるものをカウントする
                dp1[n + 1][r + a] = ( dp1[n + 1][r + a] + dp1[n][r] ) % MOD;
                dp2[n + 1][r + a] = ( dp2[n + 1][r + a] + dp2[n][r] ) % MOD;
            }
        }
    }

    // 全ての塗り方は 3^N 通り。そこから R/G/B のどれかが S/2
    // 以上になる場合を引く。 dp1 は R が S/2 以上になる場合だが、G, B
    // も同じ通りあるので、x3 している。
    long ans = ( pow_mod( 3, N, MOD ) - 3 * dp1[N][limit] ) % MOD;

    if ( ans < 0 ) ans = ( ans + MOD ) % MOD;

    // S が 2 の倍数の時だけ (R,G,B) = (S/2,S/2,0) (S/2,0,S/2) (0,S/2,S/2)
    // となる可能性があり、これは上の 3*dp1[N][limit] でそれぞれ一回ずつ重複して
    // 覗かれている。つまり、(R,G,B) = (S/2,S/2,0) となる場合 (dp2[N][limit]x3)
    // だけ無駄に取り除かれているのでそれを補正する。
    if ( S % 2 == 0 ) ans = ( ans + 3 * dp2[N][limit] ) % MOD;

    cout << ans << endl;

    return 0;
}
