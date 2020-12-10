#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : binary_search_tree.py
# @Author: Small-orange
# @Date  : 2020-12-09
# @Desc  : 二叉查找树实现

class Node(object):
    """节点"""
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None

class BinarySearchTree(object):
    """二叉查找树"""
    def __init__(self):
        self.root = None

    def find(self,root,data):
        """查找数据"""
        if root is None:
            return False
        # 比根节点小，往左子树走
        if data < root.data:
            return self.find(root.left_child,data)
        # 比根节点大，往右子树走
        elif data > root.data :
            return self.find(root.right_child,data)
        # 相等时找到
        else:
            return True

    def insert(self,data):
        """添加节点-循环实现"""
        node = Node(data)
        if self.root is None:
            self.root =  node
            return
        cur = self.root
        while cur is not None:
            if data < cur.data:
                if cur.left_child != None:
                    cur = cur.left_child
                else:
                    cur.left_child = node
                    return
            elif data > cur.data:
                if cur.right_child != None:
                    cur = cur.right_child
                else:
                    cur.right_child = node
                    return
            else:
                cur.data = data
                return

    def insert_rec(self,root,data):
        """添加节点-递归实现"""
        # 左子树为空时插入
        if root is None:
            root =  Node(data)
        # 比根节点小，往左子树走
        elif data < root.data:
            root.left_child = self.insert_rec(root.left_child,data)
        # 比根节点大，往右子树走
        elif data > root.data:
                root.right_child = self.insert_rec(root.right_child,data)
        return root

    def min(self,root):
        """最小值"""
        if root.left_child:
            return self.min(root.left_child)
        else:
            return root

    def max(self,root):
        """最大值"""
        if root.right_child:
            return search_tree.max(root.right_child)
        else:
            return root

    def inorder(self,root):
        """中序遍历--左、根、右"""
        if root is None:
            return
        self.inorder(root.left_child)
        print(root.data, end="   ")
        self.inorder(root.right_child)

    def delNode(self, root, data):
        """删除二叉搜索树中值为val的点"""
        if root == None:
            return
        if data < root.data:
            root.left_child = self.delNode(root.left_child, data)
        elif data > root.data:
            root.right_child = self.delNode(root.right_child, data)
        # 当val == root.val时，分为三种情况：只有左子树或者只有右子树、有左右子树、即无左子树又无右子树
        else:
            if root.left_child and root.right_child:
                # 既有左子树又有右子树，则需找到右子树中最小值节点
                temp = self.min(root.right_child)
                root.data = temp.data
                # 再把右子树中最小值节点删除
                root.right_child = self.delNode(root.right_child, temp.data)
            elif root.right_child == None and root.left_child == None:
                # 左右子树都为空
                root = None
            elif root.right_child == None:
                # 只有左子树
                root = root.left_child
            elif root.left_child == None:
                # 只有右子树
                root = root.right_child
        return root



if __name__ == '__main__':
    node1 = Node(40)
    node2 = Node(30)
    node3 = Node(21)
    node4 = Node(35)
    node5 = Node(50)
    node1.left_child = node2
    node1.right_child = node5
    node2.left_child = node3
    node2.right_child = node4

    search_tree = BinarySearchTree()
    search_tree.root = node1

    search_tree.insert_rec(search_tree.root,45)
    search_tree.insert_rec(search_tree.root, 15)
    print('初始树：')
    search_tree.inorder(search_tree.root)
    print()
    print('最大值：',search_tree.max(search_tree.root).data)
    print('最小值：', search_tree.min(search_tree.root).data)

    print('删除叶子节点15')
    search_tree.delNode(search_tree.root,15)
    search_tree.inorder(search_tree.root)
    print()

    print('删除一个子树的节点50')
    search_tree.delNode(search_tree.root,50)
    search_tree.inorder(search_tree.root)
    print()

    print('删除两个子树的节点30')
    search_tree.delNode(search_tree.root,30)
    search_tree.inorder(search_tree.root)
    print()
