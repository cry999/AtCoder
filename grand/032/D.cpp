#include <cstring>
#include <iostream>

using namespace std;

#define MAX_N 5000
#define INF 0x3f3f3f3f3f3f3f3f

long dp[MAX_N + 1][MAX_N + 1];
int x0[MAX_N + 1], P[MAX_N];

long rotation_sort( int N, int A, int B )
{
    for ( int i = 0; i < N; i++ ) x0[P[i]] = i;

    memset( dp, INF, sizeof( dp ) );
    memset( dp[0], 0, sizeof( dp[0] ) );

    for ( int k = 1; k <= N; k++ )
    {
        long min_prev = INF;

        for ( int x = 0; x <= N; x++ )
        {
            int cost;
            if ( x == x0[k] )
                cost = 0;
            else if ( x < x0[k] )
                cost = B;
            else
                cost = A;

            min_prev = min( min_prev, dp[k - 1][x] );
            dp[k][x] = min_prev + cost;
        }
    }

    long ans = INF;
    for ( auto v : dp[N] ) ans = min( ans, v );

    return ans;
}

int main( int argc, char **argv )
{
    long N, A, B;
    cin >> N >> A >> B;

    for ( int i = 0; i < N; i++ ) cin >> P[i];

    cout << rotation_sort( N, A, B ) << endl;

    return 0;
}
