#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

#define MAX_V 10000

using namespace std;

typedef pair<int, int> P;

vector<int> G[MAX_V];
int C[MAX_V];

int assign[MAX_V];

void dfsCalcEdgeCost( int v, int parent, int &cidx )
{
    assign[v] = C[cidx++];

    for ( auto to : G[v] )
    {
        if ( to == parent ) continue;

        dfsCalcEdgeCost( to, v, cidx );
    }
}

long long calcCost( int v, int parent )
{
    long long cost = 0;
    for ( auto to : G[v] )
    {
        if ( to == parent ) continue;

        cost += min( assign[to], assign[v] );
        cost += calcCost( to, v );
    }
    return cost;
}

int main( int argc, char **argv )
{
    // input
    int N;
    cin >> N;

    for ( int i = 0; i < N - 1; i++ )
    {
        int a, b;
        cin >> a >> b;

        G[a - 1].push_back( b - 1 );
        G[b - 1].push_back( a - 1 );
    }

    for ( int i = 0; i < N; i++ ) cin >> C[i];

    // solve
    sort( C, C + N, [&]( int a, int b ) { return a > b; } );

    int cidx = 0;
    dfsCalcEdgeCost( 0, -1, cidx );

    long long cost = calcCost( 0, -1 );
    cout << cost << endl;

    for ( int i = 0; i < N - 1; i++ ) cout << assign[i] << " ";
    cout << assign[N - 1] << endl;

    return 0;
}
