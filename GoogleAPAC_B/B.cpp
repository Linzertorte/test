#include<iostream>
#include<stdio.h>
using namespace std;

double cur[500][500];
double nxt[500][500];
int t,B,L,N;
inline void overflow(int i,int j,double a[][500],double b[][500]){
    if(a[i][j]>250){
        double over = (a[i][j]-250)/3.0;
        a[i][j] = 250;
        b[i][j] += over;
        b[i+1][j] += over;
        b[i+1][j+1] += over;
    }
}
int main()
{
    scanf("%d",&t);
    for(int q=1;q<=t;q++){
        scanf("%d%d%d",&B,&L,&N);
        double wine = B*750.0;
        memset(cur,0,sizeof cur);
        memset(nxt,0,sizeof nxt);
        cur[0][0] = wine;
        //overflow
        if(cur[0][0]>250){
            double over = (cur[0][0]-250)/3;
            cur[0][0] = 250;
            nxt[0][0] += over;
            nxt[1][0] += over;
            nxt[1][1] += over;
        }
        for(int l=2;l<=L;l++){
            //swap(cur,nxt);
            for(int i=0;i<500;i++)
                for(int j=0;j<500;j++)
                    cur[i][j] = nxt[i][j];
            
            memset(nxt,0,sizeof(double)*250000);
            for(int i=0;i<l;i++)
                for(int j=0;j<=i;j++){
                    overflow(i,j,cur,nxt);
                }
        }
        double final = 0;
        int cnt = 0;
        for(int i=0;i<L;i++)
            for(int j=0;j<=i;j++){
                cnt ++;
                if(cnt==N) final = cur[i][j];
            }
        printf("Case #%d: %.7f\n",q,final);
    }

    return 0;
}
