#include <iostream>

#define MAX_LEN 1 << 19

using namespace std;

int main( int argc, char **argv )
{
    int M, K;
    cin >> M >> K;

    if ( M == 1 )
    {
        if ( K == 0 )
            cout << "0 0 1 1" << endl;
        else
            cout << -1 << endl;
    }
    else if ( K < ( 1 << M ) )
    {
        for ( int i = 0; i < ( 1 << M ); i++ )
        {
            if ( i != K ) cout << i << " ";
        }
        cout << K << " ";
        for ( int i = ( 1 << M ) - 1; i >= 0; i-- )
        {
            if ( i != K ) cout << i << " ";
        }
        cout << K << endl;
    }
    else
    {
        cout << -1 << endl;
    }
    return 0;
}
