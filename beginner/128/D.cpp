#include <iostream>
#include <queue>

#define MAX_N 50

using namespace std;

int N, K;
int V[MAX_N];

int main( int argc, char **argv )
{
    // input
    cin >> N >> K;

    for ( int i = 0; i < N; i++ ) cin >> V[i];

    // solve
    long long ans = 0;
    int R = min( N, K );
    for ( int A = 0; A <= R; A++ )
    {
        for ( int B = 0; B <= R - A; B++ )
        {
            // cout << "=== A(" << A << ") B(" << B << ") ===" << endl;
            priority_queue<int> que;
            for ( int i = 0; i < A; i++ ) que.push( -V[i] );
            for ( int i = 0; i < B; i++ ) que.push( -V[N - 1 - i] );

            long long sum = 0;
            int throwAwayNum = 0;
            while ( !que.empty() )
            {
                int x = -que.top();
                que.pop();
                // cout << x << endl;

                if ( x < 0 && A + B + throwAwayNum < K )
                    throwAwayNum++;
                else
                    sum += x;
            }
            // cout << "sum = " << sum << endl;
            ans = max( ans, sum );
        }
    }

    cout << ans << endl;

    return 0;
}
