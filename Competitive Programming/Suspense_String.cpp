#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,fma")
#pragma GCC optimize("unroll-loops")
#include <bits/stdc++.h>
#include <complex>
#include <queue>
#include <set>
#include <unordered_set>
#include <list>
#include <chrono>
#include <random>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <stack>
#include <iomanip>
#include <fstream>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> p32;
typedef pair<ll,ll> p64;
typedef pair<double,double> pdd;
typedef vector<ll> v64;
typedef vector<int> v32;
typedef vector<vector<int> > vv32;
typedef vector<vector<ll> > vv64;
typedef vector<vector<p64> > vvp64;
typedef vector<p64> vp64;
typedef vector<p32> vp32;
ll MOD = 998244353;
double eps = 1e-12;
#define forn(i,e) for(ll i = 0; i < e; i++)
#define forsn(i,s,e) for(ll i = s; i < e; i++)
#define rforn(i,s) for(ll i = s; i >= 0; i--)
#define rforsn(i,s,e) for(ll i = s; i >= e; i--)
#define ln "\n"
#define dbg(x) cout<<#x<<" = "<<x<<ln
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define INF 2e18
#define fast_cin() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define all(x) (x).begin(), (x).end()
#define sz(x) ((ll)(x).size())


void solve(){
    int n;
    cin>>n;
    string s;
    cin>>s;
    string ans;
    if(n%2==0){
        int l=0;
        int r=n-1;
        while(l<r){
            if(s[l]=='0') ans=s[l]+ans;
            else ans=ans+s[l];
            l++;
            if(s[r]=='0') ans=ans+s[r];
            else ans=s[r]+ans;
            r--;
        }
    }else{
        int h=n/2;
        int l=0;
        int r=n-1;
        while(l<h){
            if(s[l]=='0') ans=s[l]+ans;
            else ans=ans+s[l];
            l++;
            if(s[r]=='0') ans=ans+s[r];
            else ans=s[r]+ans;
            r--;
        }
        if(s[h]=='0') ans=s[h]+ans;
        else ans=ans+s[h];
    }

    cout<<ans<<endl;
}
int main()
{
	fast_cin();
	ll t;
	cin >> t;
	for(int it=1;it<=t;it++) {
		solve();
	}
	return 0;
}
