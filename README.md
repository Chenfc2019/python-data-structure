线性结构
数组
数据在内存中顺序存储，可以通过下标索引。
特点：支持随机访问，索引元素效率高，插入元素和删除元素效率低。
数组存放空间连续，插入元素时需要将插入位置及后面的元素一次往后移动一位，然后将元素插入到空出的插入位置。
`python中的list是一个动态数组，支持动态扩容（2^n），list中封装了数组常用的方法：
>>> list = [3, 5, 7]
>>> list.append(9) # 往数组尾部添加元素
>>> list
[3, 5, 7, 9]
>>> list.insert(2,5) # 在指定位置插入元素
>>> list
[3, 5, 5, 7, 9]
>>> list.pop() # 取数组最后一个元素，会从数组中删除该元素
9
>>> list
[3, 5, 5, 7]
>>> list.remove(5) # 删除数组中的指定元素，有多个时只删除第一个
>>> list
[3, 5, 7]
>>> list.index(5) # 查找元素在列表中的位置
1
>>> list.reverse() # 列表反转
>>> list
[7, 5, 3]`
在python中通过id()函数来输出列表元素的第地址时，可以看到id的值并不是连续的，这是为什么呢？
`>>> arr = ['a','b','c']
>>> for char in arr:
        print(id(char))
2204167613216
2204167611536
2204167474288`
因为python的list存的是元素对象的引用而不是元素本身，从下面代码中可以看出来，所以输出的id值是元素对象的引用值，在底层的c语言中是使用数组来实现的。
`>>> a = 1
>>> id(a)
1598830848
>>> b = [a]
>>> id(b)
9390640
>>> id(b[0])
1598830848`
链表
链表数据在内存中的存储不连续，链表有一系列的节点通过指针依次连接起来，每个节点包含数据域和指针域，数据域存储数据，指针域存储下一个节点的指针。
单向链表
单向链表也叫单链表，是链表中最简单的形式，它的每个节点包含两个域，一个信息域（元素域）和一个链接域。这个链接指向链表中的下一个节点，而最后一个节点的链接域则指向一个空值。
因为链表中的数据不是顺序存储的，不能随机访问，因此链表的查询效率低，但是链表在任意位置插入和删除节点时不用移动节点位置，因此插入和删除效率高。
链表实现
通常有以下步骤：
1. 定义节点
2. 定义链表
3. 使用链表
`class Node(object):
    '''1.节点定义'''
    def __init__(self,data):
        # 数据域
        self.data = data
        # 指针域，创建时为None
        self.next = None
class SingleList(object):
    '''2.链表定义'''
    def __init__(self):
        # 链表头
        self.head = None
     
if __name__ == '__main__':
    #3.链表使用
    # 创建链表
    singlelist = SingleList()
    # 创建节点
    node1 = Node(3)
    # 将链表头指向节点
    singlelist.head = node1
    # 创建节点往链表上添加
    node2 = Node(5)
    node1.next = node2
    node3 = Node(7)
    node2.next = node3
    # 创建临时变量指向头节点
    temp = singlelist.head
    # 取头节点的数据
    print(temp.data)
    # 取下一个节点的数据
    temp = temp.next
    print(temp.data)`
    
输出结果：
3
5
上面定义并使用了一个单项链表，但是链表的使用很不方便，获取元素添加和获取需要定位到节点，长度也没法知道，所以需要定义一些常用的方法，方便链表的使用。
链表中的常用方法：
• is_empty() 链表是否为空
• length() 链表长度
• items() 获取链表数据迭代器
• add(item) 链表头部添加元素
• append(item) 链表尾部添加元素
• insert(pos, item) 指定位置添加元素
• remove(item) 删除节点
• find(item) 查找节点是否存在
class Node(object):
    '''节点定义'''
    def __init__(self,data):
        # 数据域
        self.data = data
        # 指针域，创建时为None
        self.next = None
