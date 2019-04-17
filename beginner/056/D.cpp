#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

// const
#define MAX_N 5000
#define MAX_K 5000

// input
int N, K;
ll A[MAX_N];

// variable
bool dp[MAX_N][MAX_K];

ll max(ll a, ll b) { return a > b ? a : b; }

bool need(int i) {
    // initialize dp
    for (int n = 0; n < N; n++)
        for (int k = 0; k < K; k++)
            dp[n][k] = false;
    dp[0][0] = true;

    // calc dp
    int elm_num = 0;
    for (int a_idx = 0; a_idx < N; a_idx++) {
        if (a_idx == i) continue;

        ll a = A[a_idx];

        for (int k = 0; k < K; k++)
            dp[elm_num+1][k] = dp[elm_num][k] || (a <= k && dp[elm_num][k-a]);
        elm_num++;
    }

    for (ll k = max(K-A[i], 0); k < K; k++)
        if (dp[N-1][k]) return true;
    return false;
}

int no_need() {
    sort(A, A+N);

    int l = -1, r = N;
    while (l + 1 < r) {
        int m = (l + r) / 2;
        
        if (need(m)) r = m;
        else l = m;
    }
    return l + 1;
}

int main(int argc, char **argv) {
    cin >> N >> K;

    for (int i = 0; i < N; i++) cin >> A[i];

    int ans = no_need();

    cout << ans << endl;
}
