#include<stdio.h>
#include<iostream>
using namespace std;

int partition(int A[],int p,int r){
	int x=A[r];
	int i=p-1;
	for(int j=p;j<=r-1;j++)
		if(A[j]<x) swap(A[++i],A[j]);
	swap(A[i+1],A[r]);
	return i+1;
}


void quicksort(int A[],int p,int r){
	if(p<r){
		int q=partition(A,p,r);
		quicksort(A,p,q-1);
		quicksort(A,q+1,r);
	}
}

int main()
{
	int A[10]={6,7,2,3,5,1,8,3,4,2};
	quicksort(A,0,9);
	for(int i=0;i<10;i++)
		cout<<A[i]<<" ";
	cout<<endl;
	return 0;

}
