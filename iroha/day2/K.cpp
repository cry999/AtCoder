#include <iostream>
#include <vector>

using namespace std;

// RMQ
struct RMQ
{
private:
    int N;
    vector<long long> node;
    const long long DEFAULT = 9223372036854775807LL;

public:
    void init( vector<int> v )
    { //初期化する O(N)
        node.clear();
        N = 1;
        while ( N < v.size() ) N *= 2;
        for ( int i = 0; i < 2 * N - 1; i++ ) node.push_back( DEFAULT );
        for ( int i = 0; i < v.size(); i++ ) node[i + N - 1] = v[i];
        for ( int i = N - 2; i >= 0; i-- )
            node[i] = min( node[i * 2 + 1], node[i * 2 + 2] );
    }
    void update( int i, long long x )
    { //値を変更する O(log N)
        i += N - 1;
        node[i] = x;
        while ( i > 0 )
        {
            i = ( i - 1 ) / 2; //親の取得は(i-1)/2
            node[i] =
                min( node[i * 2 + 1], node[i * 2 + 2] ); //子の取得はi*2+1,i*2+2
        }
    }
    long long minimum( int a, int b, int k = 0, int l = 0, int r = -1 )
    { //[a,b)の最小値を求める O(log N)
        if ( r == -1 ) r = N;
        if ( r <= a || b <= l ) return DEFAULT; //交差する場合
        if ( a <= l && r <= b ) return node[k]; //完全に含む場合
        return min( minimum( a, b, k * 2 + 1, l, ( l + r ) / 2 ),
                    minimum( a, b, k * 2 + 2, ( l + r ) / 2, r ) );
    }
};

// RUQ&RSQ-RSQ
struct SegmentTree
{
private:
    int N;
    vector<long long> node, lazy;
    vector<bool> lazyFlg;
    const long long DEFAULT = 0LL;

public:
    void init( int n )
    { //初期化する O(N)
        node.clear();
        lazy.clear();
        lazyFlg.clear();
        N = 1;
        while ( N < n ) N *= 2;
        for ( int i = 0; i < 2 * N - 1; i++ )
        {
            node.push_back( DEFAULT );
            lazy.push_back( 0LL );
            lazyFlg.push_back( false );
        }
    }
    void eval( int k, int l, int r )
    { //遅延評価を行う
        if ( lazyFlg[k] )
        { // RUQ：下に更新クエリが溜まっていても加算クエリが溜まっていても上書き
            node[k] = lazy[k];
            if ( r - l > 1 )
            {
                lazy[2 * k + 1] = lazy[k] / 2;
                lazyFlg[2 * k + 1] = true;
                lazy[2 * k + 2] = lazy[k] / 2;
                lazyFlg[2 * k + 2] = true;
            }
            lazy[k] = 0LL;
            lazyFlg[k] = false;
        }
        else
        { // RAQ：下に更新クエリが溜まっていても加算クエリが溜まっていても加算
            if ( lazy[k] == 0LL ) return;
            node[k] += lazy[k];
            if ( r - l > 1 )
            {
                lazy[2 * k + 1] += lazy[k] / 2;
                lazy[2 * k + 2] += lazy[k] / 2;
            }
            lazy[k] = 0LL;
        }
    }
    void update( int a, int b, long long x, int k = 0, int l = 0, int r = -1 )
    { //区間に対して値を変更する O(log N)
        if ( r == -1 ) r = N;
        eval( k, l, r );
        if ( r <= a || b <= l ) return; //交差する場合
        if ( a <= l && r <= b )
        { //完全に含む場合
            lazy[k] = x * ( r - l );
            lazyFlg[k] = true;
            eval( k, l, r );
        }
        else
        {
            update( a, b, x, 2 * k + 1, l, ( l + r ) / 2 );
            update( a, b, x, 2 * k + 2, ( l + r ) / 2, r );
            node[k] = node[2 * k + 1] + node[2 * k + 2];
        }
    }
    void add( int a, int b, long long x, int k = 0, int l = 0, int r = -1 )
    { //区間に対して値を加算する O(log N)
        if ( r == -1 ) r = N;
        eval( k, l, r );
        if ( r <= a || b <= l ) return; //交差する場合
        if ( a <= l && r <= b )
        { //完全に含む場合
            lazy[k] += x * ( r - l );
            eval( k, l, r );
        }
        else
        {
            add( a, b, x, 2 * k + 1, l, ( l + r ) / 2 );
            add( a, b, x, 2 * k + 2, ( l + r ) / 2, r );
            node[k] = node[2 * k + 1] + node[2 * k + 2];
        }
    }
    long long sum( int a, int b, int k = 0, int l = 0, int r = -1 )
    { //[a,b)の和を求める O(log N)
        if ( r == -1 ) r = N;
        if ( r <= a || b <= l ) return DEFAULT; //交差する場合
        eval( k, l, r );
        if ( a <= l && r <= b ) return node[k]; //完全に含む場合
        return sum( a, b, k * 2 + 1, l, ( l + r ) / 2 ) +
               sum( a, b, k * 2 + 2, ( l + r ) / 2, r );
    }
};

