#include<iostream>
#include<map>
#include<stdio.h>
#include<string.h>
using namespace std;
typedef long long LL;

int n,m;
int a[20],b[20];
int x,y,cur,nex,nx,ny;
map<int,LL> f[2];
inline LL calc(){
    LL s = 0, k = 0;
    for(int i=0;i<8;i++) b[i] = 0;
    for(int i=0;i<=m;i++)
        if(a[i]) a[i] = b[a[i]]?b[a[i]]:b[a[i]]=++k;
    for(int i=m;i>=0;i--) s<<=3, s|=a[i];
    return s;
}
void decode(LL t){
    for(int i=0;i<=m;i++) a[i] = t&7,t>>=3;
}
void up(int w,int t,LL s)
{
    if (x && y) {  //merge
        if (x!=y) {
            for(int i=0;i<=m;i++)
                if ( a[i] == y ) a[i] = x;
            a[0] = a[t] = 0;
            f[nex][calc()]+=s;
        }
    } else if ( x || y ) {
        f[nex][calc()]+=s;
        swap( a[0] , a[t] );
        f[nex][calc()]+=s;
        if(w==n && t==n){
            //last block
            a[0]=a[t] = 0;
            f[nex][calc()]+=s;
        }
    } else {
        a[0] = a[t] = 7;
        f[nex][calc()]+=s;
        a[0] = a[t] = 0;
        f[nex][calc()]+=s;
    }
}

int main()
{
    while(scanf("%d",&n),n){
        n++;
        m = n;
        f[0].clear();
        cur = 0, nex = 1;
        memset(a,0,sizeof a);
        a[1] = 1;
        f[0][calc()] += 1;
        memset(a,0,sizeof a);
        a[0] = 1;
        f[0][calc()] += 1; //the first block is independent
        
        //work
        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++){
                if(i==1 && j==1) continue;
                f[nex].clear();
                for(map<int,LL>::iterator it=f[cur].begin();it!=f[cur].end();it++){
                    decode(it->first);
                    if(j==1 && a[0]) continue;
                    x=a[0], y = a[j];
                    //x is left y is upper
                    up(i,j,it->second);
                }
                swap(cur,nex);
            }
        printf("%lld\n",f[cur][0]);
    }
    return 0;
}
