#include <cstring>
#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair< ll, ll > point;
typedef pair< point, point > rect;

rect new_rect(ll x1, ll y1, ll x2, ll y2)
{
  point p1 = point(x1, y1);
  point p2 = point(x2, y2);
  return rect(p1, p2);
}

ll max(ll a, ll b)
{
  return a > b ? a : b;
}

ll min(ll a, ll b)
{
  return a > b ? b : a;
}

vector< rect > points(ll cx, ll cy, ll K)
{
  vector< rect > res;
  ll x1 = max(0, cx - K);
  ll y1 = max(0, cy - K);
  ll x2 = cx;
  ll y2 = cy;
  res.push_back(new_rect(x1, y1, x2, y2));

  x2 = min(2 * K, cx + K), y2 = min(2 * K, cy + K);
  x1 = cx, y1 = cy;
  res.push_back(new_rect(x1, y1, x2, y2));

  if (K < cy)
  {
    x2 = min(2 * K, cx + K), y2 = cy - K;
    x1 = cx, y1 = max(0, y2 - K);
    res.push_back(new_rect(x1, y1, x2, y2));
  }

  if (cx < K)
  {
    x2 = min(2 * K, cx + 2 * K), y2 = cy;
    x1 = cx + K, y1 = max(0, cy - K);
    res.push_back(new_rect(x1, y1, x2, y2));
  }

  if (K < cx)
  {
    x2 = cx - K, y2 = min(2 * K, cy + K);
    x1 = max(0, x2 - K), y1 = cy;
    res.push_back(new_rect(x1, y1, x2, y2));
  }

  if (K < cx && K < cy)
  {
    x2 = cx - K, y2 = cy - K;
    x1 = max(0, x2 - K), y1 = max(0, y2 - K);
    res.push_back(new_rect(x1, y1, x2, y2));
  }

  return res;
}

ll white[2001][2001];
ll checker(ll N, ll K, vector< pair< point, char > > C)
{
  memset(white, 0, sizeof(white));

  for (pair< point, char > pc : C)
  {
    point p = pc.first;
    ll x = p.first, y = p.second;
    char c = pc.second;

    if (c == 'B')
      x += K;

    ll tx = (x % (2 * K)) + 1;
    ll ty = (y % (2 * K)) + 1;
    white[tx][ty] += 1;
  }

  for (ll ky = 0; ky < 2 * K; ky++)
    for (ll kx = 0; kx < 2 * K; kx++)
      white[ky + 1][kx + 1] += white[ky + 1][kx];

  for (ll ky = 0; ky < 2 * K; ky++)
    for (ll kx = 0; kx < 2 * K; kx++)
      white[ky + 1][kx + 1] += white[ky][kx + 1];

  ll max_count = 0;
  for (ll ky = K; ky < 2 * K; ky++)
  {
    for (ll kx = 0; kx < 2 * K; kx++)
    {
      ll count = 0;
      for (rect r : points(kx, ky, K))
      {
        ll x1 = r.first.first;
        ll y1 = r.first.second;
        ll x2 = r.second.first;
        ll y2 = r.second.second;

        count += white[y2][x2] - white[y2][x1] - white[y1][x2] + white[y1][x1];
      }
      max_count = max(max_count, count);
      if (max_count == N)
        break;
    }
  }
  return max_count;
}

int main(int argc, char** argv)
{
  ll N, K;
  cin >> N >> K;
  vector< pair< point, char > > C;
  for (ll n = 0; n < N; n++)
  {
    ll x, y;
    char c;
    cin >> x >> y >> c;
    C.push_back(pair< point, char >(point(x, y), c));
  }
  ll ans = checker(N, K, C);

  cout << ans << endl;

  return 0;
}
