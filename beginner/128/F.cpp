#include <iostream>

#define MAX_N 100000

using namespace std;

long long s[MAX_N];

int main( int argc, char **argv )
{
    int N;
    cin >> N;

    for ( int i = 0; i < N; i++ ) cin >> s[i];

    long long ans = 0;
    for ( int C = 1; C < N; C++ )
    {
        long long sum = 0;

        for ( int k = 0; ( k + 1 ) * C < N - 1; k++ )
        {
            if ( k * C >= N - 1 - k * C && ( N - 1 ) % C == 0 ) break;

            sum += s[( N - 1 ) - k * C] + s[k * C];
            ans = max( ans, sum );
        }
    }

    cout << ans << endl;

    return 0;
}