class SingleList(object):
    '''链表定义'''
    def __init__(self):
        # 链表头
        self.head = None
    def is_empty(self):
        '''链表判空'''
        return self.head is None
    def length(self):
        '''链表长度'''
        # 获取初始的头指针
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            # 指针后移1位
            cur = cur.next
        return count
    def datas(self):
        '''链表遍历'''
        cur = self.head
        while cur is not None:
            # 返回生成器
            yield cur.data
            # 指针后移1位
            cur = cur.next
    def add(self,data):
        '''在头部插入节点'''
        # 创建新节点
        node = Node(data)
        # 新节点指向原头节点
        node.next = self.head
        # 头节点指向新节点
        self.head = node
    def append(self,data):
        '''向尾部插入节点'''
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
    def insert(self,index,data):
        '''任意位置插入节点'''
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
        '''打印链表元素'''
        print('当前链表：')
        for i in self.datas():
            print(i)
if __name__ == '__main__':
    # 创建链表
    singlelist = SingleList()
    
    #添加节点
    singlelist.add(3)
    singlelist.append(5)
    singlelist.append(7)
    # 链表长度
    length = singlelist.length()
    print('链表长度:',length)
    singlelist.printlist()
    # 删除元素
    singlelist.remove(5)
    print('--删除元素--')
    singlelist.printlist()
    # 任意位置插入元素
    singlelist.insert(2,666)
    print('--任意位置插入元素--')
    singlelist.printlist()
双向链表
双向链表与与单向链表的区别在于，双向链表的节点包含了两个指针域，如下图，prev指针域指向前一个节点，next指向后一个节点，head指向头节点，第一个节点的prev指针为None，最后一个节点的next为空。
为了方便操作双向链表，也会在链表中定义一些常用的方法。实例如下：
# 双向链表
class Node(object):
    '''双链表的节点'''
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class DoubleLinkedList(object):
    '''双向链表'''
    def __init__(self):
        self.head = None
        self.tail = None
    def is_empty(self):
        return self.head is None
    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count
    def items(self):
        '''顺序遍历'''
        cur = self.head
        while cur is not None:
            yield cur.data
            cur = cur.next
    def add(self,data):
        '''向链表头部添加节点'''
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    def append(self,data):
        '''向链表尾部添加节点'''
        node = Node(data)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
    def insert(self,index,data):
        '''向指定位置添加节点'''
        if index <= 0:
            self.add(data)
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
        return data in self.datas()
    def print_list(self):
        '''打印链表数据'''
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
    doublelist.insert(2,666)
    doublelist.print_list()
    
    # 删除首尾和任意节点
    doublelist.remove(666)
    doublelist.remove(20)
    doublelist.remove(40)
    doublelist.print_list()
输出结果：
链表当前节点：
20
10
链表当前节点：
20
10
30
40
链表当前节点：
20
10
666
30
40
链表当前节点：
10
30
栈
栈是一种只能在一段添加和移除的线性数据结构，最先入栈的数据最后出栈，这个模式被称为 LIFO 后进先出（Last In First Out）。栈数据管理模式就是 LIFO。
应用：记录浏览器的回退记录、软件的操作撤销功能、IDE中的括号匹配检测等。
堆栈是一种线性数据结构，所以数组和链表都可以实现。
堆栈的常用方法：
• push(item) - 将元素添加到栈顶，需要参数，无返回值。
• pop() - 删除栈顶元素，不需要参数，返回栈顶元素，并修改栈的内容。
• peek() - 返回栈顶元素，不需要参数，不修改栈的内容。
• isEmpty() - 检查栈是否为空，不需要参数，返回布尔值
• size() - 返回栈中元素个数，不需要参数，返回整数
list实现
使用list的append()和pop()方法可以实现在列表的尾部添加和移除元素，所以可以用list来实现栈。
class Stack(object):
    '''定义栈类'''
    
    def __init__(self):
        self.list = []
    '''判断栈空'''
    def is_empty(self):
        return self.list == []
    '''在栈顶添加元素'''
    def push(self, data):
        self.list.append(data)
    '''弹出栈顶元素'''
    def pop(self):
        return self.list.pop()
    '''取栈顶元素，不修改栈内容'''
    def peek(self):
        return self.list[-1]
    '''栈大小'''
    def size(self):
        return len(self.list)
