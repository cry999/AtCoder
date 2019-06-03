#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

#define MAX_N 2000

using namespace std;

typedef pair<int, int> P;

struct TreeDPElm
{
    // それぞれ、部分木内の
    // pieceNum: コマの個数
    // maxOpnum: 最大操作回数
    // minOpnum: 最小操作回数
    int pieceNum, maxOpnum, minOpnum;
};

int N;
string S;
vector<int> G[MAX_N];

TreeDPElm dp[MAX_N];

void dfs( int v, int par )
{
    TreeDPElm &thisDP = dp[v];

    thisDP.pieceNum = ( S[v] == '1' ) ? 1 : 0;
    thisDP.maxOpnum = 0;
    thisDP.minOpnum = 0;

    P tmp = P( 0, 0 );
    for ( auto u : G[v] )
    {
        if ( u == par ) continue;

        dfs( u, v );
        TreeDPElm e = dp[u];

        thisDP.pieceNum += e.pieceNum;
        thisDP.maxOpnum += e.maxOpnum + e.pieceNum;

        tmp = max( tmp, P( e.maxOpnum + e.pieceNum, e.minOpnum + e.pieceNum ) );
    }

    if ( tmp.second > thisDP.maxOpnum - tmp.first )
        thisDP.minOpnum = tmp.second - ( thisDP.maxOpnum - tmp.first );
    else
        thisDP.minOpnum = thisDP.maxOpnum & 1;
}

int main( int argc, char **argv )
{
    cin >> N;
    cin >> S;

    for ( int i = 0; i < N - 1; i++ )
    {
        int a, b;
        cin >> a >> b;

        G[a - 1].push_back( b - 1 );
        G[b - 1].push_back( a - 1 );
    }

    int ans = ( 1 << 30 );
    for ( int root = 0; root < N; root++ )
    {
        dfs( root, -1 );
        if ( dp[root].minOpnum == 0 ) ans = min( ans, dp[root].maxOpnum );
    }

    if ( ans == ( 1 << 30 ) )
        cout << -1 << endl;
    else
        cout << ans / 2 << endl;

    return 0;
}
