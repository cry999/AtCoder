#include <algorithm>
#include <iostream>
#include <queue>
#include <tuple>
#include <vector>

using namespace std;

#define MAX_N 200000

int N;
vector<int> tree[MAX_N];

int diameter()
{
    int root = 0;
    int max_depth = 0;

    queue<tuple<int, int, int>> q;
    q.push( make_tuple( root, -1, 0 ) );

    while ( !q.empty() )
    {
        auto e = q.front();
        q.pop();

        int vert = get<0>( e );
        int prev = get<1>( e );
        int dept = get<2>( e );

        for ( auto t : tree[vert] )
        {
            if ( t == prev ) continue;

            q.push( make_tuple( t, vert, dept + 1 ) );
        }

        root = vert;
    }

    q.push( make_tuple( root, -1, 0 ) );

    while ( !q.empty() )
    {
        auto e = q.front();
        q.pop();

        int vert = get<0>( e );
        int prev = get<1>( e );
        int dept = get<2>( e );

        for ( auto t : tree[vert] )
        {
            if ( t == prev ) continue;

            q.push( make_tuple( t, vert, dept + 1 ) );
        }

        max_depth = max( max_depth, dept );
    }

    return max_depth;
}

int main( int argc, char **argv )
{
    cin >> N;

    for ( int n = 0; n < N - 1; n++ )
    {
        int a, b;
        cin >> a >> b;

        tree[a - 1].push_back( b - 1 );
        tree[b - 1].push_back( a - 1 );
    }

    int L = diameter();

    if ( L % 3 == 1 )
        cout << "Second" << endl;
    else
        cout << "First" << endl;

    return 0;
}
