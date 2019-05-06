#include <cstring>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define SIZE 2000

typedef pair<int, int> P;

vector<int> tree[SIZE];
int parents[SIZE][SIZE];
int id[SIZE][SIZE];
int ans;

void dfs( int v, int parent, int root )
{
    parents[root][v] = parent;

    for ( auto to : tree[v] )
    {
        if ( to == parent ) continue;
        dfs( to, v, root );
    }
}

void dfs2( int v, int parent, int b )
{
    if ( id[b][v] == v )
    {
        ans++;
        b = v;
    }

    for ( auto to : tree[v] )
    {
        if ( to == parent ) continue;
        dfs2( to, v, b );
    }
}

void add( int a, int b )
{
    if ( id[a][b] == b || id[b][a] == a ) return;

    if ( id[a][b] != -1 )
    {
        add( id[a][b], b );
        return;
    }

    if ( id[b][a] != -1 )
    {
        add( id[b][a], a );
        return;
    }

    id[a][b] = b, id[b][a] = a;

    vector<P> nxt;
    queue<int> que;

    que.push( b );
    while ( !que.empty() )
    {
        int v = que.front();
        que.pop();

        for ( auto to : tree[v] )
        {
            if ( to == parents[a][v] ) continue;

            if ( id[a][to] != -1 )
                nxt.push_back( P( to, b ) );
            else
            {
                id[a][to] = b;
                que.push( to );
            }
        }
    }

    que.push( a );
    while ( !que.empty() )
    {
        int v = que.front();
        que.pop();

        for ( auto to : tree[v] )
        {
            if ( to == parents[b][v] ) continue;

            if ( id[b][to] != -1 )
                nxt.push_back( P( to, a ) );
            else
            {
                id[b][to] = a;
                que.push( to );
            }
        }
    }

    for ( auto e : nxt ) add( e.first, e.second );
}

int main( int argc, char **argv )
{
    int N, M;
    cin >> N >> M;

    for ( int n = 0; n < N - 1; n++ )
    {
        int a, b;
        cin >> a >> b;

        tree[a - 1].push_back( b - 1 );
        tree[b - 1].push_back( a - 1 );
    }

    for ( int i = 0; i < N; i++ ) dfs( i, -1, i );

    memset( id, -1, sizeof( id ) );

    for ( int m = 0; m < M; m++ )
    {
        int c, d;
        cin >> c >> d;

        add( c - 1, d - 1 );
    }

    ans = 0;
    for ( int i = 0; i < N; i++ )
        for ( auto to : tree[i] ) dfs2( to, i, i );

    cout << ( ans >> 1 ) << endl;

    return 0;
}
