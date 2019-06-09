#include <iostream>

#define MAX_N 32

using namespace std;

int N, K;
long long A[MAX_N];

int coinNum( long long price )
{
    long long c1 = 1000000000;
    long long c5 = 5000000000;
    int num = 0;

    for ( int i = 0; i < 10; i++ )
    {
        num += price / c5;
        price %= c5;

        num += price / c1;
        price %= c1;

        c5 /= 10;
        c1 /= 10;
    }

    return num;
}

int minCoinNum = 1 << 30;

void combination( int elmNum, int rest, int idx, long long price )
{
    if ( rest == 0 )
    {
        minCoinNum = min( minCoinNum, coinNum( price ) );
        return;
    }

    if ( elmNum - idx == rest )
    {
        for ( int i = idx; i < elmNum; i++ ) price += A[i];
        minCoinNum = min( minCoinNum, coinNum( price ) );
        return;
    }

    // buy A[idx]
    combination( elmNum, rest - 1, idx + 1, price + A[idx] );
    combination( elmNum, rest, idx + 1, price );
}

long long solve()
{
    combination( N, K, 0, 0 );
    return minCoinNum;
}

int main( int argc, char **argv )
{
    // input
    cin >> N >> K;
    for ( int i = 0; i < N; i++ ) cin >> A[i];

    cout << solve() << endl;

    return 0;
}