int N, Q;

//隣接リスト
vector<int> edge[200000];

//木
vector<int> chi[200000];
int siz[200000];

//親子関係の整理・部分木の大きさ計算
int dfs( int v, int p )
{
    for ( int i = 0; i < edge[v].size(); i++ )
    {
        if ( edge[v][i] == p ) continue;
        chi[v].push_back( edge[v][i] );
        siz[v] += dfs( edge[v][i], v );
    }
    return siz[v];
}

// HL分解後のDFS木
int dfsOrder[200000];
int par[200000];
int pos[200000];
vector<int> EularTour;
int pre[200000];
int pathPar[200000];

// HL分解
int c = 0;
void HLd( int v, int p, int pp )
{
    int t = c;
    c++;

    dfsOrder[v] = t;
    par[t] = p;
    pre[t] = EularTour.size();
    pathPar[t] = pp;

    if ( chi[v].size() == 0 )
    {
        EularTour.push_back( t );
        pos[t] = c;
        return;
    }

    int M = -1;
    int M_idx = -1;
    for ( int i = 0; i < chi[v].size(); i++ )
    {
        if ( M < siz[chi[v][i]] )
        {
            M = siz[chi[v][i]];
            M_idx = i;
        }
    }

    EularTour.push_back( t );
    HLd( chi[v][M_idx], t, pp );
    EularTour.push_back( t );
    for ( int i = 0; i < chi[v].size(); i++ )
    {
        if ( i == M_idx ) continue;
        HLd( chi[v][i], t, c );
        EularTour.push_back( t );
    }
    pos[t] = c;
}

// LCA
RMQ rmq;
int LCA( int i, int j )
{
    if ( pre[i] < pre[j] )
        return rmq.minimum( pre[i], pre[j] + 1 );
    else
        return rmq.minimum( pre[j], pre[i] + 1 );
}

//クエリ処理
SegmentTree st;
long long query( int i, int j )
{
    long long ret = 0;
    int lca = LCA( i, j );
    while ( true )
    {
        if ( pathPar[i] == pathPar[lca] )
        {
            ret += st.sum( lca, i + 1 );
            st.update( lca, i + 1, 0 );
            break;
        }
        else
        {
            ret += st.sum( pathPar[i], i + 1 );
            st.update( pathPar[i], i + 1, 0 );
            i = par[pathPar[i]];
        }
    }
    while ( true )
    {
        if ( pathPar[j] == pathPar[lca] )
        {
            ret += st.sum( lca, j + 1 );
            st.update( lca, j + 1, 0 );
            break;
        }
        else
        {
            ret += st.sum( pathPar[j], j + 1 );
            st.update( pathPar[j], j + 1, 0 );
            j = par[pathPar[j]];
        }
    }
    return ret;
}

int main()
{
    scanf( "%d%d", &N, &Q );
    for ( int i = 0; i < N - 1; i++ )
    {
        int C, D;
        scanf( "%d%d", &C, &D );
        edge[C].push_back( D );
        edge[D].push_back( C );
    }
    dfs( 0, 0 );
    HLd( 0, 0, 0 );
    rmq.init( EularTour );
    st.init( N );

    int now = 0;
    for ( int q = 0; q < Q; q++ )
    {
        int type, i;
        scanf( "%d%d", &type, &i );
        if ( type == 0 )
        {
            long long k;
            scanf( "%d", &k );
            i = dfsOrder[i];
            st.add( i, pos[i], k / ( pos[i] - i ) );
        }
        else
        {
            i = dfsOrder[i];
            long long ans = query( now, i );
            printf( "%lld\n", ans );
            fflush( stdout );
            now = i;
        }
    }
}
