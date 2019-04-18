#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

#define MAX_K 50
#define MAX_W 10000

long long dp[MAX_K+1][MAX_W+1];

int main( int argc, char **argv )
{
    int W, N, K;

    cin >> W;
    cin >> N >> K;

    memset( dp, 0, sizeof( dp ) );

    long long ans = 0;
    for ( int _ = 0; _ < N; _++ )
    {
        int A, B;
        cin >> A >> B;

        for ( int k = K; k > 0; k-- )
        {
            for ( int w = W; w >= 0; w-- )
            {
                if ( A <= w ) dp[k][w] = max( dp[k][w], dp[k - 1][w - A] + B );
                ans = max( ans, dp[k][w] );
            }
        }
    }

    cout << ans << endl;

    return 0;
}
