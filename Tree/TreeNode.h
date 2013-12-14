#ifndef TREENODE_H
#define TREENODE_H
#include<iostream>
using namespace std;

template<class NODETYPE> class Tree;
template<class NODETYPE>
class TreeNode{
  friend class Tree<NODETYPE>;
 public:
 TreeNode(const NODETYPE& d):leftptr(0),data(d),rightptr(0){}
  NODETYPE getData() const{
    return data;
  }
 private:
  NODETYPE data;
  TreeNode<NODETYPE> *leftptr;
  TreeNode<NODETYPE> *rightptr;
};

#endif
