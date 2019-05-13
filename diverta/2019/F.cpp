// #include <iostream>
// #include <vector>

// #define MAX_N 20
// #define MOD 1000000007

// using namespace std;

// template <uint_fast64_t mod>
// struct modint
// {
// private:
//     uint_fast64_t val;

// public:
//     constexpr modint( const uint_fast64_t x = 0 ) noexcept : val( x % mod )
//     {}

//     constexpr uint_fast16_t value() const noexcept { return val; }

//     constexpr modint operator+( const modint &rhs ) const noexcept
//     {
//         return modint( *this ) += rhs;
//     }

//     constexpr modint operator-( const modint &rhs ) const noexcept
//     {
//         return modint( *this ) -= rhs;
//     }

//     constexpr modint operator*( const modint &rhs ) const noexcept
//     {
//         return modint( *this ) *= rhs;
//     }

//     constexpr modint operator/( const modint &rhs ) const noexcept
//     {
//         return modint( *this ) /= rhs;
//     }

//     constexpr modint &operator+=( const modint &rhs ) noexcept
//     {
//         val += rhs.val;
//         if ( val > mod ) val -= mod;
//         return *this;
//     }

//     constexpr modint &operator-=( const modint &rhs ) noexcept
//     {
//         if ( val < rhs.val ) val += mod;
//         val -= rhs.val;
//         return *this;
//     }

//     constexpr modint &operator*=( const modint &rhs ) noexcept
//     {
//         val = ( val * rhs.val ) % mod;
//         return *this;
//     }

//     constexpr modint &operator/=( const modint &rhs ) noexcept
//     {
//         long long a = rhs.val, b = mod, u = 1, v = 0;
//         while ( b )
//         {
//             long long t = a / b;
//             a -= t * b;
//             swap( a, b );

//             u -= t * v;
//             swap( u, v );
//         }

//         val = ( val * u ) % MOD;
//         if ( val < 0 ) val += MOD;
//         return *this;
//     }
// };

// using mint = modint<MOD>;

// mint _fact[MAX_N + 1];
// mint _fact_inv[MAX_N + 1];

// void init_comb()
// {
//     _fact[0] = mint( 1 );
//     for ( int n = 1; n <= MAX_N; n++ ) _fact[n] = mint( n ) * _fact[n - 1];

//     _fact_inv[MAX_N] = mint( 1 ) / _fact[MAX_N];
//     for ( int n = MAX_N; n > 0; n-- )
//         _fact_inv[n - 1] = mint( n ) * _fact_inv[n];
// }

// mint comb( int n, int r )
// {
//     if ( n <= r ) return 0;

//     return _fact[n] * _fact_inv[n - r] * _fact_inv[r];
// }

// mint fact( int n ) { return _fact[n]; }

// mint fact_inv( int n ) { return _fact_inv[n]; }

// struct edge
// {
//     int to, cost;
// };

// vector<edge> G[MAX_N];
// int cmp[1 << MAX_N];
// int cnt[1 << MAX_N];
// mint dp1[1 << MAX_N];
// mint dp2[1 << MAX_N];

// int dfs( int from, int parent, int to )
// {
//     if ( from == to ) return 0;

//     int res = -1;
//     for ( auto e : G[from] )
//     {
//         if ( e.to == parent ) continue;

//         int tmp = dfs( e.to, from, to );
//         if ( tmp == -1 ) continue;

//         res = ( res == -1 ? 0 : res ) | tmp | ( 1 << e.cost );
//     }

//     return res;
// }

// int bitnum( int n )
// {
//     int res = 0;
//     while ( n != 0 )
//     {
//         if ( n & 1 ) res++;
//         n >>= 1;
//     }
//     return res;
// }

// int main( int argc, char **argv )
// {
//     init_comb();

//     /*****************************************
//      * input
//      *****************************************/
//     int N, M;
//     cin >> N >> M;

//     for ( int n = 0; n < N - 1; n++ )
//     {
//         int a, b;
//         cin >> a >> b;

//         G[a - 1].push_back( ( edge ){b - 1, n} );
//         G[b - 1].push_back( ( edge ){a - 1, n} );
//     }

//     for ( int n = N - 1; n < M; n++ )
//     {
//         int a, b;
//         cin >> a >> b;

