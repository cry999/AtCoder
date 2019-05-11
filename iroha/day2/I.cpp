#include <cstring>
#include <iostream>
#include <queue>

using namespace std;

typedef pair<int, int> point;
typedef pair<int64_t, point> entry;

#define MAX_H 500
#define MAX_W 500
#define MAX_X ( MAX_H * MAX_W ) - 2

#define INF 1L << 60;

int A[MAX_H][MAX_W];
int64_t C[MAX_X + 1];

int64_t dp[MAX_H][MAX_W];

int dX[4] = {1, -1, 0, 0};
int dY[4] = {0, 0, 1, -1};

int main( int argc, char **argv )
{
    // inputs
    int H, W, X;
    cin >> H >> W >> X;

    int sx, sy;
    cin >> sx >> sy;
    sx--, sy--;

    int gx, gy;
    cin >> gx >> gy;
    gx--, gy--;

    for ( int h = 0; h < H; h++ )
        for ( int w = 0; w < W; w++ ) cin >> A[h][w];

    C[0] = 0;
    for ( int x = 0; x < X; x++ ) cin >> C[x + 1];

    // likely dijkstra
    for ( int h = 0; h < H; h++ )
        for ( int w = 0; w < W; w++ ) dp[h][w] = INF;

    dp[sx][sy] = 0;

    priority_queue<entry> q;
    q.push( entry( -dp[sx][sy], point( sx, sy ) ) );

    while ( !q.empty() )
    {
        int x = q.top().second.first;
        int y = q.top().second.second;
        q.pop();

        int idx = A[x][y];

        for ( int i = 0; i < 4; i++ )
        {
            int nx = x + dX[i];
            int ny = y + dY[i];

            if ( nx < 0 || H <= nx ) continue;
            if ( ny < 0 || W <= ny ) continue;

            int nidx = A[nx][ny];
            int64_t cost = ( idx == nidx ) ? 0 : C[nidx];
            int64_t alt = dp[x][y] + cost;

            if ( alt < dp[nx][ny] )
            {
                dp[nx][ny] = alt;
                if ( ( nx != gx || ny != gy ) && ( dp[nx][ny] < dp[gx][gy] ) )
                    q.push( entry( -dp[nx][ny], point( nx, ny ) ) );
            }
        }
    }

    cout << dp[gx][gy] << endl;

    return 0;
}
