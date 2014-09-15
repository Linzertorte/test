#include<iostream>
#include<stdio.h>
using namespace std;
int t,n,k;
int A[120];
int dp[110][120]; //[s,t)
int f(int s,int t){
    if(s==t) return dp[s][t] = 1;
    if(dp[s][t]!=-1) return dp[s][t];
    dp[s][t] = 0;
    
    for(int i=s+1;i<t;i++)
        for(int j=i+1;j<t;j++){
            if(A[j]-A[i]==k && A[i]-A[s]==k && f(s+1,i) && f(i+1,j) && f(j+1,t) ){
                return dp[s][t] = 1;
            }
        }
    return dp[s][t];
    
}
int main()
{
    scanf("%d",&t);
    for(int q=1;q<=t;q++){
        scanf("%d%d",&n,&k);
        for(int i=0;i<n;i++){
            scanf("%d",A+i);
        }
        memset(dp,-1,sizeof dp);
        int d[120];
        memset(d,0,sizeof d);
        for(int i=0;i<=n;i++)
            if(f(0,i)) d[i] = max(d[i],i);
        for(int i=1;i<=n;i++){
            d[i] = max(d[i],d[i-1]);
            for(int j=i;j<=n;j++)
                if(f(i,j)) d[j] = max(d[j],d[i]+j-i);
        }
        printf("Case #%d: %d\n",q,n-d[n]);
    }
    return 0;
}
