#include <algorithm>
#include <cstring>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

#define MAX_N 100000
#define MAX_M 100000

using namespace std;

int N, M, Q;
string S, T;

int lowerX[MAX_M];
int upperX[MAX_M];
int lowerY[MAX_N];
int upperY[MAX_N];

void initCompress()
{
    int le = N;
    int lw = N;
    for ( int i = 0; i < N; i++ )
    {
        if ( S[i] == 'E' ) le = i;
        if ( S[i] == 'W' ) lw = i;

        lowerY[i] = min( ( S[i] == 'E' ? lw : le ), i );
    }

    int ue = -1;
    int uw = -1;
    for ( int i = N - 1; i >= 0; i-- )
    {
        if ( S[i] == 'E' ) ue = i;
        if ( S[i] == 'W' ) uw = i;

        upperY[i] = max( ( S[i] == 'E' ? uw : ue ), i );
    }

    int ln = N;
    int ls = N;
    for ( int i = 0; i < M; i++ )
    {
        if ( T[i] == 'N' ) ln = i;
        if ( T[i] == 'S' ) ls = i;

        lowerX[i] = min( ( T[i] == 'N' ? ls : ln ), i );
    }

    int un = -1;
    int us = -1;
    for ( int i = M - 1; i >= 0; i-- )
    {
        if ( T[i] == 'N' ) un = i;
        if ( T[i] == 'S' ) us = i;

        upperX[i] = max( ( T[i] == 'N' ? us : un ), i );
    }
}

bool visited[6][6];

typedef pair<int, int> P2;
typedef pair<int, P2> P3;

int query( int y1, int x1, int y2, int x2 )
{
    vector<int> X;
    vector<int> Y;

    memset( visited, 0, sizeof( visited ) );

    // initialize X
    X.push_back( x1 );
    X.push_back( lowerX[x1] );
    X.push_back( upperX[x1] );
    X.push_back( x2 );
    X.push_back( lowerX[x2] );
    X.push_back( upperX[x2] );

    sort( X.begin(), X.end() );
    X.erase( unique( X.begin(), X.end() ), X.end() );

    // initialize Y
    Y.push_back( y1 );
    Y.push_back( lowerY[y1] );
    Y.push_back( upperY[y1] );
    Y.push_back( y2 );
    Y.push_back( lowerY[y2] );
    Y.push_back( upperY[y2] );

    sort( Y.begin(), Y.end() );
    Y.erase( unique( Y.begin(), Y.end() ), Y.end() );

    int scx = find( X.begin(), X.end(), x1 ) - X.begin(); // index of start x
    int scy = find( Y.begin(), Y.end(), y1 ) - Y.begin(); // index of start y
    int gcx = find( X.begin(), X.end(), x2 ) - X.begin(); // index of goal x
    int gcy = find( Y.begin(), Y.end(), y2 ) - Y.begin(); // index of goal y

    priority_queue<P3> q;
    q.push( P3( 0, P2( scx, scy ) ) );

    while ( !q.empty() )
    {
        int d = q.top().first;
        int cxi = q.top().second.first;
        int cyi = q.top().second.second;

        q.pop();

        if ( visited[cxi][cyi] ) continue;
        visited[cxi][cyi] = true;

        if ( cxi == gcx && cyi == gcy ) return d;

        int x = X[cxi];
        int y = Y[cyi];

        if ( T[x] == 'N' && 0 <= cyi - 1 )
        {
            int ny = Y[cyi - 1];
            q.push( P3( d + abs( ny - y ), P2( cxi, cyi - 1 ) ) );
        }
        else if ( T[x] == 'S' && cyi + 1 < Y.size() )
        {
            int ny = Y[cyi + 1];
            q.push( P3( d + abs( ny - y ), P2( cxi, cyi + 1 ) ) );
        }

        if ( S[y] == 'W' && 0 <= cxi - 1 )
        {
            int nx = X[cxi - 1];
            q.push( P3( d + abs( nx - x ), P2( cxi - 1, cyi ) ) );
        }
        else if ( S[y] == 'E' && cxi + 1 < X.size() )
        {
            int nx = X[cxi + 1];
            q.push( P3( d + abs( nx - x ), P2( cxi + 1, cyi ) ) );
        }
    }

    return -1;
}

int main( int argc, char **argv )
{
    cin >> N >> M >> Q;
    cin >> S;
    cin >> T;

    initCompress();

    for ( int q = 0; q < Q; q++ )
    {
        int a, b, c, d;
        cin >> a >> b >> c >> d;

        int ans = query( a - 1, b - 1, c - 1, d - 1 );
        cout << ans << endl;
    }

    return 0;
}
