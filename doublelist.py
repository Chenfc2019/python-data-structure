#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : doublelist.py
# @Author: Small-orange
# @Date  : 2020-12-05
# @Desc  : 双向链表

# 双向链表
class Node(object):
    """双链表的节点"""

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList(object):
    """双向链表"""

    def __init__(self):
        # 指向头节点
        self.head = None
        # 指向尾节点
        self.tail = None

    def is_empty(self):
        return self.head is None

    def length(self):
        """链表长度"""
        cur = self.head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def items(self):
        """顺序遍历"""
        cur = self.head
        while cur is not None:
            yield cur.data
            cur = cur.next

    def add(self, data):
        """向链表头部添加节点"""
        node = Node(data)
        # 链表为空时
        if self.head is None:
            self.head = node
            self.tail = node
        # 链表非空时
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def append(self, data):
        """向链表尾部添加节点"""
        node = Node(data)
        # 链表为空时
        if self.tail is None:
            self.head = node
            self.tail = node
        # 链表非空时
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def insert(self, index, data):
        """向指定位置添加节点"""
        # 头部插入
        if index <= 0:
            self.add(data)
        # 尾部插入
        elif index >= self.length():
            self.append(data)
        else:
            node = Node(data)
            cur = self.head
            for i in range(index):
                cur = cur.next
            # 循环完后cur指向节点index了
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """ 删除一个结点 """
        if self.is_empty():
            return
        # 当删除的节点在尾部
        if item == self.tail.data:
            self.tail = self.tail.prev
            self.tail.next = None
            return True
        cur = self.head
        pre = None
        # 第一个节点为需要删除的节点
        if cur.data == item:
            # 有多个节点
            if cur.next != None:
                self.head = cur.next
                return True
            # 只有一个节点
            else:
                self.head = None
                return True
        else:
            # 首尾之外的任意节点
            while cur.next != self.tail:
                if cur.data == item:
                    pre.next = cur.next
                    cur.next.prev = pre
                    return True
                else:
                    pre = cur
                    cur = cur.next

    def find(self, data):
        """ 查找节点是否存在"""
        return data in self.items()

    def print_list(self):
        """打印链表数据"""
        print('链表当前节点：')
        for node in self.items():
            print(node)


if __name__ == '__main__':
    # 实例化双向链表
    doublelist = DoubleLinkedList()

    # 向头部添加节点
    doublelist.add(10)
    doublelist.add(20)
    doublelist.print_list()

    # 向尾部添加节点
    doublelist.append(30)
    doublelist.append(40)
    doublelist.print_list()

    # 任意位置添加节点
    doublelist.insert(2, 666)
    doublelist.print_list()

    # 删除首尾和任意节点
    doublelist.remove(666)
    doublelist.remove(20)
    doublelist.remove(40)
    doublelist.print_list()

    #查找元素
    print('查找元素：',doublelist.find(30))
    print('查找元素：', doublelist.find(777))