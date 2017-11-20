#coding:utf-8


##########################################################
#format 和 %s
# name = (1,2,3)
# print "hi is %s"%(name,)
#
# print "this is {0} {1}".format("11",name)

#iterable genertors
# mygenerator = [x*x for x in range(3)]#迭代器
# mygenerator = (x*x for x in range(3))#生成器
#
# for i in mygenerator:
#     print i
# for i in mygenerator:
#     print i



##########################################################
# 单例模式

#__new__实现
# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,"_instance"):
#             orig = super(Singleton,cls)
#             cls._instance = orig.__new__(cls,*args,**kwargs)
#         return cls._instance
#
# class Myclass(Singleton):
#
#     a = 1

#装饰器实现
# def singleton(cls,*args,**kwargs):
#     instance = {}
#     def getinstance():
#         if cls not in instance:
#             instance[cls] = cls(*args,**kwargs)
#         return instance[cls]
#     return getinstance
#
# @singleton

# class Myclass:
#     pass

#import 方法
# class My_Singleton(object):
#     def foo(self):
#         pass
# myclass_singleton = My_Singleton()
#
# from mianshi import My_Singleton

# myclass_singleton.foo()


#
# A = Myclass()
# print A
# B = Myclass()
# print B
# C = Myclass()
# print C



##########################################################
#台阶问题

# fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)#1,2
# fib = lambda n: n if n <= 2 else 2*fib(n - 1)#1,2，n
#
# print fib(9)

##########################################################
#矩形覆盖我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

f = lambda n: 1 if n < 2 else f(n - 1) + f(n - 2)



##########################################################
#二分查找
def bSearch(l,t):
    low,high = 0,len(l)-1
    while low < high:
        mid = (low + high)/2
        if l[mid] < t:
            low = mid +1
        elif l[mid] > t:
            high = mid
        else:
            return mid
    return low if l[low] == t else False
l = [1, 4, 12, 45, 66, 99, 120, 444]

print bSearch(l,4)



##########################################################
#交叉链表求交点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def node(l1, l2):
    length1, length2 = 0, 0
    # 求两个链表长度
    while l1.next:
        l1 = l1.next
        length1 += 1
    while l2.next:
        l2 = l2.next
        length2 += 1
    # 长的链表先走
    if length1 > length2:
        for _ in range(length1 - length2):
            l1 = l1.next
    else:
        for _ in range(length2 - length1):
            l2 = l2.next
    while l1 and l2:
        if l1.next == l2.next:
            return l1.next
        else:
            l1 = l1.next
            l2 = l2.next


##########################################################
# 创建字典的方法
# 直接创建
dict = {'name':'earth', 'port':'80'}
# 工厂方法
items=[('name','earth'),('port','80')]
dict2=dict(items)
dict1=dict((['name','earth'],['port','80']))
# fromkeys()方法
dict1={}.fromkeys(('x','y'),-1)
dict={'x':-1,'y':-1}
dict2={}.fromkeys(('x','y'))
dict2={'x':None, 'y':None}


##########################################################
# 链表成对调换
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head != None and head.next != None:
            next = head.next
            head.next = self.swapPairs(next.next)
            next.next = head
            return next
        return head


##########################################################
#去除列表中的重复元素

# 用集合
list(set(l))
# 用字典并保持顺序
l1 = ['b','c','d','b','c','a','a']
l2 = list(set(l1))
l2.sort(key=l1.index)
print l2
# 列表推导式
l1 = ['b','c','d','b','c','a','a']
l2 = []
[l2.append(i) for i in l1 if not i in l2]


##########################################################
#快排
def qsort(seq):
    if seq==[]:
        return []
    else:
        pivot=seq[0]
        lesser=qsort([x for x in seq[1:] if x<pivot])
        greater=qsort([x for x in seq[1:] if x>=pivot])
        return lesser+[pivot]+greater

if __name__=='__main__':
    seq=[5,6,78,9,0,-1,2,3,-65,12]
    print(qsort(seq))

##########################################################
# 找零
def  coinChange(values, money, coinsUsed):
    #values    T[1:n]数组
    #valuesCounts   钱币对应的种类数
    #money  找出来的总钱数
    #coinsUsed   对应于目前钱币总数i所使用的硬币数目
    for cents in range(1, money+1):
        minCoins = cents     #从第一个开始到money的所有情况初始
        for value in values:
            if value <= cents:
                temp = coinsUsed[cents - value] + 1
                if temp < minCoins:
                    minCoins = temp
        coinsUsed[cents] = minCoins
        print('面值为：{0} 的最小硬币数目为：{1} '.format(cents, coinsUsed[cents]) )

if __name__ == '__main__':
    values = [ 25, 21, 10, 5, 1]
    money = 63
    coinsUsed = {i:0 for i in range(money+1)}
    coinChange(values, money, coinsUsed)