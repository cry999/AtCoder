#include <algorithm>
#include <iostream>
#include <limits>
#include <vector>

using namespace std;

namespace iroha_day2_k
{
const int MAX_N = 200000;
}

struct Rmq
{
private:
    int size;
    vector<long long> data;

    /**
     * @fn
     * query minimum value in [a, b)
     * @param a lower of range
     * @param b upper of range
     * @param idx index of focused
     * @param l lower of range managed by focused node
     * @param r upper of range managed by focused node
     * @return minimum value in [a, b)
     */
    long long internalQuery( int a, int b, int idx, int l, int r )
    {
        // no cross point
        if ( b <= l || r <= a ) return numeric_limits<long long>::max();

        // whole included
        if ( l <= a && b <= r ) return data[idx];

        int lidx = 2 * idx + 1; // index of left node
        int ridx = 2 * idx + 2; // index of right node
        int m = ( l + r ) / 2;  // middium point in range[l, r)

        long long lv = internalQuery( a, b, lidx, l, m );
        long long rv = internalQuery( a, b, ridx, m, r );

        return min( lv, rv );
    }

public:
    /**
     * @fn
     * initialize this RMQ
     * @param size size of RMQ
     */
    void init( vector<int> raw )
    {
        data.clear();

        int size = raw.size();
        int n = 1;
        while ( n < size ) n <<= 1;

        this->size = n;
        data.resize( 2 * n - 1, numeric_limits<long long>::max() );

        for ( int i = 0; i < size; i++ ) data[i + n - 1] = raw[i];
        for ( int i = n - 2; i >= 0; i-- )
            data[i] = min( data[2 * i + 1], data[2 * i + 2] );
    }

    /**
     * @fn
     * update data[idx] to val
     * @param idx index of data which you want to update
     * @param val value which you want to update to
     */
    void update( int idx, long long val )
    {
        idx += size - 1;
        data[idx] = val;

        while ( idx > 0 )
        {
            int p = ( idx - 1 ) / 2;
            int l = 2 * p + 1;
            int r = 2 * p + 2;

            data[p] = min( data[l], data[r] );

            idx = p;
        }
    }

    /**
     * @fn
     * query minimum value in [l, r)
     * @param l lower of range
     * @param r upper of range
     * @return minimum value in [l, r)
     */
    long long query( int l, int r )
    {
        return internalQuery( l, r, 0, 0, size );
    }
};

struct LazySegTree
{
private:
    int size;
    vector<long long> data, lazy;
    vector<bool> hasLazyUpdate;

    /**
     * @fn
     * check whther `idx`th node has lazy value or not.
     * @param idx index of node whose lazy value you want to check
     * @return node has lazy value or not
     */
    bool hasLazy( int idx ) { return lazy[idx] != 0; }

    /**
     * @fn
     * update data whose index is in [a, b) to `val`.
     * @param a the lower of index range you want to update
     * @param b the upper of index range you want to update
     * @param val the value you want to update data[a] ... data[b-1] to
     * @param idx index of node in this tree
     * @param l the lower of range managed by idx-th node
     * @param r the upper of range managed by idx-th node
     */
    void internalUpdate( int a, int b, long long val, int idx, int l, int r )
    {
        eval( idx, l, r );

        // no cross point
        if ( b <= l || r <= a ) return;

        if ( a <= l && r <= b )
        {
            // whole included

            // update idx-th node to sum of its children new lazy values
            lazy[idx] = val * ( r - l );
            hasLazyUpdate[idx] = true;

            eval( idx, l, r );
        }
        else
        {
            // partly included

            int lidx = 2 * idx + 1; // index of left child
            int ridx = 2 * idx + 2; // index of right child
            int m = ( l + r ) / 2;  // medium of the range [l, r)

            internalUpdate( a, b, val, lidx, l, m ); // update left child
            internalUpdate( a, b, val, ridx, m, r ); // update right child

            // update this node
            data[idx] = data[lidx] + data[ridx];
        }
    }

    /**
     * @fn
     * update data whose index is in [a, b) to `val`.
     * @param a the lower of index range you want to add val
     * @param b the upper of index range you want to add val
     * @param val the value you want to add to data[a] ... data[b-1]
     * @param idx index of node in this tree
     * @param l the lower of range managed by idx-th node
     * @param r the upper of range managed by idx-th node
     */
    void internalAdd( int a, int b, long long val, int idx, int l, int r )
    {
        eval( idx, l, r );

        // no cross point
        if ( b <= l || r <= a ) return;

        if ( a <= l && r <= b )
        {
            // whole included

            // add this node's children lazy values to this one
            lazy[idx] += val * ( r - l );

            eval( idx, l, r );
        }
        else
        {
            // partly included

            int lidx = 2 * idx + 1; // index of left node
            int ridx = 2 * idx + 2; // index of right node
            int m = ( l + r ) / 2;  // medium of the range [l, r)

            internalAdd( a, b, val, lidx, l, m ); // add to left child
            internalAdd( a, b, val, ridx, m, r ); // add to right child

            // in last, add this node.
            data[idx] = data[lidx] + data[ridx];
        }
    }