//         int S = dfs( a - 1, -1, b - 1 );
//         cmp[S]++;
//     }

//     /*****************************************
//      * fast ζ transform
//      *****************************************/
//     for ( int i = 0; i < N - 1; i++ )
//         for ( int bit = 0; bit < ( 1 << ( N - 1 ) ); bit++ )
//             if ( bit & ( 1 << i ) ) cmp[bit] += cmp[bit ^ ( 1 << i )];

//     for ( int bit = 0; bit < ( 1 << ( N - 1 ) ); bit++ )
//     {
//         cnt[bit] += M - ( N - 1 );
//         cnt[bit] -= cmp[( 1 << ( N - 1 ) ) - 1 - bit];
//         cnt[bit] += bitnum( bit );
//     }

//     /*****************************************
//      * dp
//      *****************************************/
//     dp1[0] = 1;
//     for ( int bit = 0; bit < ( 1 << ( N - 1 ) ); bit++ )
//     {
//         int c = bitnum( bit );
//         for ( int i = 0; i < N - 1; i++ )
//         {
//             if ( bit & ( 1 << i ) ) continue;
//             int nbit = bit | ( 1 << i );

//             dp1[nbit] +=
//                 fact( cnt[nbit] - 1 ) * fact_inv( cnt[bit] ) * dp1[bit];

//             dp2[nbit] +=
//                 fact( cnt[nbit] ) * fact_inv( cnt[bit] + 1 ) * dp2[bit];
//             dp2[nbit] += fact( cnt[nbit] - 1 ) * fact_inv( cnt[bit] ) *
//                          dp1[bit] * ( c + 1 );
//         }
//     }

//     cout << dp2[( 1 << ( N - 1 ) ) - 1].value() << endl;

//     return 0;
// }
#include <bitset>
#include <iostream>
#include <vector>
using namespace std;

template <int MOD>
struct Fp
{
    long long val;
    constexpr Fp( long long v = 0 ) noexcept : val( v % MOD )
    {
        if ( val < 0 ) v += MOD;
    }
    constexpr int getmod() { return MOD; }
    constexpr Fp operator-() const noexcept { return val ? MOD - val : 0; }
    constexpr Fp operator+( const Fp &r ) const noexcept
    {
        return Fp( *this ) += r;
    }
    constexpr Fp operator-( const Fp &r ) const noexcept
    {
        return Fp( *this ) -= r;
    }
    constexpr Fp operator*( const Fp &r ) const noexcept
    {
        return Fp( *this ) *= r;
    }
    constexpr Fp operator/( const Fp &r ) const noexcept
    {
        return Fp( *this ) /= r;
    }
    constexpr Fp &operator+=( const Fp &r ) noexcept
    {
        val += r.val;
        if ( val >= MOD ) val -= MOD;
        return *this;
    }
    constexpr Fp &operator-=( const Fp &r ) noexcept
    {
        val -= r.val;
        if ( val < 0 ) val += MOD;
        return *this;
    }
    constexpr Fp &operator*=( const Fp &r ) noexcept
    {
        val = val * r.val % MOD;
        return *this;
    }
    constexpr Fp &operator/=( const Fp &r ) noexcept
    {
        long long a = r.val, b = MOD, u = 1, v = 0;
        while ( b )
        {
            long long t = a / b;
            a -= t * b;
            swap( a, b );
            u -= t * v;
            swap( u, v );
        }
        val = val * u % MOD;
        if ( val < 0 ) val += MOD;
        return *this;
    }
    constexpr bool operator==( const Fp &r ) const noexcept
    {
        return this->val == r.val;
    }
    constexpr bool operator!=( const Fp &r ) const noexcept
    {
        return this->val != r.val;
    }
    friend constexpr ostream &operator<<( ostream &os,
                                          const Fp<MOD> &x ) noexcept
    {
        return os << x.val;
    }
    friend constexpr istream &operator>>( istream &is, Fp<MOD> &x ) noexcept
    {
        return is >> x.val;
    }
    friend constexpr Fp<MOD> modpow( const Fp<MOD> &a, long long n ) noexcept
    {
        if ( n == 0 ) return 1;
        auto t = modpow( a, n / 2 );
        t = t * t;
        if ( n & 1 ) t = t * a;
        return t;
    }
};

