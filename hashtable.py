    #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : hashtable.py
# @Author: Small-orange
# @Date  : 2020-12-07
# @Desc  : 链接法实现哈希表

class HashTable(object):
    """哈希表"""

    def __init__(self,length=2):
        # 给定初始长度
        self.length = length
        # 创建二维数组
        self.slots = [[] for i in range(self.length)]
        # 当前哈希表的元素个数
        self.datasize = 0

    def hash(self,k):
        """散列键值隐射函数"""
        # 获取键在表中的地址
        return k % self.length

    def add(self,k,v):
        """添加存储的键-值"""
        if self.datasize > len(self.slots):
            # 元素超过数组长度时扩容
            self.resize()
        index = self.hash(k)
        # 判断index下标位置list是否为空
        if self.slots[index] != []:
            # 判断index处的list中是否有key重复
            for item in self.slots[index]:
                if k == item[0]:
                    # k重复时移除键值对
                    self.slots[index].remove(item)
        # 添加键值对到哈希表中
        self.slots[index].append((k,v))
        self.datasize += 1

    def get(self,k):
        """根据键来取值"""
        index = self.hash(k)
        if self.slots[index] == []:
            return None
        else:
            for item in self.slots[index]:
                if k == item[0]:
                    return item[1]

    def resize(self):
        """扩大容量"""
        self.length = self.length * 2
        new_slot = [[] for i in range(self.length)]
        # 将原列表中的元素重新映射后赋值到新的数组
        for item in len(self.slots):
            for kv in item:
                index = self.hash(kv[0])
                new_slot[index].append(kv)
        # 将原数组指针指向扩容后的数组
        self.slots = new_slot


if __name__ == '__main__':
    dict = HashTable()
    dict.add(3,9)
    dict.add(4,'he')
    dict.add(7, 'he')
    print('--值--',dict.get(3))
    print('--值--', dict.get(4))
    print('--值--', dict.get(7))