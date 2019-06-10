#include <iostream>

#define MAX_N 300000
#define MAX_LOG_A 30

using namespace std;

long long A[MAX_N + 1][MAX_LOG_A];

int main( int argc, char **argv )
{

    int N;
    cin >> N;

    for ( int i = 0; i < N; i++ )
    {
        long long a;
        cin >> a;

        for ( int k = 0; k < MAX_LOG_A; k++ )
        {
            A[i + 1][k] = A[i][k];

            if ( a & 1 ) A[i + 1][k]++;

            a >>= 1;
        }
    }

    for ( int i = 1; i <= N; i++ )
    {
        long long res = 0;
        for ( int j = 0; j < MAX_LOG_A; j++ )
        {
            if ( A[i][j] % 2 )
                res += ( i - A[i][j] ) << j;
            else
                res += A[i][j] << j;
        }
        cout << res << endl;
    }

    return 0;
}
