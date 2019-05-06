#include <algorithm>
#include <iostream>

using namespace std;

#define MAX_N 365
#define MAX_M 365

long dp[MAX_N][MAX_M];
long A[MAX_N];

int main( int argc, char **argv )
{
    int N, M, K;
    cin >> N >> M >> K;

    A[0] = -1;
    for ( int n = 0; n < N; n++ ) cin >> A[n + 1];

    long ans = 0;
    if ( K * ( M + 1 ) - 1 < N )
        ans = -1;
    else
    {
        for ( int m = 0; m < M; m++ )
        {
            int min_n = max( m, N - ( M - m ) * K ) + 1;
            int max_n = min( N - ( M - m ), K * ( m + 1 ) - 1 ) + 1;

            for ( int n = min_n; n <= max_n; n++ )
                for ( int nn = max( 0, n - K ); nn < n; nn++ )
                    dp[m + 1][n] = max( dp[m][nn] + A[n], dp[m + 1][n] );
        }

        for ( int n = 1; n <= N; n++ ) ans = max( ans, dp[M][n] );
    }

    cout << ans << endl;

    return 0;
}
