#include <iostream>

using namespace std;

int pow( int a, int n )
{
    int res = 1;
    for ( int i = 0; i < n; i++ ) res *= a;
    return res;
}

bool ok( int m, int A )
{
    if ( m == 0 ) return false;
    if ( m == 1 ) return A == 0;

    for ( int c2 = 0; c2 <= 1; c2++ )
    {
        for ( int c3 = 0; c3 <= 4; c3++ )
        {
            for ( int c5 = 0; c5 <= 1; c5++ )
            {
                if ( m + 1 < ( 2 + 1 ) * c2 + ( 3 + 1 ) * c3 + ( 5 + 1 ) * c5 )
                    continue;

                int c4 = m;
                c4 -= ( 2 + 1 ) * c2;
                c4 -= ( 3 + 1 ) * c3;
                c4 -= ( 5 + 1 ) * c5;
                c4 = ( c4 + 1 ) / ( 4 + 1 );

                if ( c4 < 0 ) continue;

                if ( A - 2 * c4 >= 10 ) continue;
                if ( A - 2 * c4 < 0 ) return true;

                int t = ( 1 << ( A - 2 * c4 ) );
                int u = pow( 2, c2 ) * pow( 3, c3 ) * pow( 5, c5 );
                if ( t <= u ) return true;
            }
        }
    }

    return false;
}

int main( int argc, char **argv )
{
    int T;
    cin >> T;

    for ( int t = 0; t < T; t++ )
    {
        int L, A;
        cin >> L >> A;

        int l = 0, r = L + 1;
        while ( r - l > 1 )
        {
            int m = ( r + l ) / 2;
            if ( ok( m, A ) )
                r = m;
            else
                l = m;
        }

        cout << L - r + 1 << endl;
    }

    return 0;
}
