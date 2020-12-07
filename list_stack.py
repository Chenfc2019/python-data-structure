#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : list_stack.py
# @Author: Small-orange
# @Date  : 2020-12-05
# @Desc  : 栈-list实现

class Stack(object):
    """定义栈类"""

    def __init__(self):
        self.list = []

    def is_empty(self):
        """判断栈空"""
        return self.list == []

    def push(self, data):
        """在栈顶添加元素"""
        self.list.append(data)

    def pop(self):
        """弹出栈顶元素"""
        return self.list.pop()

    def peek(self):
        """取栈顶元素，不修改栈内容"""
        return self.list[-1]

    def size(self):
        """栈大小"""
        return len(self.list)


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

