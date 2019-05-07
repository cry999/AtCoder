#include <algorithm>
#include <cstring>
#include <iostream>

using namespace std;

#define MAX_A1 10
#define MAX_A2 10
#define MAX_B1 10
#define MAX_B2 10
#define MAX_C1 10
#define MAX_C2 10

#define INF 0x3f3f3f3f

int indent = 0;

struct Box
{
public:
    int handred, fifty;

    Box( int handred, int fifty ) : handred( handred ), fifty( fifty ) {}

    bool is_empty() { return handred == 0 && fifty == 0; }

    Box extract_handred() { return Box( handred - 1, fifty ); }

    Box extract_fifty() { return Box( handred, fifty - 1 ); }

    double expectation()
    {
        return ( 100.0 * handred + 50.0 * fifty ) / ( handred + fifty );
    }

    void print() { cout << "(" << handred << ", " << fifty << ")" << endl; }
};

double dp[MAX_A1 + 1][MAX_A2 + 1][MAX_B1 + 1][MAX_B2 + 1][MAX_C1 + 1]
         [MAX_C2 + 1];

double set_dp( Box A, Box B, Box C, double val )
{
    int A1 = A.handred, A2 = A.fifty;
    int B1 = B.handred, B2 = B.fifty;
    int C1 = C.handred, C2 = C.fifty;

    return dp[A1][A2][B1][B2][C1][C2] = val;
}

double get_dp( Box A, Box B, Box C )
{
    int A1 = A.handred, A2 = A.fifty;
    int B1 = B.handred, B2 = B.fifty;
    int C1 = C.handred, C2 = C.fifty;

    return dp[A1][A2][B1][B2][C1][C2];
}

double max3( double a, double b, double c ) { return max( max( a, b ), c ); }

double min3( double a, double b, double c ) { return min( min( a, b ), c ); }

void print_space( int n )
{
    for ( int i = 0; i < n; i++ ) cout << " ";
}

double rec( Box A, Box B, Box C, int turn ) { return 0.0; }

int main( int argc, char **argv )
{
    int A1, A2, B1, B2, C1, C2;

    cin >> A1 >> A2;
    cin >> B1 >> B2;
    cin >> C1 >> C2;

    memset( dp, -1, sizeof( dp ) );

    double ans = rec( Box( A1, A2 ), Box( B1, B2 ), Box( C1, C2 ), 1 );

    cout << ans << endl;

    return 0;
}
