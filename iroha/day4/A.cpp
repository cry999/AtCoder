#include <algorithm>
#include <cstring>
#include <iostream>
#include <set>
#include <stack>
#include <vector>

#define MAX_ROUND 100

using namespace std;

int N, A, B, C, D;
int a[MAX_ROUND], b[MAX_ROUND], c[MAX_ROUND], d[MAX_ROUND];

bool memo[MAX_ROUND + 1][MAX_ROUND + 1][MAX_ROUND + 1][MAX_ROUND + 1];
bool visited[MAX_ROUND + 1][MAX_ROUND + 1][MAX_ROUND + 1][MAX_ROUND + 1];
stack<int> st;

int max4( int a, int b, int c, int d )
{
    return max( max( a, b ), max( c, d ) );
}

vector<int> v = {1, 2, 3};

bool ok( int a, int b, int c )
{
    vector<int> t = {a, b, c};
    sort( t.begin(), t.end() );
    return v == t;
}

bool dfs( int ai, int bi, int ci, int di )
{
    if ( ai == A && bi == B && ci == C && di == D ) return true;
    if ( visited[ai][bi][ci][di] ) return memo[ai][bi][ci][di];
    visited[ai][bi][ci][di] = true;

    int ar = ai == A ? 4 : a[ai];
    int br = bi == B ? 4 : b[bi];
    int cr = ci == C ? 4 : c[ci];
    int dr = di == D ? 4 : d[di];

    if ( ok( br, cr, dr ) && dfs( ai, bi + 1, ci + 1, di + 1 ) )
    {
        st.push( 1 );
        return memo[ai][bi][ci][di] = true;
    }

    if ( ok( ar, cr, dr ) && dfs( ai + 1, bi, ci + 1, di + 1 ) )
    {
        st.push( 2 );
        return memo[ai][bi][ci][di] = true;
    }

    if ( ok( ar, br, dr ) && dfs( ai + 1, bi + 1, ci, di + 1 ) )
    {
        st.push( 3 );
        return memo[ai][bi][ci][di] = true;
    }

    if ( ok( ar, br, cr ) && dfs( ai + 1, bi + 1, ci + 1, di ) )
    {
        st.push( 4 );
        return memo[ai][bi][ci][di] = true;
    }

    return memo[ai][bi][ci][di];
}

int main( int argc, char **argv )
{
    cin >> N >> A >> B >> C >> D;

    for ( int i = 0; i < A; i++ ) cin >> a[i];
    for ( int i = 0; i < B; i++ ) cin >> b[i];
    for ( int i = 0; i < C; i++ ) cin >> c[i];
    for ( int i = 0; i < D; i++ ) cin >> d[i];

    if ( A + B + C + D != 3 * N || !dfs( 0, 0, 0, 0 ) )
        cout << "No" << endl;
    else
    {
        cout << "Yes" << endl;
        while ( !st.empty() )
        {
            cout << st.top() << endl;
            st.pop();
        }
    }

    return 0;
}
