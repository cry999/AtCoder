#include <iostream>

#define MAX_N 100000

using namespace std;

int N, M, L;
long long A[MAX_N], B[MAX_N];

int main( int argc, char **argv )
{
    cin >> N >> M >> L;

    for ( int n = 0; n < N; n++ ) cin >> A[n] >> B[n];

    long long fast_time = ( 1ULL << 63 ) - 1;
    for ( int n = 0; n < N; n++ )
        fast_time = min( fast_time, A[n] + B[n] * (long long)M );

    fast_time = min( fast_time, (long long)L * (long long)M );

    // // いろはちゃんが最後の何駅間を走るか二分探索で求める。
    // int l = 0, r = M + 1;
    // while ( r - l > 1 )
    // {
    //     int m = ( r + l ) / 2;

    //     long long train_time = ( 1ULL << 63 ) - 1;
    //     for ( int n = 0; n < N; n++ )
    //         train_time = min( train_time, A[n] + B[n] * (long long)( M - m )
    //         );

    //     // 電車を利用しない
    //     if ( M - m == 0 ) train_time = 0;

    //     long long iroha_time = (long long)L * (long long)m;

    //     if ( train_time + iroha_time <= fast_time )
    //     {
    //         fast_time = train_time + iroha_time;
    //         r = m;
    //     }
    //     else
    //         l = m;
    // }

    cout << fast_time << endl;

    return 0;
}
