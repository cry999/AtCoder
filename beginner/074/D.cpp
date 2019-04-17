#include <cstdio>
#include <iostream>

using namespace std;

typedef long long ll;

ll solve(int N, int A[300][300]) {
    ll ans = 0;
    for (int i = 0; i < N; i++) {
        for (int j = i+1; j < N; j++) {
            bool ok = true;
            for (int k = 0; k < N; k++) {
                if (i == k || j == k) continue;

                if (A[i][k] + A[k][j] < A[i][j]) {
                    return -1;
                }

                if (A[i][k] + A[k][j] == A[i][j]) {
                    ok = false;
                }
            }
            if (ok) ans += A[i][j];
        }
    }
    return ans;
}

int main(int argc, char **argv) {
    int N;
    int A[300][300];
    cin >> N;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> A[i][j];
        }
    }

    ll ans = solve(N, A);

    cout << ans << endl;

    return 0;
}
