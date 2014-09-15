#include<iostream>
#include<stdio.h>
using namespace std;
const long long MOD = (long long)(1e9) + 7;
int t,m,n;
inline long long mypow(long long x,int n){
    long long a = 1;
    for(int i=1;i<=n;i++){
        a = (a*x)%MOD;
    }
    return a;
}
long long dp[120][120];
inline long long C(int n,int m){
    if(m==n || m == 0) return dp[n][m] = 1;
    if(dp[n][m]!=-1) return dp[n][m];
    return dp[n][m] = (C(n-1,m) + C(n-1,m-1)) % MOD;
}
int main()
{
    scanf("%d",&t);
    memset(dp,-1,sizeof(dp));
    for(int q=1;q<=t;q++){
        scanf("%d%d",&m,&n);
        
        //m^n - C(m,1)(m-1)^n + C(m,2)(m-2)^n ...C(m,m-1) 1^n
        long long answer = 0;
        int sign = 1;
        for(int i=0;i<=m-1;i++){
            answer += (sign*C(m,i)*mypow(m-i,n))%MOD;
            answer %= MOD;
            if(answer<0) answer+=MOD;
            sign = -sign;
        }
        
        printf("Case #%d: %lld\n",q,answer);
    }
    return 0;
}
