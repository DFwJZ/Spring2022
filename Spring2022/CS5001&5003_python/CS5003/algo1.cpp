#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

const int N = 9;
double n, x, y;
double a[N], b[N];

int bs1(int l, int r, int x)
{
	while (l < r)
	{
		int mid = (l + r + 1) >> 1;
		if (b[mid] <= x)
			l = mid;
		else
			r = mid - 1;
	}

	return l;
}

int bs2(int l, int r, int y)
{
	while (l < r)
	{
		int mid = (l + r) >> 1;
		if (b[mid] >= y)
			r = mid;
		else
			l = mid + 1;
	}

	return r;
}

int main()
{
	cin >> n >> x >> y;

	if (x > y)
		return 0;

	for (int i = 0; i < n; ++i)
		cin >> a[i];

	for (int i = 0; i < n; ++i)
		b[i] = ceil(a[i]);

	int bsize = sizeof(b) / sizeof(b[0]);

	sort(b, b + bsize);
	// for (auto x : b)
	//     cout << x << ' ';

	int l = bs1(0, n, x);
	int r = bs2(0, n, y);

	int l_bound = x > b[l] ? x : b[l];
	int r_bound = b[r] > y ? b[r] : y;

	// cout << "lbound: " << l_bound << " rbound: " << r_bound << endl;

	int cnt = 0;
	for (auto x : a)
		if (x >= l_bound && x <= r_bound)
		{
			cout << x << ' ';
			cnt++;
		}

	puts("");
	cout << cnt << endl;

	return 0;
}