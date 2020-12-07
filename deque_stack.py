#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : deque_stack.py
# @Author: Small-orange
# @Date  : 2020-12-07
# @Desc  : 使用collections.deque实现栈

from collections import deque


class Stack(object):
    """定义栈类"""

    def __init__(self):
        """实例化新的栈"""
        self.stack = deque()

    def is_empty(self):
        """判断栈空"""
        return len(self.stack) == 0

    def push(self, data):
        """在栈顶添加元素"""
        self.stack.append(data)

    def pop(self):
        """弹出栈顶元素"""
        return self.stack.pop()

    def peek(self):
        """取栈顶元素，不修改栈内容"""
        return self.stack[-1]

    def size(self):
        """栈大小"""
        return len(self.stack)