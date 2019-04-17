#include <algorithm>
#include <iostream>
#include <vector>

#define BIT_LIM 40

using namespace std;

typedef long long ll;

int main(int argc, char **argv)
{
    vector<ll> A, B;
    ll n;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        ll a;
        cin >> a;
        A.push_back(a);
    }

    for (int i = 0; i < n; i++)
    {
        ll b;
        cin >> b;
        B.push_back(b);
    }

    ll res = 0;
    for (int k = 0; k < BIT_LIM; k++)
    {
        ll T = 1LL << (k + 1);
        ll num_kth_bit_is_1 = 0;
        vector<ll> Bk;
        for (auto &&b : B)
        {
            Bk.push_back(b & (T - 1));
        }
        sort(Bk.begin(), Bk.end());

        for (auto &&ai : A)
        {
            ll ai_mod = ai & (T - 1);

            T = T >> 1;
            num_kth_bit_is_1 +=
                lower_bound(Bk.begin(), Bk.end(), 2 * T - ai_mod) -
                lower_bound(Bk.begin(), Bk.end(), T - ai_mod);

            num_kth_bit_is_1 +=
                lower_bound(Bk.begin(), Bk.end(), 4 * T - ai_mod) -
                lower_bound(Bk.begin(), Bk.end(), 3 * T - ai_mod);
            T = T << 1;
        }

        res = ((num_kth_bit_is_1 & 1) << k) | res;
    }

    cout << res << endl;

    return 0;
}
