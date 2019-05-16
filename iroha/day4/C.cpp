#include <bitset>
#include <iostream>
#include <vector>

using namespace std;

typedef pair<int, string> P;

int main( int argc, char **argv )
{
    string S;
    cin >> S;

    vector<P> SS;
    int c = 0;

    SS.push_back( P( c, S ) );

    for ( int i = 2; i < S.length(); i <<= 1 )
    {
        string nextS = "";
        for ( int j = 0; j < S.length(); j++ )
        {
            if ( j < i )
                nextS += S[j];
            else
                nextS += S[j] == S[j - i] ? "0" : "1";
        }

        if ( nextS > S )
        {
            c += i;
            S = nextS;
            SS.push_back( P( c, S ) );
        }
    }

    int M;
    cin >> M;

    for ( int m = 0; m < M; m++ )
    {
        long long x;
        string s;
        cin >> x >> s;

        int l = 0, r = SS.size();
        while ( r - l > 1 )
        {
            int m = ( l + r ) / 2;
            if ( SS[m].first <= x )
                l = m;
            else
                r = m;
        }

        if ( SS[l].second <= s )
        {
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;

    return 0;
}
