#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main( int argc, char **argv )
{
    int H, W;
    cin >> H >> W;

    vector<vector<int>> A( H, vector<int>( W, 0 ) );
    vector<vector<int>> B( H, vector<int>( W, 0 ) );

    for ( int h = 0; h < H; h++ )
        for ( int w = 0; w < W; w++ ) cin >> A[h][w];

    for ( int h = 0; h < H; h++ )
        for ( int w = 0; w < W; w++ ) cin >> B[h][w];

    int M = 80 * ( H + W - 1 );

    vector<vector<vector<bool>>> dp(
        H, vector<vector<bool>>( W, vector<bool>( M + 1, false ) ) );

    dp[0][0][abs( A[0][0] - B[0][0] )] = true;

    for ( int h = 0; h < H; h++ )
    {
        for ( int w = 0; w < W; w++ )
        {
            for ( int k = 0; k <= M; k++ )
            {
                if ( !dp[h][w][k] ) continue;

                if ( h + 1 < H )
                {
                    int s0 = abs( A[h + 1][w] - B[h + 1][w] );
                    int s1 = abs( k + s0 );
                    int s2 = abs( k - s0 );

                    if ( s1 < M + 1 ) dp[h + 1][w][s1] = true;
                    if ( s2 < M + 1 ) dp[h + 1][w][s2] = true;
                }

                if ( w + 1 < W )
                {
                    int s0 = abs( A[h][w + 1] - B[h][w + 1] );
                    int s1 = abs( k + s0 );
                    int s2 = abs( k - s0 );

                    if ( s1 < M + 1 ) dp[h][w + 1][s1] = true;
                    if ( s2 < M + 1 ) dp[h][w + 1][s2] = true;
                }
            }
        }
    }

    for ( int k = 0; k <= M; k++ )
    {
        if ( dp[H - 1][W - 1][k] )
        {
            cout << k << endl;
            break;
        }
    }

    return 0;
}