if __name__ == '__main__':
    stack = Stack()
    print('栈是否为空：',stack.is_empty())
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print('栈大小：',stack.size())
    print('peek取栈顶元素：',stack.peek())
    print('---出栈---')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
输出结果：
栈是否为空： True
栈大小： 3
peek取栈顶元素： 30
---出栈---
30
20
10
链表实现
class Node(object):
    '''节点定义'''
    
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack(object):
    '''链表实现栈'''
    def __init__(self):
        self.head = None
    '''判断栈空'''
    def is_empty(self):
        return self.head is None
    '''在栈顶添加元素'''
    def push(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
    '''弹出栈顶元素'''
    def pop(self):
        val = None
        if self.is_empty():
            return val
        else:
            val = self.head.data
            self.head = self.head.next
        return val
    '''取栈顶元素，不修改栈内容'''
    def peek(self):
        return self.head.data
    '''栈大小'''
    def size(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count
collections.deque实现
python中栈也可以用deque类实现，当我们想要在实现在容器两端更快速地进行append和pop操作时，deque比列表更合适。deque可以提供O(1)时间的append和pop操作，而列表则需要O(n)时间。
from collections import deque
class Stack(object):
    '''定义栈类'''
    '''实例化新的栈'''
    def __init__(self):
        self.stack = deque()
    '''判断栈空'''
    def is_empty(self):
        return len(self.stack) == 0
    '''在栈顶添加元素'''
    def push(self, data):
        self.stack.append(data)
    '''弹出栈顶元素'''
    def pop(self):
        return self.stack.pop()
    '''取栈顶元素，不修改栈内容'''
    def peek(self):
        return self.stack[-1]
    
    '''栈大小'''
    def size(self):
        return len(self.stack)
queue模块实现
queue模块有LIFO queue，也就是栈结构．用put()和get()操作从Queue中添加和获得数据，下面是queue模块中LIFO queue的实现。
class LifoQueue(Queue):
    '''Variant of Queue that retrieves most recently added entries first.'''
    def _init(self, maxsize):
        self.queue = []
    def _qsize(self):
        return len(self.queue)
    def _put(self, item):
        self.queue.append(item)
    def _get(self):
        return self.queue.pop()
队列
队列（queue）是只允许在一端进行插入操作，而在另一端进行删除操作的线性表。
队列是一种先进先出（First in First Out）的线性表，简称FIFO。允许插入的一端称为队尾，允许删除的一端称为队头。
list实现
class Queue():
    '''定义队列类'''
    def __init__(self):
        self.queue = []
    def is_empty(self):
        return self.queue == []
    def put(self,data):
        self.queue.append(data)
    def get(self):
        return self.queue.pop(0)
    def peek(self):
        return self.queue[0]
    def size(self):
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
输出结果：
判断队列是否为空： True
--入队--
--队列大小-- 3
--队头元素-- 10
--出队--
10
12
66
链表实现
class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue():
    '''定义队列类'''
    def __init__(self):
        # 实例化时头指针为空
        self.head = None
    def is_empty(self):
        return self.head is None
    def put(self,data):
        '''入队'''
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
        '''出队'''
        if self.is_empty():
            return None
        else:
            val = self.head.data
            # 将头指针指向头节点的下一个节点
            self.head = self.head.next
            return val
    def peek(self):
        '''查看队列头部元素'''
        return self.head.data if self.head else None
    def size(self):
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
输出结果：
判断队列是否为空： True
--入队--
--队列大小-- 3
--队头元素-- 10
--出队--
10
12
66
None
Queue和deque
在Python里，queue.Queue主要是为了线程间通信，作为“队列”只是附带的功能。而collections.deque就是个容器，和dict，list类似。
如果只是想用一个简单的队列，可能从名字上看上去“Queue”更合适。当然用是可以用的，不过，Queue相比deque有个坏处：慢不少。
这里只看最简单的操作，塞东西和取东西。
Queue：put和get
deque：append和popleft
import timeit
from queue import Queue
from collections import deque
def test_queue():
    q = Queue()
    for i in range(1000):
        q.put(i)
    for i in range(1000):
        q.get()
def test_deque():
    q = deque()
    for i in range(1000):
        q.append(i)
    for i in range(1000):
        q.popleft()
if __name__ == '__main__':
    t_queue = timeit.timeit('test_queue()', setup='from __main__ import test_queue', number=100)
    t_deque = timeit.timeit('test_deque()', setup='from __main__ import test_deque', number=100)
    print('t_queue', t_queue, 't_deque', t_deque)
    print('faster', t_queue / t_deque)
结果如下:
t_queue 0.5356368 t_deque 0.017948600000000203
faster 29.84281782423108
可见，Queue所用的时间，在这里几乎是deque的30倍。
Queue是很高级的同步设施，有例如get_nowait，join等同步用接口，该阻塞就阻塞，该返回就返回。而deque只是个容器。其实从类名也有所反映，Queue是大写的首字母；而deque是和list, dict等一样是小写的首字母。
详细信息参考：https://zhuanlan.zhihu.com/p/146393319
哈希表
哈希表又称散列表，是普通数组概念的推广，是能够根据键直接访问值的数据结构，通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。这个映射函数叫做散列函数(Hash Function)，存放记录的数组叫做散列表(Hash Table)。
在平均情况下，在哈希表中查找一个元素的期望时间是  ,因此效率极高。Python中的字典就是采用了哈希表的结构。
碰撞
哈希表通过散列函数将关键字映射到散列表中，两个关键字映射到同一个槽被称为碰撞。
碰撞问题的解决
链接法
在链接法中，把散列到同一槽中的所有元素放到一个链表中，槽  中有一个指针，指向由所有散列到  的元素构成的链表的头；如果不存在这样的元素，则置为NULL。
开放寻址法
在开放寻址法中，所有的元素都存放在散列表中，因此哈希表的每个表项或包含一个元素，或包含NULL，而不像在链表法中，这里没有链表，也没有元素存放在散列表外。
在开放寻址法中，当要插入一个元素时，需要连续的检查散列表的各项，直到找到一个空槽来放置待插入的关键字为止。
哈希表性能
填充因子：散列表包含的元素/散列表总位置数，可以看作填充率，值越大，剩余的位置越少，发生碰撞的可能性越大。
散列函数：散列函数决定了键被映射的位置，不好的散列函数可能会将键映射到同一个位置，引起碰撞。
链接法实现哈希表。
链接法实现
class HashTable(object):
    '''链接法实现哈希表'''
    def __init__(self,length=2):
        '''实例化哈希表'''
        # 给定初始长度
        self.length = length
        # 创建二维数组
        self.slots = [[] for i in range(self.length)]
        # 当前哈希表的元素个数
        self.datasize = 0
    def hash(self,k):
        '''散列函数'''
        # 获取键在表中的地址
        return k % self.length
    def add(self,k,v):
        '''添加存储的键-值'''
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
        '''根据键来取值'''
        index = self.hash(k)
        if self.slots[index] == []:
            return None
        else:
            for item in self.slots[index]:
                if k == item[0]:
                    return item[1]
    def resize(self):
        '''扩大容量'''
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
输出结果：
--值-- 9
--值-- he
--值-- he
哈希表的文章：https://zhuanlan.zhihu.com/p/34587466
树形结构
树是一种非线性的层次型数据结构，存储的是具有“一对多”关系的元素的集合。是以边相连的结点的集合，每个结点存储对应的值，当存在子结点时与之相连。
相关概念：
• 根节点：树的第一个节点
• 边：树的节点与节点之间通过边相连。
• 叶子节点：树的末端节点，他们没有子节点
• 树高：是由根结点出发，到子结点的最长路径长度。
• 结点深度：是指对应结点到根结点路径长度。
二叉树
二叉树是特殊的树，它的每个节点最多只有两个子节点，称为左孩子和右孩子。
AVL树
红黑树
B树
堆
Trie哈夫曼树
并查集
图结构
邻接矩阵
邻接表