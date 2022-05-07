# Red black tree implementation, taken from: https://github.com/Bibeknam/algorithmtutorprograms/blob/master/data-structures/red-black-trees/red_black_tree.py
# Adapted for Python 3

TRBKey = int

# data structure that represents a node in the tree
class RBNode():
  def __init__(self, data: TRBKey, parent=None, left=None, right=None, color:int=0):
    self.data           = data     # holds the key
    self.parent: RBNode = parent   # pointer to the parent
    self.left: RBNode   = left     # pointer to left child
    self.right: RBNode  = right    # pointer to right child
    self.color          = color    # 1 . Red, 0 . Black
  
  def __repr__(self):
    return f"RBNode({self.data})"

# class RedBlackTree implements the operations in Red Black Tree
class RedBlackTree:
  def __init__(self):
    self.NULL_NODE = RBNode(0)
    self.root: RBNode = self.NULL_NODE

  def __search_tree_helper(self, node: RBNode, key: TRBKey):
    if node == self.NULL_NODE or key == node.data:
      return node

    if key < node.data:
      return self.__search_tree_helper(node.left, key)
    return self.__search_tree_helper(node.right, key)

  # fix the rb tree modified by the delete operation
  def __fix_delete(self, x: RBNode):
    while x != self.root and x.color == 0:
      if x == x.parent.left:
        s = x.parent.right
        if s.color == 1:
          # case 3.1
          s.color = 0
          x.parent.color = 1
          self.left_rotate(x.parent)
          s = x.parent.right

        if s.left.color == 0 and s.right.color == 0:
          # case 3.2
          s.color = 1
          x = x.parent
        else:
          if s.right.color == 0:
            # case 3.3
            s.left.color = 0
            s.color = 1
            self.right_rotate(s)
            s = x.parent.right

          # case 3.4
          s.color = x.parent.color
          x.parent.color = 0
          s.right.color = 0
          self.left_rotate(x.parent)
          x = self.root
      else:
        s = x.parent.left
        if s.color == 1:
          # case 3.1
          s.color = 0
          x.parent.color = 1
          self.right_rotate(x.parent)
          s = x.parent.left

        if s.left.color == 0 and s.right.color == 0:
          # case 3.2
          s.color = 1
          x = x.parent
        else:
          if s.left.color == 0:
            # case 3.3
            s.right.color = 0
            s.color = 1
            self.left_rotate(s)
            s = x.parent.left

          # case 3.4
          s.color = x.parent.color
          x.parent.color = 0
          s.left.color = 0
          self.right_rotate(x.parent)
          x = self.root
      x.color = 0

  def __rb_transplant(self, u: RBNode, v: RBNode):
    if u.parent == None:
      self.root = v
    elif u == u.parent.left:
      u.parent.left = v
    else:
      u.parent.right = v
    v.parent = u.parent

  def __delete_node_helper(self, node: RBNode, key: TRBKey):
    # find the node containing key
    z = self.NULL_NODE
    while node != self.NULL_NODE:
      if node.data == key:
        z = node

      if node.data <= key:
        node = node.right
      else:
        node = node.left

    if z == self.NULL_NODE:
      raise KeyError(f"key {key} not present in tree")

    y = z
    y_original_color = y.color
    if z.left == self.NULL_NODE:
      x = z.right
      self.__rb_transplant(z, z.right)
    elif (z.right == self.NULL_NODE):
      x = z.left
      self.__rb_transplant(z, z.left)
    else:
      y = self.minimum(z.right)
      y_original_color = y.color
      x = y.right
      if y.parent == z:
        x.parent = y
      else:
        self.__rb_transplant(y, y.right)
        y.right = z.right
        y.right.parent = y

      self.__rb_transplant(z, y)
      y.left = z.left
      y.left.parent = y
      y.color = z.color
    if y_original_color == 0:
      self.__fix_delete(x)
  
  # fix the red-black tree
  def  __fix_insert(self, k: RBNode):
    while k.parent.color == 1:
      if k.parent == k.parent.parent.right:
        u = k.parent.parent.left # uncle
        if u.color == 1:
          # case 3.1
          u.color = 0
          k.parent.color = 0
          k.parent.parent.color = 1
          k = k.parent.parent
        else:
          if k == k.parent.left:
            # case 3.2.2
            k = k.parent
            self.right_rotate(k)
          # case 3.2.1
          k.parent.color = 0
          k.parent.parent.color = 1
          self.left_rotate(k.parent.parent)
      else:
        u = k.parent.parent.right # uncle

        if u.color == 1:
          # mirror case 3.1
          u.color = 0
          k.parent.color = 0
          k.parent.parent.color = 1
          k = k.parent.parent 
        else:
          if k == k.parent.right:
            # mirror case 3.2.2
            k = k.parent
            self.left_rotate(k)
          # mirror case 3.2.1
          k.parent.color = 0
          k.parent.parent.color = 1
          self.right_rotate(k.parent.parent)
      if k == self.root:
        break
    self.root.color = 0

  # search the tree for the key k
  # and return the corresponding node
  def searchTree(self, k: TRBKey):
    return self.__search_tree_helper(self.root, k)

  # find the node with the minimum key
  def minimum(self, node: RBNode):
    while node.left != self.NULL_NODE:
      node = node.left
    return node

  # find the node with the maximum key
  def maximum(self, node: RBNode):
    while node.right != self.NULL_NODE:
      node = node.right
    return node

  # find the successor of a given node
  def successor(self, x: RBNode):
    # if the right subtree is not None,
    # the successor is the leftmost node in the
    # right subtree
    if x.right != self.NULL_NODE:
      return self.minimum(x.right)

    # else it is the lowest ancestor of x whose
    # left child is also an ancestor of x.
    y = x.parent
    while y != self.NULL_NODE and x == y.right:
      x = y
      y = y.parent
    return y

  # find the predecessor of a given node
  def predecessor(self,  x: RBNode):
    # if the left subtree is not None,
    # the predecessor is the rightmost node in the 
    # left subtree
    if (x.left != self.NULL_NODE):
      return self.maximum(x.left)

    y = x.parent
    while y != self.NULL_NODE and x == y.left:
      x = y
      y = y.parent

    return y

  # rotate left at node x
  def left_rotate(self, x: RBNode):
    y = x.right
    x.right = y.left
    if y.left != self.NULL_NODE:
      y.left.parent = x

    y.parent = x.parent
    if x.parent == None:
      self.root = y
    elif x == x.parent.left:
      x.parent.left = y
    else:
      x.parent.right = y
    y.left = x
    x.parent = y

  # rotate right at node x
  def right_rotate(self, x: RBNode):
    y = x.left
    x.left = y.right
    if y.right != self.NULL_NODE:
      y.right.parent = x

    y.parent = x.parent
    if x.parent == None:
      self.root = y
    elif x == x.parent.right:
      x.parent.right = y
    else:
      x.parent.left = y
    y.right = x
    x.parent = y

  # insert the key to the tree in its appropriate position
  # and fix the tree
  def insert(self, key: TRBKey):
    # Ordinary Binary Search Insertion
    node = RBNode(key)
    node.parent = None
    node.data = key
    node.left = self.NULL_NODE
    node.right = self.NULL_NODE
    node.color = 1 # new node must be red

    y = None
    x = self.root

    while x != self.NULL_NODE:
      y = x
      if node.data < x.data:
        x = x.left
      else:
        x = x.right

    # y is parent of x
    node.parent = y
    if y == None:
      self.root = node
    elif node.data < y.data:
      y.left = node
    else:
      y.right = node

    # if new node is a root node, simply return
    if node.parent == None:
      node.color = 0
      return

    # if the grandparent is None, simply return
    if node.parent.parent == None:
      return

    # Fix the tree
    self.__fix_insert(node)

  def get_root(self):
    return self.root

  # delete the node from the tree
  def delete_node(self, data: TRBKey):
    self.__delete_node_helper(self.root, data)


if __name__ == "__main__":
    bst = RedBlackTree()
    bst.insert(8)
    bst.insert(18)
    bst.insert(5)
    bst.insert(15)
    bst.insert(17)
    bst.insert(25)
    bst.insert(40)
    bst.insert(80)
    bst.delete_node(25)
    # bst.pretty_print()
    print("bruh")