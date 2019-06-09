#include <cstring>
#include <iostream>
#include <vector>

#define MAX_N 80

using namespace std;

namespace graph
{
struct Edge
{
    int to, cap, rev;
};

template <int V>
struct Graph
{
private:
    vector<Edge> G[V];
    bool used[V];

public:
    void addEdge( int from, int to, int cap )
    {
        G[from].push_back( {to, cap, (int)G[to].size()} );
        G[to].push_back( {from, 0, (int)G[from].size() - 1} );
    }

private:
    int dfs( int v, int t, int f )
    {
        if ( v == t ) return f;

        used[v] = true;

        for ( auto &e : G[v] )
        {
            if ( !used[e.to] && e.cap > 0 )
            {
                int d = dfs( e.to, t, min( f, e.cap ) );

                if ( d > 0 )
                {
                    e.cap -= d;
                    G[e.to][e.rev].cap += d;

                    return d;
                }
            }
        }
        return 0;
    }

public:
    int maxFlow( int s, int t )
    {
        int flow = 0;
        for ( ;; )
        {
            memset( used, 0, sizeof( used ) );
            int f = dfs( s, t, INT32_MAX );
            if ( f == 0 ) return flow;
            flow += f;
        }
    }
};
} // namespace graph

using Graph = graph::Graph<MAX_N * MAX_N + 2>;

int main( int argc, char **argv )
{
    int N;
    cin >> N;

    vector<int> P( N );
    for ( int i = 0; i < N; i++ )
    {
        cin >> P[i];
        P[i]--;
    }

    vector<int> A( N );
    for ( int i = 0; i < N; i++ ) cin >> A[i];

    int s = N * N;
    int t = N * N + 1;
    auto index = [&]( int i, int j ) {
        if ( j < 0 || N <= j ) return s;
        if ( i < 0 || N <= i ) return t;
        return i * N + j;
    };

    Graph g;
    for ( int i = 0; i < N; i++ )
    {
        for ( int j = 0; j < N; j++ )
        {
            if ( j == P[i] ) continue;

            int from = index( i, ( j < P[i] ) ? ( j - 1 ) : ( j + 1 ) );
            int to = index( i, j );
            int cap = ( abs( P[i] - j ) + A[i] - 1 ) / A[i];

            g.addEdge( from, to, cap );
            g.addEdge( to, from, INT32_MAX );
        }

        for ( int j = 0; j < N; j++ )
        {
            if ( j == i ) continue;

            int from = index( j, P[i] );
            int to = index( ( j < i ) ? ( j - 1 ) : ( j + 1 ), P[i] );
            int cap = ( abs( i - j ) + A[i] - 1 ) / A[i];

            g.addEdge( from, to, cap );
            g.addEdge( to, from, INT32_MAX );
        }
    }

    cout << g.maxFlow( s, t ) << endl;

    return 0;
}
