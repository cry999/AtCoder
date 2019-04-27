#include <iostream>

using namespace std;

#define MAX_N 20
#define MAX_V 50
#define MAX_C 50

int V[MAX_V], C[MAX_C];

int main( int argc, char **argv )
{
    int N;
    cin >> N;

    for ( int i = 0; i < N; i++ ) cin >> V[i];
    for ( int i = 0; i < N; i++ ) cin >> C[i];

    int max_diff = 0;
    for ( int i = 0; i < ( 1 << N ); i++ )
    {
        int diff = 0;
        for ( int j = 0; j < N; j++ )
            if ( i & ( 1 << j ) ) diff += V[j] - C[j];
        max_diff = max( max_diff, diff );
    }

    cout << max_diff << endl;

    return 0;
}
