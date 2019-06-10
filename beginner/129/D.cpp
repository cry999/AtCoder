#include <iostream>
#include <string>
#include <vector>

#define MAX_H 2000
#define MAX_W 2000

using namespace std;

struct UnionFind
{
private:
    int size;
    vector<int> root;

public:
    UnionFind( int size ) : size( size ) { root.resize( size, -1 ); }

    int find( int x )
    {
        if ( root[x] < 0 ) return x;
        return root[x] = find( root[x] );
    }

    bool same( int x, int y ) { return find( x ) == find( y ); }

    bool unite( int x, int y )
    {
        int rx = find( x );
        int ry = find( y );

        if ( rx == ry ) return false;
        if ( ry < rx ) swap( rx, ry );

        root[rx] += root[ry];
        root[ry] = rx;

        return true;
    }
};

int lenH[MAX_H * MAX_W]; // 縦方向のながさ
int lenW[MAX_H * MAX_W]; // 横方向のながさ

string S[MAX_H];

int main( int argc, char **argv )
{
    // inputs
    int H, W;
    cin >> H >> W;

    for ( int i = 0; i < H; i++ ) cin >> S[i];

    // solve
    UnionFind ufW( H * W + 1 );
    UnionFind ufH( H * W + 1 );

    auto index = [&]( const int h, const int w ) {
        if ( h < 0 || H <= h ) return H * W;
        if ( w < 0 || W <= w ) return H * W;
        return h * W + w;
    };

    // 横方向の長さを計算
    for ( int h = 0; h < H; h++ )
    {
        int len = 0;
        int start = 0;
        for ( int w = 0; w < W; w++ )
        {
            if ( S[h][w] == '#' )
            {
                // 壁
                int idx = index( h, w - 1 );
                lenW[ufW.find( idx )] = len;
                len = 0;
                start = w + 1;
            }
            else
            {
                // 通路
                len++;

                int idx1 = index( h, w );
                int idx2 = index( h, start );
                ufW.unite( idx1, idx2 );
            }
        }

        if ( len > 0 )
        {
            int idx = index( h, W - 1 );
            lenW[ufW.find( idx )] = len;
        }
    }

    // 縦方向の長さ
    for ( int w = 0; w < W; w++ )
    {
        int len = 0;
        int start = 0;
        for ( int h = 0; h < H; h++ )
        {
            if ( S[h][w] == '#' )
            {
                // 壁
                int idx = index( h - 1, w );
                lenH[ufH.find( idx )] = len;
                len = 0;
                start = h + 1;
            }
            else
            {
                // 通路
                len++;

                int idx1 = index( h, w );
                int idx2 = index( start, w );
                ufH.unite( idx1, idx2 );
            }
        }

        if ( len > 0 )
        {
            int idx = index( H - 1, w );
            lenH[ufH.find( idx )] = len;
        }
    }

    int maxLightUp = 0;
    for ( int h = 0; h < H; h++ )
    {
        for ( int w = 0; w < W; w++ )
        {
            int idx = index( h, w );
            int lightUp = lenH[ufH.find( idx )] + lenW[ufW.find( idx )] - 1;

            maxLightUp = max( maxLightUp, lightUp );
        }
    }

    cout << maxLightUp << endl;

    return 0;
}
