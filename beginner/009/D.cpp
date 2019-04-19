#include <iostream>
#include <vector>

using namespace std;

#define MAX_K 100

class Matrix
{
public:
    Matrix( int row, int col ) : row( row ), col( col )
    {
        for ( int i = 0; i < row; i++ )
        {
            this->data.push_back( vector<long>() );
            for ( int j = 0; j < col; j++ ) this->data[i].push_back( 0 );
            // this->data[i][j] = 0;
        }
    }

    long get( int i, int j ) { return this->data[i][j]; }
    void set( int i, int j, long v ) { this->data[i][j] = v; }

    Matrix pow( int n )
    {
        Matrix ret = Matrix( this->row, this->col );
        this->_pow( n, ret );
        return ret;
    }

    Matrix operator^( Matrix other )
    {
        if ( this->col != other.col || this->row != other.row )
            return Matrix( 0, 0 );

        Matrix ret = Matrix( this->row, this->col );
        for ( int i = 0; i < this->row; i++ )
        {
            for ( int j = 0; j < this->col; j++ )
            {
                long v = this->data[i][j] ^ other.data[i][j];
                ret.set( i, j, v );
            }
        }
        return ret;
    }

    Matrix operator&( Matrix other )
    {
        if ( this->col != other.row ) return Matrix( 0, 0 );

        Matrix ret = Matrix( this->row, other.col );
        for ( int i = 0; i < this->row; i++ )
        {
            for ( int j = 0; j < other.col; j++ )
            {
                long v = 0;
                for ( int k = 0; k < this->col; k++ )
                    v ^= this->data[i][k] & other.data[k][j];
                ret.set( i, j, v );
            }
        }
        return ret;
    }

    void print()
    {
        for ( int i = 0; i < this->row; i++ )
        {
            for ( int j = 0; j < this->col; j++ )
                cout << this->data[i][j] << " ";
            cout << endl;
        }
    }

private:
    int row, col;
    vector<vector<long>> data;
    // long data[MAX_K][MAX_K];

    void _pow( int n, Matrix &ret )
    {
        // cout << "_pow(" << n << ")" << endl;
        if ( n == 0 )
        {
            for ( int i = 0; i < this->row; i++ )
                for ( int j = 0; j < this->col; j++ )
                    ret.set( i, j, i == j ? -1 : 0 );
        }
        else if ( n % 2 )
        {
            this->_pow( n - 1, ret );
            ret = ( *this ) & ret;
        }
        else
        {
            this->_pow( n / 2, ret );
            ret = ret & ret;
        }
    }
};

int main( int argc, char **argv )
{
    int K, M;
    cin >> K >> M;

    Matrix A = Matrix( K, 1 );
    Matrix C = Matrix( K, K );

    for ( int k = 0; k < K; k++ )
    {
        long a;
        cin >> a;

        A.set( K - k - 1, 0, a );
    }

    for ( int k = 0; k < K; k++ )
    {
        long c;
        cin >> c;

        C.set( 0, k, c );
    }

    for ( int i = 0; i < K - 1; i++ ) { C.set( i + 1, i, -1 ); }

    if ( M - K < 0 ) { cout << A.get( K - M, 0 ) << endl; }
    else
    {
        A = C.pow( M - K ) & A;
        cout << A.get( 0, 0 ) << endl;
    }

    return 0;
}
