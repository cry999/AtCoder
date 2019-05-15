#include <iostream>
#include <string>

using namespace std;

const string ALPHABET = "abcdefghijklmnopqrstuvwxyz";

string query( char C, long long E )
{
    if ( E == 0 ) return C == 'a' ? "a" : "aa";

    string ans = "";
    for ( int N = 0; ( 1LL << N ) <= E; N++ )
    {
        if ( ( E % ( 1LL << N ) ) != 0 ) { continue; }

        long long S = E / ( 1LL << N );
        if ( S >= 26 ) { continue; }

        string tmp = "";

        int i = 0;
        while ( i < S && ALPHABET[i] < C ) tmp += ALPHABET[i++];

        for ( int n = 0; n < N; n++ ) tmp += C;

        while ( i++ < S ) tmp += ALPHABET[i];

        if ( ans == "" )
            ans = tmp;
        else
            ans = min( ans, tmp );
    }

    return ans == "" ? "-1" : ans;
}

int main( int argc, char **argv )
{
    int Q;
    cin >> Q;

    for ( int q = 0; q < Q; q++ )
    {
        char C;
        long long E;
        cin >> C >> E;

        string ans = query( C, E );
        cout << ans << endl;
    }
    return 0;
}
