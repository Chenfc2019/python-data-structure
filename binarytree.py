#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : binarytree.py
# @Author: Small-orange
# @Date  : 2020-12-07
# @Desc  : 二叉树实现

class Node(object):
    """节点"""
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None

class BinaryTree(object):
    """二叉树"""

    def __init__(self):
        self.root = None

    def add(self,data):
        """插入节点"""
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        # 使用列表构造队列，并将根节点放到队列中
        queue = [self.root]
        # 队列不为空时循环
        while queue:
            # 取队列头部节点作为当前处理节点
            cur_node = queue.pop(0)
            # 左孩子为空时直接放在左孩子位置
            if cur_node.left_child is None:
                cur_node.left_child = node
                return
            # 不为空时将左孩子放进队列等待处理
            else:
                queue.append(cur_node.left_child)
            # 右孩子逻辑相同
            if cur_node.right_child is None:
                cur_node.right_child = node
                return
            else:
                queue.append(cur_node.right_child)

    def breadth_travel(self):
        """层次遍历"""
        if self.root is None:
            return
        # 使用列表构造层次遍历的队列
        queue = [self.root]
        while queue:
            # 取队列头部节点作为当前处理节点
            cur_node = queue.pop(0)
            # 打印节点数据
            print(cur_node.data,end="   ")
            # 左孩子非空时将左孩子放入队列
            if cur_node.left_child is not None:
                queue.append(cur_node.left_child)
            # 右孩子非空时将左孩子放入队列
            if cur_node.right_child is not None:
                queue.append(cur_node.right_child)

    def preorder(self,root):
        """先序遍历--根、左、右"""
        if root is None:
            return
        print(root.data,end="   ")
        self.preorder(root.left_child)
        self.preorder(root.right_child)

    def inorder(self,root):
        """中序遍历--左、根、右"""
        if root is None:
            return
        self.inorder(root.left_child)
        print(root.data, end="   ")
        self.inorder(root.right_child)

    def postrder(self,root):
        """后序遍历--左、右、根"""
        if root is None:
            return
        self.postrder(root.left_child)
        self.postrder(root.right_child)
        print(root.data, end="   ")


if __name__ == '__main__':
    tree = BinaryTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)

    print('--层次遍历--')
    tree.breadth_travel()

    print('\n--前序遍历--')
    tree.preorder(tree.root)

    print('\n--中序遍历--')
    tree.inorder(tree.root)

    print('\n--后序遍历--')
    tree.postrder(tree.root)
