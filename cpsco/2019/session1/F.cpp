#include <iostream>
#include <queue>

#define MAX_N 20000

using namespace std;

typedef pair<int64_t, int64_t> P;

struct Fruit
{
    int64_t t;
    int64_t A;
    int64_t B;
};

int64_t N;
Fruit fruits[MAX_N];

bool check( int64_t x )
{
    priority_queue<P> eatNotYet;
    priority_queue<P> canEat;

    // まだ食べられないものリストに全部突っ込む
    for ( int i = 0; i < N; i++ )
    {
        auto f = fruits[i];
        if ( f.A < x ) return false;

        int64_t v = ( f.A - x ) / f.B;
        int64_t L = max( (int64_t)1, f.t - v );
        int64_t R = min( N, f.t + v );

        // 賞味期限が始まるのが早い順に取り出せるようにする。
        eatNotYet.push( P( -L, R ) );
    }

    for ( int t = 1; t <= N; t++ )
    {
        while ( true )
        {
            // まだ食べられないものリストに残っていない
            if ( eatNotYet.empty() ) break;

            int64_t L = -eatNotYet.top().first;
            int64_t R = eatNotYet.top().second;

            // 賞味期限が始まってない
            if ( t < L ) break;
            eatNotYet.pop();

            // 賞味期限が終わるのが早い順に突っ込む
            canEat.push( P( -R, L ) );
        }

        // 食べられるものがまだない
        if ( canEat.empty() ) return false;

        int64_t L = canEat.top().second;
        int64_t R = -canEat.top().first;
        canEat.pop();

        // 賞味期限切れ発見
        if ( R < t ) return false;
    }
    // 全て食べつくしてたら OK
    return true;
}

int main( int argc, char **argv )
{
    cin >> N;
    for ( int i = 0; i < N; i++ )
        cin >> fruits[i].t >> fruits[i].A >> fruits[i].B;

    auto f = fruits[0];
    int64_t maxX = f.A;
    int64_t minX = f.A - max( f.t - 1, N - f.t ) * f.B;
    for ( int i = 0; i < N; i++ )
    {
        auto f = fruits[i];

        maxX = max( maxX, f.A );
        minX = min( minX, f.A - max( f.t - 1, N - f.t ) * f.B );
    }

    int64_t l = minX;
    int64_t r = maxX;

    while ( r - l > 1 )
    {
        int64_t m = ( r + l ) / 2;
        if ( check( m ) )
            l = m;
        else
            r = m;
    }

    cout << l << endl;

    return 0;
}
