#include<iostream>
#include"Tree.h"
using namespace std;
int main()
{
  Tree<int> intTree;
  int intV;
  cout<<"Enter 10 int"<<endl;
  for(int i=0;i<10;i++){
    cin>>intV;
    intTree.insertNode(intV);
  }
 
  intTree.preOrderTraversal();
  intTree.inOrderTraversal();
  intTree.postOrderTraversal();
  cout<<endl;
}
