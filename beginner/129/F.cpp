#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

long long MOD = 1000000007;

struct matrix
{
    vector<vector<ll>> mat;
    ll row;
    ll col;

    void resize( ll row, ll col, ll initial )
    {
        this->row = row;
        this->col = col;
        mat.resize( row, vector<ll>( col, initial ) );
    }
    void identity() // first resize with initial = 0
    {
        for ( ll i = 0; i < (ll)mat.size(); i++ ) mat[i][i] = 1;
    }

    matrix operator+( matrix &b ) const
    {
        matrix temp;
        temp.resize( row, col, 0 );

        for ( ll i = 0; i < row; i++ )
        {
            for ( ll j = 0; j < col; j++ )
            {
                temp.mat[i][j] = ( mat[i][j] % MOD ) + ( b.mat[i][j] % MOD );
                temp.mat[i][j] %= MOD;
            }
        }
        return temp;
    }

    matrix operator*( matrix &b ) const
    {
        matrix temp;
        ll ro, co;

        temp.resize( row, b.col, 0 );
        for ( ll i = 0; i < row; i++ )
        {
            for ( ll j = 0; j < b.col; j++ )
            {
                for ( ll k = 0; k < col; k++ )
                {
                    temp.mat[i][j] +=
                        ( ( mat[i][k] % MOD ) * ( b.mat[k][j] % MOD ) );
                    temp.mat[i][j] %= MOD;
                }
            }
        }
        return temp;
    }

    matrix power( ll b )
    {
        matrix a = matrix( *this );
        matrix ans;

        ans.resize( row, col, 0 );
        ans.identity();

        while ( b )
        {
            if ( b & (ll)1 ) { ans = ans * a; }
            a = a * a;
            b >>= 1;
        }
        return ans;
    }
};

int main()
{
    ll l, a, b, m;
    cin >> l >> a >> b >> m;

    MOD = m;

    matrix ans;
    ans.resize( 1, 3, 0 );
    ans.mat[0][0] = a % MOD;
    ans.mat[0][1] = ( a + b ) % MOD;
    ans.mat[0][2] = 1;

    ll term = 1, d = 10;
    while ( term < l )
    {
        ll lo = max( (ll)0, ( ( d / 10 - 1 ) - a ) / b );
        ll hi = min( l - 1, max( ( d - 1 - a ) / b, (ll)0 ) );
        ll now = hi - lo;

        term += hi - lo;

        matrix temp;
        temp.resize( 3, 3, 0 );
        temp.mat[0][0] = d % MOD;
        temp.mat[1][0] = 1;
        temp.mat[1][1] = 1;
        temp.mat[2][1] = b % MOD;
        temp.mat[2][2] = 1;

        temp = temp.power( now );
        ans = ans * temp;

        d *= 10;
    }

    cout << ans.mat[0][0] << endl;

    return 0;
}