    /**
     * @fn
     * compute summary from l to r-1.
     * @param a the lower of index range you want to summarize
     * @param b the upper of index range you want to summarize
     * @param idx index of node in this tree
     * @param l the lower of range managed by idx-th node
     * @param r the upper of range managed by idx-th node
     */
    long long internalSum( int a, int b, int idx, int l, int r )
    {
        // no cross point
        if ( b <= l || r <= a ) return 0LL;

        eval( idx, l, r );

        if ( a <= l && r <= b )
        {
            // whole included

            return data[idx];
        }
        else
        {
            // partly included

            int lidx = 2 * idx + 1; // index of left node
            int ridx = 2 * idx + 2; // index of right node
            int m = ( l + r ) / 2;  // medium of the range [l, r)

            long long lv = internalSum( a, b, lidx, l, m ); // sum left
            long long rv = internalSum( a, b, ridx, m, r ); // sum right

            return lv + rv;
        }
    }

public:
    /**
     * @fn
     * initialize
     * @param size size of this segment tree
     */
    void init( int size )
    {
        int n = 1;
        while ( n < size ) n <<= 1;

        this->size = n;
        this->data.resize( 2 * n - 1, 0 );
        this->lazy.resize( 2 * n - 1, 0 );
        this->hasLazyUpdate.resize( 2 * n - 1, false );
    }

    /**
     * @fn
     * evaluates lazy value `idx`th node has
     * @param idx index of node you want to evaluates
     * @param l the lower of range managed by the node
     * @param r the upper of range managed by the node
     */
    void eval( int idx, int l, int r )
    {
        if ( hasLazyUpdate[idx] )
        {
            // update

            // update value of idx-th node to the newest lazy value, ignore
            // older ones.
            data[idx] = lazy[idx];

            // propagate evaluates value to its children
            // if its node has children
            if ( r - l > 1 )
            {
                int lidx = 2 * idx + 1;
                int ridx = 2 * idx + 2;

                // propagte half of evaluates value to each children.
                // if children already has lazy value, overwrite it.
                lazy[lidx] = lazy[idx] / 2;
                lazy[ridx] = lazy[idx] / 2;

                // make children `hasLazyUpdate` on
                hasLazyUpdate[lidx] = true;
                hasLazyUpdate[ridx] = true;
            }

            // clear `idx`th node's lazy value
            lazy[idx] = 0;
            hasLazyUpdate[idx] = false;
        }
        else
        {
            // add

            // if this node has no lazy value, ignore this.
            if ( lazy[idx] == 0LL ) return;

            // add lazy value to this node
            data[idx] += lazy[idx];

            // if this has children, propagate lazy value.
            if ( r - l > 1 )
            {
                int lidx = 2 * idx + 1;
                int ridx = 2 * idx + 2;

                // if children already has lazy values, add new one to it.
                lazy[lidx] += lazy[idx] / 2;
                lazy[ridx] += lazy[idx] / 2;
            }

            // clear lazy value of this node
            lazy[idx] = 0;
        }
    }

    /**
     * @fn
     * update data[l], ..., data[r-1] to `val`
     * @param l the lower of the range
     * @param r the upper of the range
     * @param val the value you want to update data to
     */
    void update( int l, int r, long long val )
    {
        internalUpdate( l, r, val, 0, 0, size );
    }

    /**
     * @fn
     * add `val` to data[l], ..., data[r-1]
     * @param l the lower of the range
     * @param r the upper of the range
     * @param val the value you want to add to data
     */
    void add( int l, int r, long long val )
    {
        internalAdd( l, r, val, 0, 0, size );
    }

    /**
     * @fn
     * compute summary from l to r-1.
     * @param l lower of range
     * @param r upper of range
     * @return summary
     */
    long long sum( int l, int r ) { return internalSum( l, r, 0, 0, size ); }
};

// Tree's variables
vector<int> edges[iroha_day2_k::MAX_N];
vector<int> children[iroha_day2_k::MAX_N];
int subtreeSize[iroha_day2_k::MAX_N];

// HL Decomposition's variables
int dfsOrder[iroha_day2_k::MAX_N];
int parent[iroha_day2_k::MAX_N];
int pos[iroha_day2_k::MAX_N];
vector<int> eulerTour;
int pre[iroha_day2_k::MAX_N];
int pathParent[iroha_day2_k::MAX_N];

struct Tree
{
private:
    int treeSize;
    int hldCount;
    Rmq lcaRmq;

    int dfs( int v, int p )
    {
        for ( auto u : edges[v] )
        {
            if ( u == p ) continue;

            children[v].push_back( u );
            subtreeSize[v] += dfs( u, v );
        }
        return subtreeSize[v];
    }

