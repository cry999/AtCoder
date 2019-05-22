#include <iostream>
#include <set>

using namespace std;

int main( int argc, char **argv )
{
    int N, Q;
    cin >> N >> Q;

    set<long long> A;
    for ( int i = 0; i < N; i++ )
    {
        long long a;
        cin >> a;

        // if a is new value, add it into A
        if ( A.find( a ) == A.end() ) A.insert( a );
        // if a already exists, remove it from A
        else
            A.erase( a );
    }

    for ( int q = 0; q < Q; q++ )
    {
        long long L, R, X;
        cin >> L >> R >> X;

        long long res = 0;
        int count = 0;
        auto l = A.lower_bound( L );
        auto r = A.upper_bound( R );

        // query
        for ( auto it = l; it != r && it != A.end(); it++ )
        {
            auto a = *it;
            res ^= a;
            count++;
        }

        A.erase( l, r );

        // add new value X or not ?
        if ( count % 2 )
        {
            if ( A.find( X ) != A.end() )
            {
                // found
                A.erase( X );
            }
            else
            {
                // not found
                A.insert( X );
            }
        }
        cout << res << endl;
    }

    return 0;
}
