#include <algorithm>
#include <iostream>
#include <vector>

#define MAX_N 5000
#define INF ( 1LL << 60 )

using namespace std;

struct Edge
{
    int to, cost;
};

int N;
vector<Edge> G[MAX_N];

int treeSize[MAX_N];
long long dp[MAX_N][MAX_N];

int initTreeSize( int node, int parent )
{
    for ( auto e : G[node] )
    {
        if ( e.to == parent ) continue;

        treeSize[node] += initTreeSize( e.to, node );
    }

    return ++treeSize[node];
}

int solve( int node, int parent, long long h, vector<vector<long long>> &a )
{
    vector<vector<long long>> v;
    for ( auto e : G[node] )
    {
        if ( e.to == parent ) continue;

        solve( e.to, node, e.cost, v );
    }

    vector<long long> tmp( 1, 0 );
    int sz = v.size();
    for ( int i = 0; i < sz; i++ )
    {
        int s = tmp.size();
        int t = v[i].size();
        vector<long long> ntmp( s + t - 1, 1LL << 60 );
        for ( int j = 0; j < s; j++ )
        {
            for ( int k = 0; k < t; k++ )
                ntmp[j + k] = min( ntmp[j + k], tmp[j] + v[i][k] );
        }

        tmp = ntmp;
        int idx = upper_bound( tmp.begin(), tmp.end(), h ) - tmp.begin();
        tmp.resize( idx );
    }

    int idx = upper_bound( tmp.begin(), tmp.end(), h ) - tmp.begin();
    tmp.resize( idx + 1 );
    tmp[idx] = h;

    a.push_back( tmp );
    return tmp.size();
}

int main( int argc, char **argv )
{
    // input
    cin >> N;
    for ( int i = 0; i < N - 1; i++ )
    {
        int p, H;
        cin >> p >> H;

        G[i + 1].push_back( {p, H} );
        G[p].push_back( {i + 1, H} );
    }

    // initialize
    initTreeSize( 0, -1 );
    for ( int i = 0; i < N; i++ )
        for ( int j = 0; j < N; j++ ) dp[i][j] = 1LL << 60;

    // solve
    vector<vector<long long>> tmp;
    cout << solve( 0, -1, 1LL << 60, tmp ) - 1 << endl;

    return 0;
}
