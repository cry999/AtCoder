#include <algorithm>
#include <iostream>

using namespace std;

typedef long long ll;

int main( int argc, char **argv )
{
    ll N;
    cin >> N;

    ll res = 0;
    for ( ll a = 1; a * a <= N; a++ )
    {
        if ( N % a ) continue;

        ll m = ( N / a ) - 1;
        if ( m <= a ) continue;

        res += m;
    }

    cout << res << endl;

    return 0;
}
