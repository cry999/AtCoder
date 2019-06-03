#include <iostream>
#include <vector>

#define MAX_N 1000

using namespace std;

namespace graph
{
struct Edge
{
    long long to, cap, cost, rev;
};

template <int MAX_V>
struct Graph
{
private:
    vector<Edge> G[MAX_V];
    long long dist[MAX_V];
    long long prevv[MAX_V];
    long long preve[MAX_V];

    int V;
    const long long INF = ( 1LL << 60 );

public:
    Graph( int V ) : V( V ) {}

    void addEdge( long long from, long long to, long long cap, long long cost )
    {
        G[from].push_back( ( Edge ){to, cap, cost, (long long)G[to].size()} );
        G[to].push_back(
            ( Edge ){from, 0, -cost, (long long)G[from].size() - 1} );
    }

    long long minCostFlow( long long s, long long t, long long f )
    {
        long long res = 0;
        while ( f > 0 )
        {
            fill( dist, dist + V, INF );
            dist[s] = 0;

            bool update = true;
            while ( update )
            {
                update = false;
                for ( int v = 0; v < V; v++ )
                {
                    if ( dist[v] == INF ) continue;

                    for ( int i = 0; i < G[v].size(); i++ )
                    {
                        Edge &e = G[v][i];
                        if ( e.cap > 0 && dist[e.to] > dist[v] + e.cost )
                        {
                            dist[e.to] = dist[v] + e.cost;
                            prevv[e.to] = v;
                            preve[e.to] = i;
                            update = true;
                        }
                    }
                }
            }

            if ( dist[t] == INF ) return -1;

            long long d = f;
            for ( int v = t; v != s; v = prevv[v] )
                d = min( d, G[prevv[v]][preve[v]].cap );

            f -= d;
            res += d * dist[t];

            for ( int v = t; v != s; v = prevv[v] )
            {
                Edge &e = G[prevv[v]][preve[v]];
                e.cap -= d;
                G[v][e.rev].cap += d;
            }
        }

        return res;
    }
};

} // namespace graph

using G = graph::Graph<1 + MAX_N + 4 + MAX_N + 1>;

int main( int argc, char **argv )
{
    const long long INF = ( 1LL << 60 );

    int N;
    cin >> N;

    const int TYPE1 = N + 1;
    const int TYPE2 = N + 2;
    const int TYPE3 = N + 3;
    const int TYPE4 = N + 4;

    G g( 1 + N + 4 + N + 1 );
    int s = 0;                     // Graph の始点
    int t = 1 + N + 4 + N + 1 - 1; // Graph の終点

    int offset = 1;
    int numBall = 0;
    for ( int i = 0; i < N; i++ )
    {
        int RX, RY, RC;
        cin >> RX >> RY >> RC;

        // 始点から各赤ボールへの辺を引く
        g.addEdge( s, i + offset, RC, 0 );

        // 各赤ボールからそれぞれのタイプへの辺を引く
        g.addEdge( i + offset, TYPE1, INF, -( RX + RY ) );  // type 1
        g.addEdge( i + offset, TYPE2, INF, -( -RX + RY ) ); // type 2
        g.addEdge( i + offset, TYPE3, INF, -( RX - RY ) );  // type 3
        g.addEdge( i + offset, TYPE4, INF, -( -RX - RY ) ); // type 4

        numBall += RC;
    }

    offset = 1 + N + 4;
    for ( int i = 0; i < N; i++ )
    {
        int BX, BY, BC;
        cin >> BX >> BY >> BC;

        // 各タイプから青ボールへの辺を引く
        g.addEdge( TYPE1, i + offset, INF, -( -BX - BY ) ); // type 1
        g.addEdge( TYPE2, i + offset, INF, -( BX - BY ) );  // type 2
        g.addEdge( TYPE3, i + offset, INF, -( -BX + BY ) ); // type 3
        g.addEdge( TYPE4, i + offset, INF, -( BX + BY ) );  // type 4

        // 各青ボールから終点へ辺を引く。
        g.addEdge( i + offset, t, BC, 0 );
    }

    cout << -g.minCostFlow( s, t, numBall ) << endl;

    return 0;
}
