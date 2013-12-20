#include<iostream>
#include<string.h>
using namespace std;

//give a string s
//compute its suffix array
//example
// aabaaaab
// 34506172

void print(int A[],int n){
  for(int i=0;i<n;i++)
    cout<<A[i]<<" ";
  cout<<endl;
}
//where the alpha set size 
void sa(char *s,int sa[])
{
  int n=strlen(s);
  int *x,*y;
  int cnt[256];
  int ma[100],mb[100];
  x=ma,y=mb;
  
  //radix sort
  memset(cnt,0,sizeof(cnt));
  for(int i=0;i<n;i++)
    cnt[x[i]=s[i]]++;
  for(int i=1;i<256;i++) cnt[i]+=cnt[i-1];
  for(int i=n-1;i>=0;i--) sa[--cnt[x[i]]]=i;
  
  print(sa,n);
  
  //double radix sort
  int p,j,i;
  for(p=1,j=1;p<n;j*=2)
  {
    cout<<"OK"<<endl;
    for(p=0,i=n-j;i<n;i++) y[p++]=i; //sort 2nd key
    for(i=0;i<n;i++) if(sa[i]>=j) y[p++]=sa[i]-j;
    memset(cnt,0,sizeof(cnt));
    for(i=0;i<n;i++) cnt[x[y[i]]]++;
    for(i=1;i<256;i++) cnt[i]+=cnt[i-1];
    for(i=n-1;i>=0;i--) sa[--cnt[x[y[i]]]]=y[i];
    print(sa,n);
    swap(x,y);
    x[sa[0]]=0;
    p=1;
    for(i=1;i<n;i++)
      x[sa[i]]=(y[sa[i]]==y[sa[i-1]] && y[sa[i]+j]==y[sa[i-1]+j]) ?p-1:p++;
    
    
    
  }

  print(sa,n);

}
int main()
{
  char s[100]="aabaaaab#";
  int a[100];  
  sa(s,a);
  for(int i=0;i<strlen(s);i++)
    cout<<a[i]<<" ";
  cout<<endl;
}
