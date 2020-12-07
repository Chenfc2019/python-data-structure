#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : list_queue.py
# @Author: Small-orange
# @Date  : 2020-12-07
# @Desc  : list实现队列

class Queue():
    """定义队列类"""
    def __init__(self):
        self.queue = []

    def is_empty(self):
        """判空"""
        return self.queue == []

    def put(self,data):
        """入队"""
        self.queue.append(data)

    def get(self):
        """出队"""
        return self.queue.pop(0)

    def peek(self):
        """获取队头元素"""
        return self.queue[0]

    def size(self):
        """队列大小"""
        return len(self.queue)

    
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