    /**
     * @fn
     * found child whose subtree size is max.
     * @param p parent
     * @return id of p's child whose subtree size is max in p's children
     */
    int childWhoseSubtreeIsMax( int p )
    {
        int maxSize = -1, maxChild = -1;
        for ( auto child : children[p] )
        {
            if ( maxSize < subtreeSize[child] )
            {
                maxSize = subtreeSize[child];
                maxChild = child;
            }
        }
        return maxChild;
    }

    /**
     * @fn
     * compute HL Decompression
     * @param v vertex
     * @param p parent
     * @param pp path parent
     */
    void hld( int v, int p, int pp )
    {
        int t = hldCount++;

        dfsOrder[v] = t;

        parent[t] = p;
        pre[t] = eulerTour.size();
        pathParent[t] = pp;

        if ( children[v].size() == 0 )
        {
            eulerTour.push_back( t );
            pos[t] = hldCount;
            return;
        }

        int maxChild = childWhoseSubtreeIsMax( v );

        eulerTour.push_back( t );
        hld( maxChild, t, pp );
        eulerTour.push_back( t );

        for ( auto child : children[v] )
        {
            if ( child == maxChild ) continue;
            hld( child, t, hldCount );
            eulerTour.push_back( t );
        }

        pos[t] = hldCount;
    }

public:
    void init( int size ) { treeSize = size; }

    void addEdge( int u, int v )
    {
        edges[u].push_back( v );
        edges[v].push_back( u );
    }

    void build()
    {
        dfs( 0, 0 );
        hldCount = 0;
        hld( 0, 0, 0 );
        lcaRmq.init( eulerTour );
    }

    int lca( int u, int v )
    {
        if ( pre[u] < pre[v] )
            return lcaRmq.query( pre[u], pre[v] + 1 );
        else
            return lcaRmq.query( pre[v], pre[u] + 1 );
    }

    int getDfsOrder( int v ) { return dfsOrder[v]; }

    int getPos( int dfsOrder_ ) { return pos[dfsOrder_]; }

    int getSubtreeSize( int dfsOrder_ ) { return pos[dfsOrder_] - dfsOrder_; }

    int getPathParent( int dfsOrder_ ) { return pathParent[dfsOrder_]; }

    int getParent( int pp ) { return parent[pp]; }
};

Tree tree;
LazySegTree seg;

/**
 * @fn
 * move from `from` vertex to `to` vertex, collecting insects on vertex.
 * @param from source vertex
 * @param to destination vertex
 * @param tree tree where kitanuu moves
 * @return collected insects
 */
long long move( int from, int to, Tree tree )
{
    long long res = 0;
    int lca = tree.lca( from, to );

    // move from `from` to LCA
    int now = from;
    while ( true )
    {
        int pp = tree.getPathParent( now );

        if ( pp == tree.getPathParent( lca ) )
        {
            // reaches LCA from start point

            // collect insects
            res += seg.sum( lca, now + 1 );
            // get all insects from `from` vertex, so remove it from there.
            seg.update( lca, now + 1, 0 );

            break;
        }
        else
        {
            // halfway

            // collect insects
            res += seg.sum( pp, now + 1 );
            // get all insects from `from` vertex, so remove it from there.
            seg.update( pp, now + 1, 0 );

            now = tree.getParent( pp );
        }
    }

    // move from `to` to LCA
    now = to;
    while ( true )
    {
        int pp = tree.getPathParent( now );

        // reaches LCA
        if ( pp == tree.getPathParent( lca ) )
        {
            // collect insects
            res += seg.sum( lca, now + 1 );
            // get all insects from `from` vertex, so remove it from there.
            seg.update( lca, now + 1, 0 );

            break;
        }
        // halfway
        else
        {
            // collect insects
            res += seg.sum( pp, now + 1 );
            // get all insects from `from` vertex, so remove it from there.
            seg.update( pp, now + 1, 0 );

            now = tree.getParent( pp );
        }
    }

    return res;
}

/**
 * @fn
 * handle query
 * @param N size of tree
 * @param Q number of queries
 * @param tree tree
 */
void handleQuery( int N, int Q )
{
    // handle query
    seg.init( N );
    int now = 0;
    for ( int q = 0; q < Q; q++ )
    {
        int t, i;
        cin >> t >> i;

        i = tree.getDfsOrder( i );

        if ( t == 0 )
        {
            long long k;
            cin >> k;

            // add `k` insect into t's subtree
            int p = tree.getPos( i );
            int s = tree.getSubtreeSize( i );
            seg.add( i, p, k / s );
        }
        else
        {
            cout << move( now, i, tree ) << endl << flush;
        }
    }
}

/**
 * @fn
 * main function
 * @param argc number of argument
 * @param argv arguments
 * @return error code
 */
int main( int argc, char **argv )
{
    // input
    int N, Q;
    cin >> N >> Q;

    // build tree
    tree.init( N );
    for ( int n = 0; n < N - 1; n++ )
    {
        int C, D;
        cin >> C >> D;

        tree.addEdge( C, D );
    }
    tree.build();

    handleQuery( N, Q );

    return 0;
}
