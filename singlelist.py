#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : singlelist.py
# @Author: Small-orange
# @Date  : 2020-12-04
# @Desc  : 单链表

class Node(object):
    """节点定义"""

    def __init__(self, data):
        # 数据域
        self.data = data
        # 指针域，创建时为None
        self.next = None


class SingleList(object):
    """链表定义"""

    def __init__(self):
        # 链表头
        self.head = None

    def is_empty(self):
        """链表判空"""
        return self.head is None

    def length(self):
        """链表长度"""
        # 获取初始的头指针
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            # 指针后移1位
            cur = cur.next
        return count

    def datas(self):
        """链表遍历"""
        cur = self.head
        while cur is not None:
            # 返回生成器
            yield cur.data
            # 指针后移1位
            cur = cur.next

    def add(self, data):
        """在头部插入节点"""
        # 创建新节点
        node = Node(data)
        # 新节点指向原头节点
        node.next = self.head
        # 头节点指向新节点
        self.head = node

    def append(self, data):
        """向尾部插入节点"""
        node = Node(data)
        if self.is_empty():
            # 空链表则直接将head指向node
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                # 将指针移到最后一个节点
                cur = cur.next
            # 将最后一个节点的指针指向node
            cur.next = node

    def insert(self, index, data):
        """任意位置插入节点"""
        if index <= 0:
            # 在头部插入
            self.add(data)
        elif index >= self.length():
            # 在尾部插入
            self.append(data)
        else:
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
                # 创建新节点
            node = Node(data)
            # 将新节点指向就节点
            node.next = cur.next
            # 将旧节点前一个节点指向新节点
            cur.next = node

    def remove(self, item):
        """ 删除一个结点 """
        if self.is_empty():
            return
        cur = self.head
        pre = None
        # 第一个元素为需要删除的元素
        if cur.data == item:
            if cur.next != None:
                cur.next = self.head.next
                # 调整头部结点
                self.head = self.head.next
            else:
                # 只有一个元素
                self.head = None
        else:
            # 不是第一个元素
            pre = self.head
            while cur.next != self.head:
                if cur.data == item:
                    # 删除
                    pre.next = cur.next
                    return True
                else:
                    pre = cur  # 记录前一个指针
                    cur = cur.next  # 调整指针位置
        # 当删除元素在末尾
        if cur.data == item:
            pre.next = self.head
            return True

    def find(self, data):
        """ 查找元素是否存在"""
        return data in self.datas()

    def printlist(self):
        """打印链表元素"""
        print('当前链表：')
        for i in self.datas():
            print(i)


if __name__ == '__main__':
    # 创建链表
    singlelist = SingleList()

    # 添加节点
    singlelist.add(3)
    singlelist.append(5)
    singlelist.append(7)
    print('查找元素',singlelist.find(10))
    # 链表长度
    length = singlelist.length()
    print('链表长度:', length)

    singlelist.printlist()

    # 删除元素
    singlelist.remove(5)
    print('--删除元素--')
    singlelist.printlist()

    # 任意位置插入元素
    singlelist.insert(2, 666)
    print('--任意位置插入元素--')
    singlelist.printlist()