#include <iostream>
#include <queue>
#include <set>

using namespace std;

typedef pair<int, int> P;
typedef pair<int, P> event_t;

int main( int argc, char **argv )
{
    //
    int N, Q;
    cin >> N >> Q;

    priority_queue<event_t, vector<event_t>, greater<event_t>> que;
    for ( int i = 0; i < N; i++ )
    {
        int S, T, X;
        cin >> S >> T >> X;

        que.push( event_t( S - X, P( 1, X ) ) );
        que.push( event_t( T - X, P( -1, X ) ) );
    }

    set<int> set;

    for ( int i = 0; i < Q; i++ )
    {
        int D;
        cin >> D;

        while ( !que.empty() && que.top().first <= D )
        {
            event_t e = que.top();
            que.pop();

            int type = e.second.first;
            int X = e.second.second;

            if ( type == 1 )
                set.insert( X );
            else
                set.erase( X );
        }

        if ( !set.empty() )
            cout << *set.begin() << endl;
        else
            cout << -1 << endl;
    }

    return 0;
}
