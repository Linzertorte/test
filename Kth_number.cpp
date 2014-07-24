#include<iostream>
#include<queue>
#include<stdlib.h>
#include<vector>
#include<algorithm>
#include<stdio.h>
using namespace std;
int selectK(int s,int t,vector<int> &seq,int k){
    if(t-s==1) return seq[s];
    int key = seq[s];
    int j=s;
    for(int i=s+1;i<t;i++)
        if(seq[i]<=key)
            swap(seq[++j],seq[i]);
    
    swap(seq[s],seq[j]);
    ++j;
    printf("(%d,%d,%d,%d)\n",s,t,j-1,k);
    if(j-s==k) return seq[j-1];
    else if(j-s>k) return selectK(s,j-1,seq,k);
    else return selectK(j,t,seq,k-j+s);
}

int main(){
    
    vector<int> seq(10);
    srand(time(NULL));
    //srand(10);
    for(int i=0;i<10;i++)
        seq[i]=rand()%100;
    for(int i=0;i<10;i++)
        cout<<seq[i]<<" ";
    cout<<endl;
    int key = selectK(0,10,seq,5);
    cout<<"The 5th number is"<<endl;
    cout<<key<<endl;
    
    int j = -1;
    for(int i=0;i<10;i++){
        if(seq[i]<=key) swap(seq[i],seq[++j]);
    }
    cout<<"partition by the 5th number"<<endl;
    for(int i=0;i<10;i++)
        cout<<seq[i]<<" ";
    cout<<endl;
    
    cout<<"totally order is"<<endl;
    sort(seq.begin(),seq.end());
    for(int i=0;i<10;i++)
        cout<<seq[i]<<" ";
    
    cout<<endl;
    
    return 0;
}
