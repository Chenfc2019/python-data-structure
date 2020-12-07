#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : linkedlist_stack.py
# @Author: Small-orange
# @Date  : 2020-12-07
# @Desc  : 栈结构的链表实现

class Node(object):
    """节点定义"""

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack(object):
    """链表实现栈"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """判断栈空"""
        return self.head is None

    def push(self, data):
        """在栈顶添加元素"""
        node = Node(data)
        # 栈为空时
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        """弹出栈顶元素"""
        val = None
        if self.is_empty():
            return val
        else:
            val = self.head.data
            # 将头指针指向头节点的下一个节点
            self.head = self.head.next
        return val

    def peek(self):
        """取栈顶元素，不修改栈内容"""
        return self.head.data

    def size(self):
        """栈大小"""
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count


if __name__ == '__main__':
    stack = Stack()
    print('栈是否为空：', stack.is_empty())
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print('栈大小：', stack.size())
    print('peek取栈顶元素：', stack.peek())
    print('---出栈---')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())