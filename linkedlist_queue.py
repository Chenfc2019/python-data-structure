#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : linkedlist_queue.py
# @Author: Small-orange
# @Date  : 2020-12-07
# @Desc  : 链表实现队列

class Node(object):
    """节点"""
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue():
    """定义队列类"""

    def __init__(self):
        # 实例化时头指针为空
        self.head = None

    def is_empty(self):
        """判空"""
        return self.head is None

    def put(self,data):
        """尾部入队"""
        node = Node(data)
        if self.head is None:
            # 队列为空时
            self.head = node
        else:
            # 队列不为空时，先将node的指针指向头节点，然后将链表的头指针指向node节点
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def get(self):
        """头部出队"""
        if self.is_empty():
            return None
        else:
            val = self.head.data
            # 将头指针指向头节点的下一个节点
            self.head = self.head.next
            return val

    def peek(self):
        """查看队列头部元素"""
        return self.head.data if self.head else None

    def size(self):
        """队列大小"""
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count


if __name__ == '__main__':
    queue = Queue()
    print('判断队列是否为空：',queue.is_empty())
    print('--入队--')
    queue.put(10)
    queue.put(12)
    queue.put(66)
    print('--队列大小--',queue.size())
    print('--队头元素--',queue.peek())
    print('--出队--')
    print(queue.get())
    print(queue.get())
    print(queue.get())
    print(queue.get())