#include <algorithm>
#include <cstring>
#include <iomanip>
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

    Box extract100() { return Box( handred - 1, fifty ); }

    Box extract50() { return Box( handred, fifty - 1 ); }

    double expectation()
    {
        return ( 100.0 * handred + 50.0 * fifty ) / ( handred + fifty );
    }

    double prob100() { return ( handred + 0.0 ) / ( handred + fifty ); }

    double prob50() { return ( fifty + 0.0 ) / ( handred + fifty ); }
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

double rec( Box A, Box B, Box C, int turn )
{
    // already calculated
    if ( get_dp( A, B, C ) >= 0.0 ) return get_dp( A, B, C );

    // nothing to do
    if ( A.is_empty() && B.is_empty() && C.is_empty() ) return 0.0;

    // EX = expectation value when extract coin from box X
    double EA =
        A.is_empty() ? ( turn ? 0.0 : INF ) : ( turn ? A.expectation() : 0.0 );
    double EB =
        B.is_empty() ? ( turn ? 0.0 : INF ) : ( turn ? B.expectation() : 0.0 );
    double EC =
        C.is_empty() ? ( turn ? 0.0 : INF ) : ( turn ? C.expectation() : 0.0 );

    if ( !A.is_empty() )
    {
        if ( A.handred > 0 )
            EA += rec( A.extract100(), B, C, 1 - turn ) * A.prob100();
        if ( A.fifty > 0 )
            EA += rec( A.extract50(), B, C, 1 - turn ) * A.prob50();
    }

    if ( !B.is_empty() )
    {
        if ( B.handred > 0 )
            EB += rec( A, B.extract100(), C, 1 - turn ) * B.prob100();
        if ( B.fifty > 0 )
            EB += rec( A, B.extract50(), C, 1 - turn ) * B.prob50();
    }

    if ( !C.is_empty() )
    {
        if ( C.handred > 0 )
            EC += rec( A, B, C.extract100(), 1 - turn ) * C.prob100();
        if ( C.fifty > 0 )
            EC += rec( A, B, C.extract50(), 1 - turn ) * C.prob50();
    }

    // when my turn, i want to maximize expectation value, but, when others
    // turn, he wants to minimize it.
    return set_dp( A, B, C, turn ? max3( EA, EB, EC ) : min3( EA, EB, EC ) );
}

int main( int argc, char **argv )
{
    int A1, A2, B1, B2, C1, C2;

    cin >> A1 >> A2;
    cin >> B1 >> B2;
    cin >> C1 >> C2;

    memset( dp, -1, sizeof( dp ) );

    double ans = rec( Box( A1, A2 ), Box( B1, B2 ), Box( C1, C2 ), 1 );

    cout << fixed;
    cout << setprecision( 10 );
    cout << ans << endl;

    return 0;
}
