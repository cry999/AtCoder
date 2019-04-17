#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

#define MAX_H 1000
#define MAX_W 1000
#define MOD 1000000007

int H, W;
ll A[MAX_H][MAX_W];
ll memo[MAX_H][MAX_W];

bool in_range(int h, int w) { return 0 <= h && h < H && 0 <= w && w < W; }

ll dfs(int ch, int cw)
{
    if (memo[ch][cw])
        return memo[ch][cw];

    memo[ch][cw] = 1;
    pair<int, int> dirs[] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    for (int i = 0; i < 4; i++)
    {
        int dh = dirs[i].first, dw = dirs[i].second;

        if (!in_range(ch + dh, cw + dw))
            continue;

        if (A[ch + dh][cw + dw] <= A[ch][cw])
            continue;

        memo[ch][cw] += dfs(ch + dh, cw + dw);
        memo[ch][cw] %= MOD;
    }

    return memo[ch][cw];
}

int main(int argc, char **argv)
{
    cin >> H >> W;

    for (int h = 0; h < H; h++)
        for (int w = 0; w < W; w++)
            cin >> A[h][w];

    ll sum = 0;
    for (int h = 0; h < H; h++)
        for (int w = 0; w < W; w++)
            sum = (sum + dfs(h, w)) % MOD;

    cout << sum << endl;

    return 0;
}
