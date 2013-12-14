#ifndef TREE_H
#define TREE_H
#include<iostream>
#include "TreeNode.h"
using namespace std;
template<class NODETYPE> class Tree{
 public:
  Tree();
  void insertNode(const NODETYPE &d);
  void preOrderTraversal() const;
  void inOrderTraversal() const;
  void postOrderTraversal() const;
 private:
  TreeNode<NODETYPE> *rootptr;
  
  void insertNodeHelper(TreeNode<NODETYPE> **,const NODETYPE &d);
  void preOrderTraversalHelper(TreeNode<NODETYPE> *) const;
  void inOrderTraversalHelper(TreeNode<NODETYPE> *) const;
  void postOrderTraversalHelper(TreeNode<NODETYPE> *) const;
};

template<class NODETYPE>
Tree<NODETYPE>::Tree(){
  rootptr=0;
}
template<class NODETYPE>
void Tree<NODETYPE>::insertNode(const NODETYPE &d){
  insertNodeHelper(&rootptr,d);
}
template<class NODETYPE>
void Tree<NODETYPE>::preOrderTraversal() const{
  preOrderTraversalHelper(rootptr);
  cout<<endl;
}
template<class NODETYPE>
void Tree<NODETYPE>::inOrderTraversal() const{
  inOrderTraversalHelper(rootptr);
  cout<<endl;
}
template<class NODETYPE>
void Tree<NODETYPE>::postOrderTraversal() const{
  postOrderTraversalHelper(rootptr);
  cout<<endl;
}

template<class NODETYPE>
void Tree<NODETYPE>::insertNodeHelper(TreeNode<NODETYPE> **ptr,const NODETYPE &d){
  if(*ptr==0) *ptr=new TreeNode<NODETYPE>(d);
  else if((*ptr)->data>d) insertNodeHelper(&(*ptr)->leftptr,d);
  else if((*ptr)->data<d) insertNodeHelper(&(*ptr)->rightptr,d);
  else cout<<d<<" dup"<<endl;
}
template<class NODETYPE>
void Tree<NODETYPE>::preOrderTraversalHelper(TreeNode<NODETYPE> *ptr) const
{
  if(ptr){
    cout<<ptr->data<<" ";
    preOrderTraversalHelper(ptr->leftptr);
    
    preOrderTraversalHelper(ptr->rightptr);
  }
}
template<class NODETYPE>
void Tree<NODETYPE>::inOrderTraversalHelper(TreeNode<NODETYPE> *ptr) const{
  if(ptr){
    inOrderTraversalHelper(ptr->leftptr);
    cout<<ptr->data<<" ";
    inOrderTraversalHelper(ptr->rightptr);
  }
}
template<class NODETYPE>
void Tree<NODETYPE>::postOrderTraversalHelper(TreeNode<NODETYPE> *ptr) const
{
  if(ptr) {
    postOrderTraversalHelper(ptr->leftptr);
    postOrderTraversalHelper(ptr->rightptr);
    cout<<ptr->data<<" ";
  }
}


#endif
