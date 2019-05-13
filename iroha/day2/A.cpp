#include <algorithm>
#include <cstring>
#include <iostream>
#include <string>

using namespace std;

#define MAX_LEN 5000

int lcs[MAX_LEN + 1][MAX_LEN + 1];

int main( int argc, char **argv )
{
    memset( lcs, 0, sizeof( lcs ) );

    string S, T;
    cin >> S;
    cin >> T;

    for ( int i = 0; i < S.length(); i++ )
    {
        for ( int j = 0; j < T.length(); j++ )
        {
            if ( S[i] == T[j] )
                lcs[i + 1][j + 1] = lcs[i][j] + 1;
            else
                lcs[i + 1][j + 1] = max( lcs[i][j + 1], lcs[i + 1][j] );
        }
    }

    cout << lcs[S.length()][T.length()] + 1 << endl;

    return 0;
}
