#include <algorithm>
#include <iostream>
#include <map>
#include <tuple>
#include <vector>

using namespace std;

typedef tuple<int, int, int, bool> T4;

int getM( T4 t ) { return get<0>( t ); }
int getk( T4 t ) { return get<1>( t ); }
int getOrdIdx( T4 t ) { return get<2>( t ); }
bool isLeft( T4 t ) { return get<3>( t ); }

long long N, X;
long long A[100010];

long long solve( int L, int R )
{
    if ( R < L ) { return 0; }
    if ( R == L ) { return A[L] + A[L] + A[L] == X ? 1 : 0; }
    if ( R - L == 1 )
    {
        long long tmp = 0;
        if ( A[L] + A[L] + A[L] == X ) { tmp++; }
        if ( A[R] + A[R] + A[R] == X ) { tmp++; }
        if ( A[L] <= A[R] && A[L] + A[R] + A[R] == X ) { tmp++; }
        if ( A[R] <= A[L] && A[L] + A[L] + A[R] == X ) { tmp++; }
        return tmp;
    }

    long long ans = 0;
    int mid = ( L + R ) / 2;
    vector<T4> vec;

    int Ml = -1;
    int kl = 0;
    for ( int i = mid; i >= L; i-- )
    {
        if ( A[i] > Ml )
        {
            Ml = A[i];
            kl = 1;
        }
        else if ( A[i] == Ml )
        {
            kl++;
        }
        vec.push_back( T4( Ml, kl, i, true ) );
    }

    int Mr = -1;
    int kr = 0;
    for ( int i = mid + 1; i <= R; i++ )
    {
        if ( A[i] > Mr )
        {
            Mr = A[i];
            kr = 1;
        }
        else if ( A[i] == Mr )
        {
            kr++;
        }
        vec.push_back( T4( Mr, kr, i, false ) );
    }
    sort( vec.begin(), vec.end() );

    map<int, long long> mpL;
    map<int, long long> mpR;
    int M = -1;
    for ( int i = 0; i < vec.size(); i++ )
    {
        auto t = vec[i];

        if ( getM( t ) != M )
        {
            int mark = i;
            M = getM( t );
            while ( mark < vec.size() && getM( vec[mark] ) == M )
            {
                if ( isLeft( vec[mark] ) )
                    mpR[A[getOrdIdx( vec[mark] )]]++;
                else
                    mpL[A[getOrdIdx( vec[mark] )]]++;

                mark++;
            }
        }

        if ( isLeft( t ) )
            ans += mpL[X - getM( t ) - A[getOrdIdx( t )]] * getk( t );
        else
            ans += mpR[X - getM( t ) - A[getOrdIdx( t )]] * getk( t );
    }

    ans += solve( L, mid );
    ans += solve( mid + 1, R );

    return ans;
}

int main()
{
    cin >> N >> X;
    for ( int i = 0; i < N; i++ ) { cin >> A[i]; }

    long long ans = solve( 0, N - 1 );
    cout << ans << endl;

    return 0;
}
