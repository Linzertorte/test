#include <stdio.h>
#include <stdlib.h>
int size;  /* number of nodes in the tree */
           /* Not actually needed for any of the operations */

typedef struct tree_node Tree;
struct tree_node {
  Tree * left, * right;
  int item;
};

Tree * splay (int i, Tree * t) {
  /* Simple top down splay, not requiring i to be in the tree t.  */
  /* What it does is described above.                             */
  Tree N, *l, *r, *y;
  if (t == NULL) return t;
  N.left = N.right = NULL;
  l = r = &N;

  for (;;) {
    if (i < t->item) {
      if (t->left == NULL) break;
      if (i < t->left->item) {
	y = t->left;                           /* rotate right */
	t->left = y->right;
	y->right = t;
	t = y;
	if (t->left == NULL) break;
      }
      r->left = t;                               /* link right */
      r = t;
      t = t->left;
    } else if (i > t->item) {
      if (t->right == NULL) break;
      if (i > t->right->item) {
	y = t->right;                          /* rotate left */
	t->right = y->left;
	y->left = t;
	t = y;
	if (t->right == NULL) break;
      }
      l->right = t;                              /* link left */
      l = t;
      t = t->right;
    } else {
      break;
    }
  }
  l->right = t->left;                                /* assemble */
  r->left = t->right;
  t->left = N.right;
  t->right = N.left;
  return t;
}

/* Here is how sedgewick would have written this.                    */
/* It does the same thing.                                           */
Tree * sedgewickized_splay (int i, Tree * t) {
  Tree N, *l, *r, *y;
  if (t == NULL) return t;
  N.left = N.right = NULL;
  l = r = &N;

  for (;;) {
    if (i < t->item) {
      if (t->left != NULL && i < t->left->item) {
	y = t->left; t->left = y->right; y->right = t; t = y;
      }
      if (t->left == NULL) break;
      r->left = t; r = t; t = t->left;
    } else if (i > t->item) {
      if (t->right != NULL && i > t->right->item) {
	y = t->right; t->right = y->left; y->left = t; t = y;
      }
      if (t->right == NULL) break;
      l->right = t; l = t; t = t->right;
    } else break;
  }
  l->right=t->left; r->left=t->right; t->left=N.right; t->right=N.left;
  return t;
}

Tree * insert(int i, Tree * t) {
  /* Insert i into the tree t, unless it's already there.    */
  /* Return a pointer to the resulting tree.                 */
  Tree * new;
    
  new = (Tree *) malloc (sizeof (Tree));
  if (new == NULL) {
    printf("Ran out of space\n");
    exit(1);
  }
  new->item = i;
  if (t == NULL) {
    new->left = new->right = NULL;
    size = 1;
    return new;
  }
  t = splay(i,t);
  if (i < t->item) {
    new->left = t->left;
    new->right = t;
    t->left = NULL;
    size ++;
    return new;
  } else if (i > t->item) {
    new->right = t->right;
    new->left = t;
    t->right = NULL;
    size++;
    return new;
  } else { /* We get here if it's already in the tree */
    /* Don't add it again                      */
    free(new);
    return t;
  }
}

Tree * delete(int i, Tree * t) {
  /* Deletes i from the tree if it's there.               */
  /* Return a pointer to the resulting tree.              */
  Tree * x;
  if (t==NULL) return NULL;
  t = splay(i,t);
  if (i == t->item) {               /* found it */
    if (t->left == NULL) {
      x = t->right;
    } else {
      x = splay(i, t->left);
      x->right = t->right;
    }
    size--;
    free(t);
    return x;
  }
  return t;                         /* It wasn't there */
}

void main() {
  /* A sample use of these functions.  Start with the empty tree,         */
  /* insert some stuff into it, and then delete it                        */
  Tree * root;
  int i;
  root = NULL;              /* the empty tree */
  size = 0;
  for (i = 0; i < 1024; i++) {
    root = insert((541*i) & (1023), root);
  }
  for (i = 0; i < 1024; i++) {
    root = delete((541*i) & (1023), root);
  }
  printf("size = %d\n", size);
}