// 二項係数ライブラリ
template <class T>
struct BiCoef
{
    vector<T> fact_, inv_, finv_;
    constexpr BiCoef( int n ) noexcept
        : fact_( n, 1 ), inv_( n, 1 ), finv_( n, 1 )
    {
        int MOD = fact_[0].getmod();
        for ( int i = 2; i < n; i++ )
        {
            fact_[i] = fact_[i - 1] * i;
            inv_[i] = -inv_[MOD % i] * ( MOD / i );
            finv_[i] = finv_[i - 1] * inv_[i];
        }
    }
    constexpr T com( int n, int k ) const noexcept
    {
        if ( n < k || n < 0 || k < 0 ) return 0;
        return fact_[n] * finv_[k] * finv_[n - k];
    }
    constexpr T fact( int n ) const noexcept
    {
        if ( n < 0 ) return 0;
        return fact_[n];
    }
    constexpr T inv( int n ) const noexcept
    {
        if ( n < 0 ) return 0;
        return inv_[n];
    }
    constexpr T finv( int n ) const noexcept
    {
        if ( n < 0 ) return 0;
        return finv_[n];
    }
};

const int MAX = 201010;
const int MOD = 1000000007;
using mint = Fp<MOD>;

int N, M;
using pint = pair<int, int>;
using Graph = vector<vector<pint>>;
Graph G;

int dfs( int v, int p, int goal )
{
    if ( v == goal ) return 0;
    int res = -1;
    for ( auto e : G[v] )
    {
        if ( e.first == p ) continue;
        int tmp = dfs( e.first, v, goal );
        if ( tmp != -1 )
        {
            if ( res == -1 )
                res = tmp | ( 1 << e.second );
            else
                res |= tmp | ( 1 << e.second );
        }
    }
    return res;
}

int main()
{
    BiCoef<mint> bc( MAX );

    // 入力と、MST 以外の辺が MST と作るサイクルたち
    cin >> N >> M;
    G.assign( N, vector<pint>() );
    for ( int i = 0; i < N - 1; ++i )
    {
        int a, b;
        cin >> a >> b;
        --a, --b;
        G[a].push_back( {b, i} );
        G[b].push_back( {a, i} );
    }
    vector<int> cmp( 1 << ( N - 1 ), 0 );
    for ( int i = N - 1; i < M; ++i )
    {
        int a, b;
        cin >> a >> b;
        --a, --b;
        int S = dfs( a, -1, b );
        cmp[S]++;
    }

    // 高速ゼータ変換
    for ( int i = 0; i < N - 1; ++i )
        for ( int bit = 0; bit < 1 << ( N - 1 ); ++bit )
            if ( bit & ( 1 << i ) ) cmp[bit] += cmp[bit ^ ( 1 << i )];
    vector<int> cnt( 1 << ( N - 1 ), 0 );
    for ( int bit = 0; bit < 1 << ( N - 1 ); ++bit )
    {
        cnt[bit] = M - ( N - 1 ) - cmp[( 1 << ( N - 1 ) ) - 1 - bit] +
                   __builtin_popcount( bit );
    }

    // DP
    vector<mint> cdp( 1 << ( N - 1 ), 0 ), sdp( 1 << ( N - 1 ), 0 );
    cdp[0] = 1;
    for ( int bit = 0; bit < 1 << ( N - 1 ); ++bit )
    {
        long long con = __builtin_popcount( bit );
        for ( int i = 0; i < N - 1; ++i )
        {
            if ( bit & ( 1 << i ) ) continue;
            int nbit = bit | ( 1 << i );
            cdp[nbit] +=
                bc.fact( cnt[nbit] - 1 ) * bc.finv( cnt[bit] ) * cdp[bit];
            sdp[nbit] +=
                bc.fact( cnt[nbit] ) * bc.finv( cnt[bit] + 1 ) * sdp[bit] +
                bc.fact( cnt[nbit] - 1 ) * bc.finv( cnt[bit] ) * cdp[bit] *
                    ( con + 1 );
        }
    }
    cout << sdp[( 1 << ( N - 1 ) ) - 1] << endl;
}
