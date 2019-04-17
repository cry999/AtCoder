#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

struct edge
{
  int from;
  int to;
  int cap;
};

int solve(int N, int M, int R, vector< int > visits, vector< edge > edges)
{
  long long INF = 0x3f3f3f3f;
  long long A[N][N];
  for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++)
      if (i == j)
        A[i][j] = 0;
      else
        A[i][j] = INF;

  for (auto it = edges.begin(); it != edges.end(); it++)
  {
    edge e = *it;
    A[e.from - 1][e.to - 1] = e.cap;
    A[e.to - 1][e.from - 1] = e.cap;
  }

  for (int k = 0; k < N; k++)
    for (int i = 0; i < N; i++)
      for (int j = 0; j < N; j++)
        A[i][j] = min(A[i][j], A[i][k] + A[k][j]);

  long long min_d = INF;
  sort(visits.begin(), visits.end());
  do
  {
    long long d = 0;
    for (int r = 0; r < R - 1; r++)
      d += A[visits[r] - 1][visits[r + 1] - 1];

    min_d = min(min_d, d);

  } while (next_permutation(visits.begin(), visits.end()));

  return min_d;
}

int main(int argc, char **argv)
{
  int N, M, R;
  cin >> N >> M >> R;

  vector< int > visits(R);
  for (int i = 0; i < R; i++)
  {
    cin >> visits[i];
  }

  vector< edge > edges(M);
  for (int i = 0; i < M; i++)
  {
    int from, to, cap;
    cin >> from >> to >> cap;
    edges.push_back((edge){from, to, cap});
  }

  int ans = solve(N, M, R, visits, edges);

  cout << ans << endl;

  return 0;
}
