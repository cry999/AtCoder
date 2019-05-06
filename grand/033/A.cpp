#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

#define MAX_H 1000
#define MAX_W 1000

typedef pair<int, int> point;

char A[MAX_H][MAX_W];
bool visited[MAX_H][MAX_W];
pair<int, int> dirs[4] = {make_pair( 0, 1 ), make_pair( 0, -1 ),
                          make_pair( 1, 0 ), make_pair( -1, 0 )};

int main( int argc, char **argv )
{
    int H, W;
    cin >> H >> W;

    auto q = priority_queue<pair<int, point>>();

    for ( int h = 0; h < H; h++ )
    {
        cin >> A[h];
        for ( int w = 0; w < W; w++ )
            if ( A[h][w] == '#' ) q.push( make_pair( 0, make_pair( h, w ) ) );
    }

    int ans = 0;
    int count = 0;
    while ( count < H * W )
    {
        auto e = q.top();
        q.pop();

        int c = e.first, h = e.second.first, w = e.second.second;
        // cout << "(" << h << ", " << w << ") " << c << endl;
        if ( visited[h][w] ) continue;

        ans = c;
        visited[h][w] = true;
        count++;

        for ( auto d : dirs )
        {
            int dh = d.first, dw = d.second;
            int nh = h + dh, nw = w + dw;

            if ( nh < 0 or H <= nh ) continue;
            if ( nw < 0 or W <= nw ) continue;
            if ( visited[nh][nw] ) continue;

            q.push( make_pair( c - 1, make_pair( nh, nw ) ) );
        }
    }

    cout << -ans << endl;

    return 0;
}
