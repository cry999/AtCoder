#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

typedef pair<int, int> P;

int main( int argc, char **argv )
{
    int N;
    cin >> N;

    priority_queue<P, vector<P>, greater<P>> que;
    for ( int i = 0; i < N; i++ )
    {
        int s, t;
        cin >> s >> t;

        que.push( P( s, t ) );
    }

    int cs = 0;
    int ct = 0;
    int ans = 0;

    while ( !que.empty() )
    {
        int s = que.top().first;
        int t = que.top().second;
        que.pop();

        if ( cs <= s && s <= ct )
            ct = max( ct, t );
        else
        {
            ans++;
            cs = s;
            ct = t;
        }
    }

    cout << ans << endl;

    return 0;
}
