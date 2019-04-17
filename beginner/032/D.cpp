#include <algorithm>
#include <iostream>

using namespace std;

#define INF 0x3f3f3f3f

typedef long long ll;
typedef pair<ll, ll> item;

/***********************
 * questions parameter *
 ***********************/
#define MAX_N 200
int N, W;
item items[MAX_N];

/***********************
 * weight dp parameter *
 ***********************/
#define MAX_W 1000 * MAX_N
ll dpW[MAX_N + 1][MAX_W + 1];

ll weight_knapsack()
{
    for (int i = 0; i < N; i++)
    {
        ll v0 = items[i].first, w0 = items[i].second;

        for (int w = 0; w < MAX_W + 1; w++)
        {
            if (w < w0)
                dpW[i + 1][w] = dpW[i][w];
            else
                dpW[i + 1][w] = max(dpW[i][w], dpW[i][w - w0] + v0);
        }
    }
    return dpW[N][min(W, MAX_W)];
}

/**********************
 * value dp parameter *
 **********************/
#define MAX_V 1000 * MAX_N
ll dpV[MAX_N + 1][MAX_V + 1];

ll value_knapsack()
{
    // init
    fill(dpV[0], dpV[0] + MAX_V + 1, INF);
    dpV[0][0] = 0;

    for (int i = 0; i < N; i++)
    {
        ll v0 = items[i].first, w0 = items[i].second;

        for (int v = 0; v < MAX_V + 1; v++)
        {
            if (v < v0)
                dpV[i + 1][v] = dpV[i][v];
            else
                dpV[i + 1][v] = min(dpV[i][v], dpV[i][v - v0] + w0);
        }
    }

    int res = 0;
    for (int v = 0; v < MAX_V + 1; v++)
        if (dpV[N][v] <= W)
            res = v;
    return res;
}

/***********************
 * enum half parameter *
 ***********************/
item allA[1 << 15];

ll enum_half_knapsack()
{
    const int aN = N / 2, bN = N - aN;
    int ai = 0, bi = 0;
    item A[aN], B[bN];

    for (int n = 0; n < N; n++)
    {
        if (n < aN)
            A[ai++] = items[n];
        else
            B[bi++] = items[n];
    }

    // A を全列挙
    // 全列挙したものはソートしやすいように (重さ、価値)
    // の順になっていることに注意
    int allA_i = 0;
    for (int i = 0; i < 1 << aN; i++)
    {
        ll tv = 0, tw = 0;
        for (int j = 0; j < aN; j++)
        {
            if ((i & (1 << j)) == 0)
                continue;
            ll v = A[j].first, w = A[j].second;
            tv += v, tw += w;
        }
        if (tw <= W)
            allA[allA_i++] = {tw, tv};
    }
    sort(allA, allA + allA_i);

    // allA のなかで i<j かつ vi>vj となる j を消去
    int offset = 1;
    for (int i = 0; i + offset < allA_i; i++)
    {
        if (allA[i].second >= allA[i + offset].second)
        {
            offset++;
            i--;
        }
        else
        {
            allA[i + 1] = allA[i + offset];
        }
    }
    allA_i -= (offset - 1);

    // B を全列挙しながら A とマージ
    ll max_value = 0;
    for (int i = 0; i < 1 << bN; i++)
    {
        ll tv = 0, tw = 0;
        for (int j = 0; j < bN; j++)
        {
            if ((i & (1 << j)) == 0)
                continue;
            ll v = B[j].first, w = B[j].second;
            tv += v, tw += w;
        }

        if (W < tw)
            continue;

        // B と合わせられる最適な A の組み合わせを二分探索。
        int l = 0, r = allA_i;
        while (r - l > 1)
        {
            int m = (r + l) / 2;
            ll mw = allA[m].first;

            if (tw + mw <= W)
                l = m;
            else
                r = m;
        }
        max_value = max(max_value, tv + allA[l].second);
    }

    return max_value;
}

int main(int argc, char **argv)
{
    cin >> N >> W;

    ll max_v = 0, max_w = 0;
    for (int n = 0; n < N; n++)
    {
        ll v, w;
        cin >> v >> w;

        items[n] = {v, w};
        max_v = max(v, max_v);
        max_w = max(w, max_w);
    }

    ll ans = 0;

    if (max_w <= 1000)
        ans = weight_knapsack();
    else if (max_v <= 1000)
        ans = value_knapsack();
    else
        ans = enum_half_knapsack();

    cout << ans << endl;

    return 0;
}
