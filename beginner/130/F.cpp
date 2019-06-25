#include <algorithm>
#include <iomanip>
#include <iostream>
#include <vector>

#define INF ( 1LL << 60 )

using namespace std;

struct Point
{
    double x, y;
    char d;

    friend ostream &operator<<( ostream &out, const Point &p )
    {
        return ( out << "P(" << p.x << ", " << p.y << ", " << p.d );
    }

    friend istream &operator>>( istream &in, Point &p )
    {
        return ( in >> p.x >> p.y >> p.d );
    }
};

int N;
vector<Point> points;

/**
 * t[s] の時の面積を計算する。
 */
double area( double t )
{
    double xmin = INF;
    double ymin = INF;
    double xmax = -INF;
    double ymax = -INF;

    for ( auto p : points )
    {
        double cx = p.x + ( p.d == 'L' ? ( -t ) : ( p.d == 'R' ? t : 0 ) );
        double cy = p.y + ( p.d == 'D' ? ( -t ) : ( p.d == 'U' ? t : 0 ) );

        xmin = min( xmin, cx );
        xmax = max( xmax, cx );
        ymin = min( ymin, cy );
        ymax = max( ymax, cy );
    }

    return ( xmax - xmin ) * ( ymax - ymin );
}

template <typename T>
T abs( T a )
{
    return a > 0 ? a : -a;
}

void gen_candidates( bool is_vertical, bool is_min, vector<double> &dist )
{
    double backward = is_min ? INF : -INF;   // 減少方向へ動くもの
    double forward = is_min ? INF : -INF;    // 増加方向へ動くもの
    double orthogonal = is_min ? INF : -INF; // 直交方向へ動くもの

    auto min = []( double a, double b ) { return a > b ? b : a; };
    auto max = []( double a, double b ) { return a > b ? a : b; };
    auto ope = is_min ? min : max;

    for ( auto p : points )
    {
        double v = is_vertical ? p.y : p.x;

        if ( p.d == ( is_vertical ? 'D' : 'L' ) )
            backward = ope( v, backward );
        else if ( p.d == ( is_vertical ? 'U' : 'R' ) )
            forward = ope( v, forward );
        else
            orthogonal = ope( v, orthogonal );
    }

    auto defined = is_min ? []( double a ) { return a < INF; }
                          : []( double a ) { return a > -INF; };

    if ( defined( backward ) && defined( forward ) )
        dist.push_back( abs( backward - forward ) / 2 );
    if ( defined( forward ) && defined( orthogonal ) )
        dist.push_back( abs( forward - orthogonal ) );
    if ( defined( orthogonal ) && defined( backward ) )
        dist.push_back( abs( orthogonal - backward ) );
}

int main( int argc, char **argv )
{
    cin >> N;

    points.resize( N );
    for ( int i = 0; i < N; i++ ) cin >> points[i];

    vector<double> candidates;

    gen_candidates( true, true, candidates );
    gen_candidates( true, false, candidates );
    gen_candidates( false, true, candidates );
    gen_candidates( false, false, candidates );

    sort( candidates.begin(), candidates.end() );
    candidates.erase( unique( candidates.begin(), candidates.end() ),
                      candidates.end() );

    double res = INF;
    for ( auto t : candidates ) res = min( res, area( t ) );

    cout << fixed << setprecision( 10 );
    cout << res << endl;

    return 0;
}
