#include <bitset>
#include <iostream>

#define MAX_N 2000

using namespace std;

bitset<MAX_N> dpl[MAX_N];
bitset<MAX_N> dpr[MAX_N];

bitset<MAX_N> A[MAX_N];

int main( int argc, char **argv )
{
    // input
    int N;
    cin >> N;

    for ( int i = 1; i < N; i++ )
    {
        string S;
        cin >> S;

        for ( int j = 0; j < i; j++ )
        {
            if ( S[j] == '1' )
                A[i][j] = true;
            else
                A[j][i] = true;
        }
    }

    for ( int i = 0; i < N; i++ ) dpl[i][i] = dpr[i][i] = true;

    // solve
    for ( int d = 0; d < N; d++ )
    {
        for ( int i = 0; i + d < N; i++ )
        {
            int j = i + d;
            if ( ( dpl[j - 1] & dpr[i] & A[j] ).any() ) dpr[i][j] = 1;
            if ( ( dpl[j] & dpr[i + 1] & A[i] ).any() ) dpl[j][i] = 1;
        }
    }

    int ans = ( dpl[N - 1] & dpr[0] ).count();
    cout << ans << endl;

    return 0;
}
