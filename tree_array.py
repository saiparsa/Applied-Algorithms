from __future__ import annotations

from typing import Optional, List


class Node:
    def __init__(self, data):
        """
        Creates a node without children or parent
        :param data: the value stored in the node
        """
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.parent: Optional[Node] = None
        self.size = 1

    @staticmethod
    def get_size(node: Optional[Node]):
        """
        :param node: (possibly None) node
        :return: Size of the node. When the node is None, returns 0.
        """
        return 0 if node is None else node.size

    def fix_size(self):
        """
        Fixes node size based on sizes of its children
        """
        self.size = 1 + Node.get_size(self.left) + Node.get_size(self.right)

class TreeArray:
    """
    Efficient variable-size arrays implemented using tree
    """
    def __init__(self):
        self.root: Optional[Node] = None

    def size(self):                  #Time complexity :O(1)
        """
        :return: The total number of elements
        """
        return Node.get_size(self.root)

    def find(self, i: int) -> Node:        #Time complexity :O(n)'''
        """
        :param i: An index of a node to find
        :return: A node in the the tree with index i
        :raises IndexError if index is out of bounds
        """
        rt = self.root
        if i >= Node.get_size(rt) or i<0:
            raise IndexError

        while 1:
            
            curr_size = Node.get_size(rt.left)
            
            if i == curr_size:
                return rt

            else:
                
                if i < curr_size:
                    rt = rt.left
    
                if i > curr_size:
                    i = i - curr_size - 1
                    rt = rt.right

        ...

    def get(self, i: int):         #Time complexity :O(n)'''
        """
        :param i: Index where the element is inserted
        :return: A value at index i
        :raises IndexError if index is out of bounds
        """
        return self.find(i).data

    def set(self, i: int, x):     #Time complexity :O(n)'''
        """
        Changes value at index i to x
        :param i: Index of the modified value
        :param x: The new value
        :raises IndexError if index is out of bounds
        """
        self.find(i).data=x
        ...

    def fix_sizes(self, node: Node):
        """
        Fixes sizes of all nodes on the path between this node and the root of the tree
        :param node: Starting node
        """
        while node.parent != None:
            node = node.parent
            node.fix_size()
        ...

    def insert(self, i: int, x):        #Time complexity :O(n)'''
        """
        Insert value x into position i
        :param i: Index where the element is inserted
        :param x: The inserted value
        :raises IndexError if index is out of bounds
        """
        
        if  i > Node.get_size(self.root) or i < 0:
            raise IndexError
            
        if self.root == None:
            self.root = Node(x)
            out = self.root
            self.fix_sizes(out)
            
        else :
            
            if i == 0:
                
                curr = None
                node = self.root
                while node != None:
                    curr = node
                    node = node.left
                if curr == None:
                    self.root = Node(x)
                    curr = self.root
                else:
                    curr.left = Node(x)
                    curr.left.parent = curr
    
                self.fix_sizes(curr.left)
            
            else:
                
                curr=self.find(i-1)
                
                if curr.right!=None:
                    ip=curr.right
                    while ip.left != None:
                        ip=ip.left
                    ip.left=Node(x)
                    ip.left.parent=curr.right
                    self.fix_sizes(ip.left)
                    
                else:
                    ip = Node(x)
                    curr.right = ip
                    ip.parent=curr
                    self.fix_sizes(ip)               
                         
        ...
        
    def tree_min(self, node):
        while node.left != None:
            node = node.left
        return node

    def successor(self, node):
        if node.right != None:
            return self.tree_min(node)
        y = node.parent
        while y != None :
            if node == y.right:
                node = y
                y = y.parent
        return y

    def transplant(self, u, v):
        
        if u.parent == None:
            self.root = v
        if u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent
        
        
            
        

    def remove(self, i: int):       #Time complexity :O(n)'''
        """
        Removes an element at index i
        :param i: Index of the removed element
        :raises IndexError if index is out of bounds"""
        
        if i > Node.get_size(self.root) or i<0:
            raise IndexError
    
        z = self.find(i)
        
        if z.left == None and z.right != None:
            self.transplant(z, z.right)
            self.fix_sizes(z.parent)
        elif z.right == None and z.left != None:
            self.transplant(z, z.left)
            self.fix_sizes(z.parent)
        elif z.left == None and z.right == None:
           
            self.transplant(z,None)
            self.fix_sizes(z.parent)
        else:
            y = self.successor(z)
            if y == z.right or y == z.left:
                self.transplant(z, y)
                self.fix_sizes(z.parent)
            if y != z.right or y != z.left:
                self.transplant(z, y)
                self.transplant(y, y.right)
                self.fix_sizes(y.parent)
                
        

    def inorder(self) -> List:    #Time complexity :O(n)'''
        
        """
        :return: Elements in inorder. Should return an array represented by the tree
        """
        array=[]
        curr = self.root
        if curr==None:
            print('Empty')
            return
        curr_nodes=[]
        while 1:
            if curr!=None:
                curr_nodes.append(curr)
                curr=curr.left
            else:
                if len(curr_nodes) != 0:                        
                    curr = curr_nodes.pop()
                    array.append(curr.data)
                    curr = curr.right
                else:                
                    return array
                
                
tree = TreeArray()
tree.insert(0,10)
tree.insert(1,31)
tree.insert(2,14)
tree.insert(2,54)
tree.insert(0,38)
#tree.insert(8,8)  #throws out of bounds error
tree.insert(2,24)
tree.insert(1,8)
tree.insert(3,156)
print(tree.inorder())
tree.remove(1)
print(tree.inorder())
tree.remove(5)
print(tree.inorder())
tree.remove(5)
print(tree.inorder())
tree.remove(0)
print(tree.inorder())



        
                
            
        
